#!/usr/bin/env python
#coding:utf-8

from sgmllib import SGMLParser
import urllib2

class Parser(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)

		self.test_ul = 0
		self.test_li = 0
		self.test_a = 0
		self.test_span = 0

		self.data = None

		self.list = []

		self.date = None
		self.title = None

	def start_ul(self, attrs):
		for k, v in attrs:
			if k == "class" and v == "newUpdate":
				self.test_ul = 1

	def end_ul(self):
		if self.test_ul == 1:
			self.test_ul = 0

	def start_li(self, attrs):
		if self.test_ul == 1:
			self.test_li = 1

	def end_li(self):
		if self.test_li == 1:
			self.test_li = 0
			self.list.append((self.title, self.date))

	def start_a(self, attrs):
		if self.test_li == 1:
			self.test_a = 1

	def end_a(self):
		if self.test_li == 1:
			self.test_a = 0

	def start_span(self, attrs):
		if self.test_li == 1:
			self.test_span = 1

	def end_span(self):
		if self.test_li == 1:
			self.test_span = 0

	def handle_data(self, data):
		if self.test_span == 1:
			self.date = data
		elif self.test_a == 1:
			self.title = data

URL = "http://www.hltm.cc"

class HLParser:
	def __init__(self):
		self.p = Parser()
		self.new_dict = {}
		self.all_dict = {}
		self.newdate = None
		self.html = None

		self.all_output = ""
		self.new_output = ""
	
	def fetch(self):
		self.html = urllib2.urlopen(URL).read().decode("gbk").encode("utf-8")
		# with open("input.html") as f:
		# 	self.html = f.read()

	def feed(self):
		self.p.feed(self.html)

	def run(self):
		self.fetch()
		self.feed()
		p = 0

		for title, date in self.p.list:
			if not self.all_dict.has_key(date):
				self.all_dict[date] = []
				self.all_dict[date].append(p)
				self.newdate = self.newdate and self.newdate or date
				p += 1

			self.all_dict[date].append(title)
		
			self.new_dict[self.newdate] = self.all_dict[self.newdate]

	def new(self):
		return sorted(self.new_dict.iteritems(), key = lambda x : x[1][0])

	def all(self):
		return sorted(self.all_dict.iteritems(), key = lambda x : x[1][0])

def test():
	p = HLParser()
	p.run()
	print p.new()
	print p.all()

if __name__ == "__main__":
	test()
