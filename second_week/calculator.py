#!/usr/bin/env python3
import csv
import sys
from collections import namedtuple

# 税率表条目类，该类由namedtuple动态创建，代表一个命名元组：
IncomeTaxQuickLookupItem = namedtuple(
        'IncomeTaxQuickLookupItem',
        ['taxable','taxrate','quick'])

# 起征点
CUTOFF_POINT = 5000

# 税率及速算扣除数对应表：
INCOME_TAX_QUICK_LOOKUP_TABLE = [
        IncomeTaxQuickLookupItem(80000, 0.45, 15160),
        IncomeTaxQuickLookupItem(55000, 0.35, 7160),
        IncomeTaxQuickLookupItem(35000, 0.30, 4410),
        IncomeTaxQuickLookupItem(25000, 0.25, 2660),
        IncomeTaxQuickLookupItem(12000, 0.20, 1410),
        IncomeTaxQuickLookupItem(3000, 0.10, 210),
        IncomeTaxQuickLookupItem(0, 0.03, 0)
        ]

class Argv(object):
    """命令采集类"""
    def __init__(self):
        self.args = sys.argv[1:]

    def _get_args(self,option):
        """输入参数，返回参数后的命令"""
        try:
            index = self.args.index(option)
            return self.args[index + 1]
        except:
            print("Option Error")
            exit()

    @property
    def config_path(self):
        """
        TODO: Docstring for config_path.
        """
        return self._get_args('-c')

    @property
    def userdata_path(self):
        """
        TODO: Docstring for userdata_path.
        """
        return self._get_args('-d')

    @property
    def export_path(self):
        """
        TODO: Docstring for export_path.
        """
        return self._get_args('-o')

args = Argv()

class Config(object):

    """配置文件获取类"""

    def __init__(self):
        """TODO: to be defined. """
        self.config = self._get_config()

    def _get_config(self):
        """
        TODO: Docstring for _get_config.
        """
        config = {}
        with open(args.config_path) as f_ob:
            for line in f_ob.readlines():
                key,value = line.strip().split('=')
                config[key.strip()] = float(value.strip())

        return config

    @property
    def fund_low(self):
        """
        TODO: Docstring for fund_low.
        """
        return self.config['JiShuL']

    @property
    def fund_high(self):
        """
        TODO: Docstring for fund_high.
        """
        return self.config['JiShuH']

    @property
    def social_security_ratio(self):
        """
        TODO: Docstring for social_security_ratio.
        """
        return sum([
                self.config['YangLao'],
                self.config['YiLiao'],
                self.config['ShiYe'],
                self.config['GongShang'],
                self.config['ShengYu'],
                self.config['GongJiJin']
                ])

config = Config()

class UserData(object):

    """处理员工数据类"""

    def __init__(self):
        """TODO: to be defined. """
        self.userdata = self._get_userdata()

    def _get_userdata(self):
        """
        TODO: Docstring for _get_userdata.
        """
        try:
            with open(args.userdata_path) as f_ob:
                userdata = list(csv.reader(f_ob))
            return userdata
        except:
            print("UserData File Error")
            exit()

class Calculator(object):

    """计算结果类"""

    def __init__(self,userdata):
        """
        输入员工数据，返回计算结果
        """
        self._userdata = userdata

    @staticmethod
    def calculator_social_security(income):
        """
        计算社保金额
        """
        if income < config.fund_low:
            return config.fund_low * config.social_security_ratio
        elif income > config.fund_high:
            return config.fund_high * config.social_security_ratio
        else:
            return income * config.social_security_ratio

    @classmethod
    def tax(cls, income):
        """
        计算个税金额
        """
        taxable_income = income - cls.calculator_social_security(income) - CUTOFF_POINT

        for item in INCOME_TAX_QUICK_LOOKUP_TABLE:
            if taxable_income > item.taxable:
                return taxable_income * item.taxrate - item.quick

        return 0.00

    def payroll(self):
        """计算出员工工资单"""
        result = []
        for employee in self._userdata:
            employee_id, income = employee
            income = float(income)
            social_security = Calculator.calculator_social_security(income)
            tax = Calculator.tax(income)
            real_income = income - social_security - tax
            result.append([employee_id, '{:.2f}'.format(income), '{:.2f}'.format(social_security), '{:.2f}'.format(tax), '{:.2f}'.format(real_income)])
        return result

class Export(object):

    """输出到文件类"""

    def __init__(self, result):
        self._result = result

    def export_file(self):
        """
        以CSV格式输入到目标文件
        """
        with open(args.export_path,'w') as f_ob:
            csv.writer(f_ob).writerows(self._result)

if __name__ == '__main__':

    # 获取员工数据
    data = UserData()
    data_list = data.userdata

    # 获取计算结果
    calculator = Calculator(data_list)
    result = calculator.payroll()

    # 输出到目标文件
    export = Export(result)
    export.export_file()
