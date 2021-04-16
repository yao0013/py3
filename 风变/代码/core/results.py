# -*- coding: utf-8 -*-

import xlwt
from xlwt import Style
import os
import pytz
from datetime import datetime
from configs import settings
from core.logs import log
from string import Template


class ResultSave(object):
    def __init__(self):
        self.parent_dir = settings.excel_reports_path
        if not os.path.isdir(self.parent_dir):
            os.makedirs(self.parent_dir)
        self.sheet = None
        self.sheet_info = {}
        self._init_workbook()
        self.sheet_title = ["casename", "url", "method", "params", "header", "response", "status_code", "response_time"]

    def _init_workbook(self):
        now_time = datetime.now(tz=pytz.timezone("Asia/Shanghai")).strftime("%Y-%m-%d_%H-%M-%S")
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.file_name = "{}.xls".format(now_time)

    def write_row(self, sheet_name, start_row, start_col, data_list, style=Style.default_style):
        if not isinstance(sheet_name, str) and not isinstance(data_list, list):
            log.error("要写入的结果的入参类型错误")
            return False

        if sheet_name not in self.sheet_info:
            self.sheet = self.workbook.add_sheet(sheet_name, cell_overwrite_ok=True)
        else:
            self.sheet = self.workbook.get_sheet(sheet_name)
        for col, data in enumerate(data_list):
            try:
                data = str(data)
            except Exception as e:
                log.error(Template("待写入的数据无法格式化为string格式，写入异常：$e").substitute(e=e))
                data = "format error"
            self.sheet.write(start_row, start_col+col, data, style)

    def append_row(self, sheet_name, data_list, passed):
        """
        往Excel表格中追加数据
        :param sheet_name:
        :param data_list:
        :param passed 用例是否执行通过
        :return:
        """
        passed = passed or 'PASS'
        if not isinstance(data_list, list):
            log.error("要写入的结果的入参类型错误")
            return False
        if sheet_name not in self.sheet_info:
            self.sheet = self.workbook.add_sheet(sheet_name, cell_overwrite_ok=True)
            self.sheet_info[sheet_name] = {"row": 1, "col": 0}
            self.write_row(sheet_name, 0, 0, self.sheet_title)
        else:
            self.sheet = self.workbook.get_sheet(sheet_name)
        row = self.sheet_info[sheet_name]['row']
        col = self.sheet_info[sheet_name]['col']

        if passed.upper() == 'PASS':
            style = self.set_style('green')
        elif passed.upper() == 'FAIL':
            style = self.set_style('red')
        elif passed.upper() == 'WARNING':
            style = self.set_style('yellow')
        else:
            style = self.set_style('green')
        try:
            self.write_row(sheet_name, row, col, data_list, style)
        except Exception as e:
            log.error(Template("往Excel表格中写入数据异常,异常信息：$e").substitute(e=e))
        self.sheet_info[sheet_name]['row'] += 1

    def save(self):
        self.workbook.save(os.path.join(self.parent_dir, self.file_name))

    @classmethod
    def set_style(cls, color):
        style = Style.XFStyle()
        pattern = xlwt.Pattern()
        pattern.pattern = pattern.SOLID_PATTERN
        if color == 'red':
            pattern.pattern_fore_colour = Style.colour_map['red']
        elif color == 'green':
            pattern.pattern_fore_colour = Style.colour_map['green']
        elif color == 'yellow':
            pattern.pattern_fore_colour = Style.colour_map['yellow']
        style.pattern = pattern
        return style


RS = ResultSave()
