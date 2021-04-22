# -*- coding: utf-8 -*-
import os
import logging

current_path = os.path.abspath(os.getcwd())

# 日志配置
log_path = os.path.join(current_path, "logs")
log_devel = "DEBUG"

# 模板用例存放目录
template_file_path = os.path.join(current_path, "static")

# 脚本生成的测试用例存放目录
testcase_file_path = os.path.join(current_path, "testcase")

# 接口测试结果存放目录（Excel保存的文件）
excel_reports_path = os.path.join(current_path, "reports")

# 接口测试结果存放目录（allure生成的测试报告）
allure_reports_path = os.path.join(current_path, "reports/Excel")


# Excel用例文件字段对应的列位置
excel_fields = {
    "order": 0,
    "module": 1,
    "casename": 2,
    "description": 3,
    "url": 4,
    "method": 5,
    "params": 6,
    "header": 7,
    "interface_var": 8,
    "wait_time": 9,
    "verify_fields": 10,
    "res_text": 11,
    "res_header": 12,
    "status_code": 13,
    "sql": 14,
    "db_value": 15,
    "expression": 16,
    "response_time": 17,
    "init": 18,
    "restore": 19,
    "dyparam": 20,
    "header_manager": 21,
    "database": 22,
    "iteration": 23,
    "global_var_key": 0,
    "global_var_value": 1
}

fields_mapper = {
    "interface_var": "interface_var",
    "verify_fields": "verify_fields",
    "sql": "sql",
    "expression": "expression",
    "init": "init",
    "restore": "restore",
    "dyparam": "dyparam",
    "header_manager": "header_manager"
}


