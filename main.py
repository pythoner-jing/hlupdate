#coding:utf-8

import tornado.ioloop
import tornado.web
from tornado.options import define, options

import os
import torndb

from parser import Parser, HLParser

if "SERVER_SOFTWARE" in os.environ:
	from sae.const import (MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB)
else:
	MYSQL_HOST = "localhost:3306"
	MYSQL_USER = "root"
	MYSQL_PASS = ""
	MYSQL_DB = "app_hlupdate"

define("port", default = 8888)
define("diff_limit", default=1, help="limit of minute'difference")
# define("mysql_host", default="127.0.0.1:3306", help="database host")
# define("mysql_database", default="hlupdate", help="database name")
# define("mysql_user", default="root", help="database user")
# define("mysql_password", default="", help="database password")


def update(db):
	p = HLParser()
	p.run()
	update = p.all()

	items = map(lambda x : (x[0], x[1][1:]), update)

	delete_list_sql = "DELETE FROM List"
	insert_list_sql = "INSERT INTO List(title, updatedate, orderno) VALUES(%s, %s, %s)"
	delete_context_sql = "DELETE FROM Context"
	insert_context_sql = "INSERT INTO Context(fetchtime) values(NOW())"

	db.update(delete_list_sql)
	db.update(delete_context_sql)

	insert_seq = [(y, x[0], x[1][0]) for x in update for y in x[1][1:]]

	db.insertmany(insert_list_sql, insert_seq)
	db.insert(insert_context_sql)

	return items

def selectNew(db):
	query_sql = "SELECT * FROM List WHERE orderno<=ALL(SELECT orderno FROM List)"
	rs = db.query(query_sql)
	items = [(rs[0]["updatedate"], map(lambda x : x["title"], rs))]

	return items

def select(db):
	query_sql = "SELECT * FROM List"

	all_list = []
	orderno = None
	
	for x in db.query(query_sql):
		if x["orderno"] != orderno:
			orderno = x["orderno"]
			all_list.append((x["updatedate"], [x["title"],]))
		else:
			all_list[-1][1].append(x["title"])
	
	return all_list

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

class IndexHandler(BaseHandler):
	def get(self):
		self.render("index.html")

class NewHandler(BaseHandler):
	def get(self):
		query_context_sql = "SELECT fetchtime FROM Context"
		query_time_sql = "SELECT TIMESTAMPDIFF(MINUTE, %s, now()) AS diff"

		fetchtime = self.db.get(query_context_sql)["fetchtime"]
		diff = self.db.get(query_time_sql, fetchtime)["diff"]

		if diff < options.diff_limit:
			msg = u"距离上次更新小于%s分钟，使用缓存数据" % options.diff_limit
		else:
			msg = u"距离上次更新大于%s分钟，刷新数据库" % options.diff_limit
			update(self.db)

		items = selectNew(self.db)
		return self.render("module.html", msg = msg, items = items)

class AllHandler(BaseHandler):
	def get(self):
		query_context_sql = "SELECT fetchtime FROM Context"
		query_time_sql = "SELECT TIMESTAMPDIFF(MINUTE, %s, now()) AS diff"

		fetchtime = self.db.get(query_context_sql)["fetchtime"]
		diff = self.db.get(query_time_sql, fetchtime)["diff"]

		if diff < options.diff_limit:
			msg = u"距离上次更新小于%s分钟，使用缓存数据" % options.diff_limit
			items = select(self.db)
		else:
			msg = u"距离上次更新大于%s分钟，刷新数据库" % options.diff_limit
			items = update(self.db)

		return self.render("module.html", msg = msg, items = items)

class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "template"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            debug = True,
        )

        handlers = [
            (r"/$", IndexHandler),
            (r"/new$", NewHandler),
            (r"/all$", AllHandler),
        ]
        
        tornado.web.Application.__init__(self, handlers, **settings)

        self.db = torndb.Connection(
        	MYSQL_HOST,
        	MYSQL_DB,
        	MYSQL_USER,
        	MYSQL_PASS,
        )

if __name__ == "__main__":
	Application().listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
