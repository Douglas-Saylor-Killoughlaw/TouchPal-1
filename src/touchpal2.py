#!/usr/bin/python
#coding:utf8
'''
Created on 2015年11月13日

@author: Kenny.Li
'''
import urllib2,time

k = {1:"R4PbXzL"}
class Touch():
    print k[1]
    phoneNumber = None
    def __init__(self):
        self.invitationCode = raw_input("Enter the invitation code :")
        self.phoneNumberHead = raw_input("Enter the phone number head:")
        self.start = raw_input('input start:')
        self.end = raw_input('input end:')
        self.url = "http://ws2.cootekservice.com/voip/tmp_invitation?invitation="+self.invitationCode+"&phone="
    
    def createPhoneNumber(self,phoneNumberHead):
        for i in xrange(int(self.start),int(self.end)+1):
            tail = '{:0>4}'.format(i)# 参见format函数的用法
            phoneNumber = self.phoneNumberHead+tail
            time.sleep(2)
            print phoneNumber
            try:
                response = urllib2.urlopen(self.url+phoneNumber)
            except urllib2.HTTPError, e:
                print e.code
        Touch.phoneNumber = phoneNumber
    def saveLog(self):
        
        f = open('./log.txt','a+')
        f.write('%s\t****logs****\n'%time.strftime("%H:%M:%S",time.localtime()))
        f.write("invitationCode: %s\n"%self.invitationCode)
#         total = int(self.end)-int(self.start)
        print Touch.phoneNumber
        f.write("end phone number is: %s\n"%Touch.phoneNumber)
        f.close()
        
myTouch = Touch()
myTouch.createPhoneNumber(myTouch.phoneNumberHead)
myTouch.saveLog()
