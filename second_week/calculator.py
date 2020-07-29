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

    def _read_command(self, option):
        """输入参数，返回参数后的值"""
        try:
            index = self.args.index(option)
            return self.args[index + 1]
        except:
            print('Parameter Error')
            exit()

    @property
    def config_path(self):
        """返回配置文件路径"""
        return self._read_command('-c')

    @property
    def userdata_path(self):
        """返回用户数据文件"""
        return self._read_command('-d')

    @property
    def export_path(self):
        return self._read_command('-o')

args = Argv()

class Config(object):
    """提取配置文件信息"""

    def __init__(self):
        self.config = self._read_config

    def _read_config(self):
        """读取配置文件"""

        config = {}
        with open(args.config_path) as f_ob:
            for line in f_ob.readlines():
                key,value = line.strip().split('=')
                try:
                   config[key.strip()] = float(value.strip())
                except:
                    print("Parameter  Error")
                    exit()

    def _get_config(self, key):
        """获取配置文件"""
        try:
            return self.config[key]
        except:
            print("Config Error")
            exit()

    @property
    def social_insurance_baseline_low(self):
        return self._get_config('JiShuL')

    @property
    def social_insurance_baseline_high(self):
        return self._get_config('JiShuH')

    @property
    def social_insurance_total(self):
        return sum([
            self._get_config('YangLao'),
            self._get_config('YiLiao'),
            self._get_config('ShiYe'),
            self._get_config('GongShang'),
            self._get_config('ShengYu'),
            self._get_config('GongJiJin')
            ])

config = Config()

class UserData(object):
    """获取员工数据"""

    def __init__(self):
        self.userdata = self._read_users_data

    def _read_users_data(self):
        """读取与员工数据"""
        userdata = []
        with open(args.userdata_path) as f_ob:
            for line in f_ob.readlines():
                id_user, income_string = line.strip().split(',')
                try:
                    income = int(income_string)
                except:
                    print("Parameter Error")
                    exit()
                userdata.append((id_user, income))
        return userdata

    def __iter__(self):
        return iter(self.userdata)

class IncomeTaxCalculator(object):
    """税后工资计算类"""

    def __init__(self,userdata):
        self.userdata = userdata

    @staticmethod
    def calc_social_indurance_moeny(income):
        """计算社保金额"""
        if income < config.social_insurance_baseline_low:
            return config.social_insurance_baseline_low * config.social_insurance_total

        if income > config.social_insurance_baseline_high:
            return config.social_insurande_baseline_high * config.social_insurance_total
        else:
            return income * config.social_insurance_total

    @classmethod
    def calc_income_tax_and_remain(cla,income):
        """计算税后工资"""

        # 计算社保金额
        social_insurance_money = cls.calc_social_insurance_money(income)

        # 计算应纳税额
        real_income = income - social_insurance_money
        taxable_part = real_income - INCOME_TAX_START_POINT

        # 从高到第判断落入的税率区间，如果找到则用该区间的参数计算纳税额并返回结果
        for item in INCOME_TAX_QUICK_LOOKUP_TABLE:
            if taxable_part > item.start_point:
                tax = taxable_part * item.tax_rate + item.quick_subtractor
                return '{:.2f}'.format(tax), '{:.2f}'.format(real_income - tax)

        return '0.00', '{:.2f}'.format(real_income)

    def calc_for_all_userdata(self):
        """计算所有用户的税后工资"""
        result = []
        for id_user, income in self.userdata:
            # 计算社保金额
            social_insurance_money = '{:.2f}'.format(
                    self.calc_social_insurance_money(income))

            # 计算税后工资
            tax, remain = self.calc_income_tax_and_remain(income)

            # 添加到结果集
            result.append([id_user, income, social_insurance_money, tax, remain])

        return result

    def export(self):
        """导出所有用户"""

        # 计算所有用户的税后工资
        result = self.calc_for_all_userdata()

        with open(args.export_path, 'w', newline='') as f_ob:
            # 创建CSV文件写入对象
            writer = csv.writer(f_ob)
            # 写入多行
            writer.writerows(result)

if __name__ == "__main__":
    # 创建税后工资计算器
    calculator = IncomeTaxCalculator(UserData())

    # 调用export方法导出税后工资到文件
    calculator.export()
