#!/usr/bin/python
#coding:utf8
'''


@author: Kenny.Li
'''
import urllib2
try:
    response = urllib2.urlopen('http://www.baidu.com')
except urllib2.HTTPError, e:
    print e.code