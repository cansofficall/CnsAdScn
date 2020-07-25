#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Site Adı \n(Domain : example.com Yada www.example.com ): ")
	print "\n\Mevcut Köprüler : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "Başarılı => ",req_link
def Credit():
	
	Space(9); print "              CnsAdScn.py           "
	Space(9); print"       İnstagram can_s_officiall     "
	Space(9); print "            ÇevrilmişProgram        "

Credit()
findAdmin()
