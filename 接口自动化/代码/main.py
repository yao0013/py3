# -*- coding: utf-8 -*-
import pytest
import pytz
import argparse
from datetime import datetime
from core.case_parse.base import Process
from core.case_parse.generator import Generator
from core.results import RS


def run():
    testsuites = Process(filepath="D:\\listtest\\接口自动化\\代码\\case.xls")
    gn = Generator(testsuites)
    gn.generate_common_test()
    gn.generate_testsuite()
    now_time = datetime.now(tz=pytz.timezone("Asia/Shanghai")).strftime("%Y-%m-%d_%H-%M-%S")
    pytest.main(["D:\\listtest\\接口自动化\\代码\\case.xls", "-v", "-s", "--alluredir=./reports/{}".format(now_time)])
    RS.save()  # 保存测试结果到Excel文件


if __name__ == '__main__':
    run()
