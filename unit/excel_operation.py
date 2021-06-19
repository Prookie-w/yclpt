#!/usr/bin/env python
# -*- coding:utf-8 -*-
import xlrd


class ExcelOperation:
    def __init__(self, file_path, sheet_id):
        self.file_path = file_path
        self.sheet_id = sheet_id
        self.data = self.get_data()
    #
    def get_data(self):
        data = xlrd.open_workbook(self.file_path)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_lines(self):
        tables = self.data
        return tables.nrows

    def get_cell_value(self, row, col):
        data = self.data.cell_value(row, col)
        return data


if __name__ == '__main__':
    # 'E:\\work\\code\\case\\test.xls'
    opers = ExcelOperation('E:\\work\\code\\case\\test.xls', 0)
    print(opers.get_lines())
    print(opers.get_cell_value(1, 0))
