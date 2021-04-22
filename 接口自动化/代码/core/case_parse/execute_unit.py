# -*- coding: utf-8 -*-
import random
import string
import re
import json
import jmespath

from core.logs import log
from core.myexceptions import TestcaseTypeErrorException, VarReplaceException, ResponseJsonException
from string import Template


def generate_random_str(lenght=16):
    """
    func: 生成随机字符串
    :param lenght: 字符串的长度
    :return: 随机字符串
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(lenght))


class VarReplace(object):
    def __init__(self, case, object_list):
        self.case = case
        self.object_list = object_list
        self.backup_case = case
        self.interface_vars = {}

    def var_replace(self):
        self.var_add_random_str()
        self._var_replace()
        log.info(Template("变量替换后的用例信息:$case").substitute(case=self.case))
        return self.case

    def _var_replace(self):
        """
        功能：解析测试用例中是否存在需要变量替换的字符串
        流程：根据传入的用例和需要检查的对象列表，判断对象列表中是否包含有用例中需要转换的变量字符串，如果有，则将对应的字符串转换为对应的变量值
        """
        case = self.case
        object_list = self.object_list
        if not isinstance(case, dict):
            raise TestcaseTypeErrorException()
        if not isinstance(object_list, list):
            raise TypeError("object list is not a list object")
        self._add_interface_vars()
        object_list.append(self)
        pattern_front = re.compile(r"@{")
        pattern_back = re.compile(r"@}")
        random_front = generate_random_str()
        random_back = generate_random_str()
        try:
            content = json.dumps(case, ensure_ascii=False)
        except Exception as e:
            log.error(string.Template("testcase json dumps fail, error info: $e").substitute(e=e))
            raise VarReplaceException
        content = re.sub(pattern_front, random_front, content)
        content = re.sub(pattern_back, random_back, content)
        # log.debug(string.Template("after replaced random string: $content").substitute(content=content))
        pattern = re.compile(r"\{\w+\}")
        key_words = re.findall(pattern, content)
        log.debug(string.Template("所有需要进行变量替换的变量为: $key_words").substitute(key_words=key_words))

        if key_words:
            """
            循环遍历所有待替换的字符，如果待替换的字符在传入的对象列表中有对应的属性，则进行替换
            否则不作处理
            对象替换按传入的对象的下标进行排序，匹配到了之后，退出循环，即取最先匹配到的对象的属性值
            """
            for key_word in key_words:
                real_word = key_word.lstrip('{').rstrip('}')
                for index in range(0, len(object_list)):
                    log.debug(Template("$o对象的所有属性$a").substitute(o=object_list[index].__class__.__name__, a=object_list[index].__dict__))
                    if not hasattr(object_list[index], "interface_vars"):
                        log.debug(Template("$o对象没有interface_vars属性").substitute(o=object_list[index]))
                        continue
                    attr_dict = object_list[index].__dict__
                    interface_var_dict = attr_dict["interface_vars"]  # 获取对象的所有属性值
                    if real_word in interface_var_dict:
                        log.debug(Template("正在替换变量：$s").substitute(s=real_word))
                        content = content.replace(key_word, str(interface_var_dict[real_word]))
                        break

        content = content.replace(random_front, r'{')
        content = content.replace(random_back, r'}')
        try:
            json_content = json.loads(content)
            self.case = json_content
        except Exception as e:
            log.error(string.Template("testcase json loads fail, the error info: $e").substitute(e=e))
            raise VarReplaceException

    def var_add_random_str(self):
        case = self.case
        if not isinstance(case, dict):
            raise TestcaseTypeErrorException()

        pattern_random = re.compile(r"@$")
        random_str = generate_random_str()
        try:
            content = json.dumps(case, ensure_ascii=False)
        except Exception as e:
            log.error(string.Template("testcase json dumps fail, error info: $e").substitute(e=e))
            raise VarReplaceException
        content = re.sub(pattern_random, random_str, content)
        # log.debug(string.Template("after replaced random string: $content").substitute(content=content))
        pattern = re.compile(r"\$\S+\$")
        key_words = re.findall(pattern, content)
        log.debug(string.Template("所有需要添加随机字符的变量为: $key_words").substitute(key_words=key_words))

        if key_words:
            """
            循环遍历所有待替换的字符，如果待替换的字符在传入的对象列表中有对应的属性，则进行替换
            否则不作处理
            对象替换按传入的对象的下标进行排序，匹配到了之后，退出循环，即取最先匹配到的对象的属性值
            """
            for key_word in key_words:
                real_word = key_word.lstrip('$').rstrip('$')

                log.debug(Template("正在替换变量：$s").substitute(s=real_word))
                content = content.replace(key_word, real_word+generate_random_str(8))

        content = content.replace(random_str, r'$')
        try:
            json_content = json.loads(content)
            self.case = json_content
            return json_content
        except Exception as e:
            log.error(string.Template("testcase json loads fail, the error info: $e").substitute(e=e))
            raise VarReplaceException

    def _add_interface_vars(self):
        case = self.case
        params = case['params']
        header = case['header']
        if params:
            for k, v in params.items():
                self.interface_vars[k] = v
        if header:
            for k, v in header.items():
                self.interface_vars[k] = v


def parse_interface_var(source: object, response: object) -> object:
    var_dict = {}

    for k, v in source.items():
        try:
            var_dict[k] = jmespath.search(v, response)
        except Exception as e:
            log.error(string.Template("get interface_var:$v from response fail,error info: $e").substitute(v=v, e=e))
    return var_dict


def check_verify_fields(fields, response):
    error_info = ""
    if not fields:
        return error_info
    if not isinstance(fields, dict):
        raise TypeError("need to verify fields is not a dict")
    for k, v in fields.items():
        try:
            # if str(v) != str(eval("response" + k)):
            if str(v) != str(jmespath.search(k, response)):
                error_info += Template("response $k not equal $v, real value is: $response").substitute(k=k, v=v, response=str(eval("response" + k)))
        except Exception as e:
            error_info += Template("对比结果$k时出现异常，异常信息:$e").substitute(k=k, e=e)
    return error_info


def check_response_text(fields, response):
    error_info = ""
    log.debug(Template("fields: $fields, response: $response").substitute(fields=fields, response=response))
    if not fields:
        return error_info
    if not isinstance(fields, str):
        raise TypeError("neet to check fields is not a str")
    for text in fields.split(','):
        text = text.lstrip("'").lstrip('"').rstrip("'").rstrip('"')
        log.debug(Template("待校验的内容: $text").substitute(text=text))
        if isinstance(response, dict):
            # if not response.get(text):
            isempty = jmespath.search(text, response)
            if isempty is None:
                error_info += Template("接口响应内容没有待校验的字段:$t，响应内容:$res").substitute(t=text, res=response)
        else:
            if text not in response:
                error_info += Template("接口响应内容没有待校验的字段:$t，响应内容:$res").substitute(t=text, res=response)

    return error_info


def check_response_header(fields, headers):
    error_info = ""
    if not fields:
        return error_info
    log.debug(Template("fields: $fields, headers: $headers").substitute(fields=fields, headers=headers))
    if not fields:
        return error_info
    if not isinstance(fields, str):
        log.debug(type(fields))
        log.debug(fields)
        raise TypeError("neet to check fields is not a str")
    for text in fields.split(','):
        text = text.lstrip("'").lstrip('"').rstrip("'").rstrip('"')
        if isinstance(headers, dict):
            # if not headers.get(text):
            isempty = jmespath.search(text, headers)
            if isempty is None:
                error_info += Template("接口响应内容没有待校验的字段:$t，响应内容:$res").substitute(t=text, res=headers)
        else:
            if text not in headers:
                error_info += Template("接口响应内容没有待校验的字段:$t，响应内容:$res").substitute(t=text, res=headers)

    return error_info


def check_status_code(code, response):
    error_info = ""
    if not code:
        return error_info
    try:
        code = int(code)
    except Exception as e:
        log.error(Template("接口响应状态码入参错误，请检查, 入参值：$code").substitute(code=code))
        error_info += Template("接口响应状态码入参错误，请检查, 入参值：$code").substitute(code=code)
        return error_info
    if code != response:
        error_info += Template("接口响应码校验失败:预期值：$n，响应值:$res").substitute(n=code, res=response)
    return error_info


def check_response_time(_time, response):
    error_info = ""
    if not _time:
        return error_info
    try:
        _time = float(_time)
        if _time < response:
            log.error(Template("接口响应时间超时，期望值: $t， 响应值: $r").substitute(t=_time, r=response))
            error_info += Template("接口响应时间超时，期望值: $t， 响应值: $r").substitute(t=_time, r=response)
            return error_info
    except Exception as e:
        log.error(Template("接口响应时间入参错误，请检查: $t").substitute(t=_time))
        error_info += Template("接口响应时间入参错误，请检查: $t").substitute(t=_time)
        return error_info


def check_pyexpression(pys, response):
    error_info = ""
    response = response
    exe_pys = []
    if not pys:
        return error_info
    if isinstance(pys, list):
        exe_pys = pys
    elif isinstance(pys, str):
        exe_pys.append(pys)
    else:
        error_info += "py表达式入参错误，参数仅支持列表和字符串格式"
        return error_info
    for py in exe_pys:
        try:
            if not eval(py):
                log.error(Template("py表达式执行失败，表达式内容：$py").substitute(py=py))
                error_info += (Template("py表达式执行失败，表达式内容：$py").substitute(py=py))
        except Exception as e:
            error_info += Template("执行py表达式异常，表达式内容：$py, 异常信息：$e").substitute(py=py, e=e)

    return error_info
