#!/usr/bin/python
#coding:utf8
'''
Created on 2015年11月13日

@author: Kenny.Li
'''
import urllib2,time

class Touch():
    global url
    invitationCode = raw_input("Enter the invitation code :")
    url = "http://ws2.cootekservice.com/voip/tmp_invitation?invitation="+invitationCode+"&phone="
    def createPhoneNumber(self,phoneNumberHead):
        for i in xrange(0,10):
            for j in xrange(0,10):
                for k in xrange(0,10):
                    for l in xrange(0,10):
                        time.sleep(2)
                        phoneNumber = phoneNumberHead+str(i)+str(j)+str(k)+str(l)
                        print phoneNumber
                        try:
                            response = urllib2.urlopen(url+phoneNumber)
                        except urllib2.HTTPError, e:
                            print e.code
            
myTouch = Touch()
phoneNumber = raw_input("Enter the phone number head:")
myTouch.createPhoneNumber(phoneNumber)
