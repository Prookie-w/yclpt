#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
class wyf():

    def info(self, a, *name, **addr):
        print('a is', a)
        for s in name:
            print('name', s)

        for local, floor in addr.items():
            print(local, 'is', floor)



if __name__ == '__main__':
    wyf().info(10, 1, 2, 3, 4, 5, heida=31, suning=22, huayu=77)



