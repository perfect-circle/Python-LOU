# -*- coding: utf-8 -*-

import re
from datetime import datetime
from collections import Counter

def open_parser(filename):
    with open(filename) as logfile:
        pattern = (
                r'(\d+.\d+.\d+.\d+.)\s-\s-\s'   # IP地址
                r'\[(.+)\]\s'    # 时间
                r'"GET\s(.+)\s\w+/.+"\s'   # 返回路径
                r'(\d+)\s'      # 状态码
                r'(\d+)\s'      # 数据大小
                r'"(.+)"\s'     # 请表头
                r'"(.+)"'       # 客户端信息
                )
        parsers = re.findall(pattern, logfile.read())
    return parsers

def main():
    """计算"""
    logs = open_parser('nginx.log')
    ip_list = []
    url_list = []
    for log in logs:
        dt = datetime.strptime(log[1][:-6], "%d/%b/%Y:%H:%M:%S")
        # 获取11日当天的数据，返回满足要求的IP
        if int(dt.strftime('%d')) == 11 and int(dt.strftime('%Y')) == 2017:
            ip_list.append(log[0])
        # 获取状态码为404，请求为GET的请求地址
        if log[3] == '404':
            url_list.append(log[2])

    max_ip = Counter(ip_list).most_common(1)
    ip_dict = {max_ip[0][0]:max_ip[0][1]}
    max_url = Counter(url_list).most_common(1)
    url_dict = {max_url[0][0]:max_url[0][1]}
    return ip_dict, url_dict

if __name__ == "__main__":
    ip_dict, url_dict = main()
    print(ip_dict, url_dict)
