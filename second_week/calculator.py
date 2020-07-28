#!/usr/bin/env python3

import sys
import csv
from collections import namedtuple

# 税表条目类，该类由namedtuple动态创建，代表一个命名元组
IncomeTaxQuickLookupItem = (
        'IncomTaxQuickLookupItem',
        ['start_point', 'tax_rate', 'quick_subtractor']
        )


# 起征点常量
INCOME_TAX_START_POINT = 5000

# 税率表，里面的元素类型为前面创建的IncomeTaxQuickLookupItem
INCOME_TAX_QUICK_LOOKUP_TABLE = [
        IncomeTaxQuickLookupItem(80000, 0.45, 15160),
        IncomeTaxQuickLookupItem(55000, 0.35, 7160),
        IncomeTaxQuickLookupItem(35000, 0.3, 4410),
        IncomeTaxQuickLookupItem(25000, 0.25, 2660),
        IncomeTaxQuickLookupItem(12000, 0.2, 1410),
        IncomeTaxQuickLookupItem(3000, 0.1, 210),
        IncomeTaxQuickLookupItem(0, 0.03, 0)
]

class Argv(object):
    """提取命令"""
    def __init__(self):
        self.args = sys.argv[1:]

    def read_command(self):
        try:
            for index,arg in enumerate(self.args):
                if arg == '-c':
                    self.sebao_path = self.args[index+1]
                if arg == '-d':
                    self.gz_path = self.args[index+1]
                if arg == '-o':
                    self.gzd_path = self.args[index+1]
        except:
                print("Enter Error")
                exit()
args = Argv()

class Config(object):

    def __init__(self):
        self. 
