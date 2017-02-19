import sys
import os
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        self.render('www/index.html')


urls = [
    # (r"/", tornado.web.StaticFileHandler, dict(path=os.path.join(os.path.dirname(__file__), 'www')+"/index.html")),
    (r"/", MainHandler),
    (r"/index.html", MainHandler),
]

application = tornado.web.Application(urls)

if __name__ == "__main__":
    import logging
    logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                        format='%(asctime)s %(levelno)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    application.listen(8002)
    tornado.ioloop.IOLoop.instance().start()
