#!/usr/bin/python
#coding:utf8
'''
Created on 2015年11月13日

@author: Kenny.Li
'''
import urllib2,time

nameList = {"liyifei":"R4PbXzL","douyahuan":"R4229Ow"}
print "Choose the user:"
for k,v in nameList.items():
    print k,"\t---->\t",v
class Touch():
    phoneNumber = None
    def __init__(self):
        self.userName = raw_input("Enter the user name :")
#         print 'invitation code:', nameList[self.userName]
        self.phoneNumberHead = raw_input("Enter the phone number head:")
        self.start = raw_input('input start:\t')
        self.end = raw_input('input end:\t')
        self.url = "http://ws2.cootekservice.com/voip/tmp_invitation?invitation="+nameList[self.userName]+"&phone="
    
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
                print "some error coming ..."
        Touch.phoneNumber = phoneNumber
    def saveLog(self):
        try:
            f = open('./log.txt','a')
            f.write('%s\t****logs****\n'%time.strftime("%H:%M:%S",time.localtime()))
            f.write("user: %s\n"%self.userName)
            f.write("invitationCode: %s\n"%nameList[self.userName])
    #         total = int(self.end)-int(self.start)
#             print Touch.phoneNumber
            f.write("end phone number is: %s\n"%Touch.phoneNumber)
        except Exception,e:
            print "End by user..."
            print e
        f.close()
        
myTouch = Touch()
myTouch.createPhoneNumber(myTouch.phoneNumberHead)
myTouch.saveLog()
print "Mission Complete!"
