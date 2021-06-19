#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json


class JsonOperation:
    def __init__(self, file_path):
        with open(file_path) as fp:
            self.data = json.load(fp)

    def read_data(self, para):
        return self.data[para]


if __name__ == '__main__':
    js =JsonOperation('')
    print(js.read_data(''))
