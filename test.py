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

p = Parser()

html = urllib2.urlopen("http://www.hltm.cc").read().decode("gb2312").encode("utf-8")

p.feed(html)
new_list = {}
all_list = {}
newdate = None

for title, date in p.list:
	if not all_list.has_key(date):
		all_list[date] = []
		newdate = newdate and newdate or date
	all_list[date].append(title)

new_list[newdate] = all_list[newdate]

for k in sorted(all_list.keys(), reverse = True):
	print "%s:" % k
	for v in all_list[k]:
		print v