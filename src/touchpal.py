#!/usr/bin/python
#coding:utf8
'''
Created on 2015��11��13��

@author: Kenny.Li
'''
import urllib2,time

class Touch():
    global url
    url = "http://ws2.cootekservice.com/voip/tmp_invitation?invitation=JSVVT73IUN&phone="   
    def createPhoneNumber(self,phoneNumberHead):
        
        for i in xrange(0,10):
            for j in xrange(0,10):
                for k in xrange(0,10):
                    for l in xrange(0,10):
                        time.sleep(10)
                        phoneNumber = phoneNumberHead+str(i)+str(j)+str(k)+str(l)
                        try:
                            response = urllib2.urlopen(url+phoneNumber)
                        except urllib2.HTTPError, e:
                            print e.code
            
myTouch = Touch()
myTouch.createPhoneNumber("1353072")
