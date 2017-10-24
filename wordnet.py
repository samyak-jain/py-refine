import requests
import os
import tornado.auth
import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from bcnf import getBCNF
from tornado.options import define, options

define("port", default=8000, help="runs on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
    	URL = "http://ws4jdemo.appspot.com/?mode=w&s1=&w1=name%23n%231&s2=&w2=doctor%23n%231"


class NormHandler(tornado.web.RequestHandler):
	def get(self):
        data = tornado.escape.json_decode(self.request.body)
        cols = data['cols']
        fds = data['fds']
        s = getBCNF(cols, fds)
        self.write({'data': s})    	


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/norm", NormHandler)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(os.environ.get("PORT",options.port))
    tornado.ioloop.IOLoop.instance().start(