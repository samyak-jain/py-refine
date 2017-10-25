import requests
import os
import tornado.auth
import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json

from bcnf import getBCNF
from tornado.options import define, options

define("port", default=8000, help="runs on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        URL = "http://ws4jdemo.appspot.com/?mode=w&s1=&w1=name%23n%231&s2=&w2=doctor%23n%231"


class NormHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        self.set_header('Access-Control-Allow-Methods', ' PUT, DELETE, OPTIONS')

    def get(self):
        data = json.loads(self.get_argument('data'))
        cols = data['cols']
        for i in range(len(cols)):
            cols[i] = cols[i].replace('\xa0', '')
        rows = data['myrows']
        fds = {}
        for i in rows:
            x = i.get('LHS').split(',')
            for abc in range(len(x)):
                x[abc] = x[abc].replace('\xa0', '')
            y = i.get('RHS').split(',')
            for abc in range(len(y)):
                y[abc] = y[abc].replace('\xa0', '')
            fds[tuple(x)] = y

        print(cols, fds)

        s = getBCNF(cols, fds)
        self.write({'data': s})

    def options(self):
        # no body
        self.set_status(204)
        self.finish()


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
    tornado.ioloop.IOLoop.instance().start()