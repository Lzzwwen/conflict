import tornado.web
import tornado.ioloop

import handlers

if __name__ == '__main__':
    app = tornado.web.Application(handlers.url)
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
