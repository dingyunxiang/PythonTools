# coding:utf-8
#用于检测ip段内可用的ip地址,来避免Ip冲突
import time, os

ip = '202.118.212.'


def ping_test(ip, length):
    result = 0
    for num in range(length):
        ip_new = ip + str(num)
        result = os.system('ping -o -t 1 %s' % ip_new)  # -o ping成功后自动退出  -t 等待时间设为1
        if result:
            print "fail" + ip_new
        else:
            print "success" + ip_new


ping_test(ip, 256)
