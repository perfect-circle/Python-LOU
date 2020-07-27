import sys
from collections import namedtuple

# 税表条目类，该类由namedtuple动态创建，代表一个命名元组
IncomeTaxQuickLookupItem = namedtuple(
        'IncomeTaxQuickLookupItem',
        ['start_point', 'tax_rate','quick_subtractor']
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

# 各种社保缴费比例常量
SOCIAL_INSURANCE_MONEY_RATE = {
        'endowment_insurance': 0.08,
        'medical_insurance': 0.02,
        'unemployment_insurance':0.005,
        'employment_injury_insurance': 0,
        'matermity_insurance': 0,
        'public_accumulation_funds': 0.06
}

def calc_income_tax_and_remain(income):
    """工资纳税计算器"""
    # 计算扣除社保费和起征之后的应税额
    social_insurance_money = income * sum(SOCIAL_INSURANCE_MONEY_RATE.values())
    real_income = income - social_insurance_money
    taxale_part = real_income - INCOME_TAX_START_POINT

    # 从高到低判断落入税率区间，如果找到则用该区间的参数计算纳税额并返回结果
    for item in INCOME_TAX_QUICK_LOOKUP_TABLE:
        if taxale_part >  item.start_point:
            tax = taxale_part * item.tax_rate - item.quick_subtractor
            return '{:.2f}'.format(tax),'{:.2f}'.format(real_income)
    return '0.00', '{:.2f}'.format(real_income)

def main():
    """对命令行的传入的每一个用户，依次调用计算器计算纳税额"""

    # 循环处理每个用户
    for item in sys.argv[1:]:
        # 解析用户ID和工资
        employee_id, income_string = item.split(':')
        try:
            income = int(income_string)
        except ValueError:
            print('Parameter Error')
            continue

        # 调用计算器并打印结果
        _, remain = calc_income_tax_and_remain(income)
        print('{}:{}'.format(employee_id, remain))

if __name__ == "__main__":
    main()
