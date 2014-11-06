#!/usr/bin/env python
#coding:utf-8

import torndb

db = torndb.Connection("127.0.0.1:3306", "hlupdate", user="root", password="")
query_sql = "SELECT * FROM List"
all_list = []
orderno = None

for x in db.query(query_sql):
	if x["orderno"] != orderno:
		orderno = x["orderno"]
		all_list.append((x["updatedate"], [x["title"],]))
	else:
		all_list[-1][1].append(x["title"])

print all_list