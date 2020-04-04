import sys
import json
import tornado.ioloop
import tornado.web
from post_handler import handle_request

PORT = 8888


class Handler(tornado.web.RequestHandler):
    def get(self):
        from db import list_people
        people = list_people(100)
        print("Request received")
        print(people)
        self.write(
            json.dumps(
                people
            )
        )

    def post(self):
        body = json.loads(self.request.body)
        response = handle_request(body)
        self.write(json.dumps(response))


def make_app(autoreload):
    return tornado.web.Application([(r"/", Handler)], autoreload=autoreload)


if __name__ == "__main__":

    print("Starting server on http://localhost:%s/" % PORT)
    autoreload = True if len(
        sys.argv) > 1 and sys.argv[1] == "autoreload" else False
    print("Autoreload: %s" % autoreload)
    app = make_app(autoreload=autoreload)
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()