import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello, world!")


if __name__ == '__main__':
    app = tornado.web.Application([
        ('/', IndexHander),
        ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
