#!/usr/bin/env python3
# encoding=utf-8


import responser


api = responser.API(yaml_allowed=True)


@api.route("/")
def hello(req, resp):
    resp.status = responser.http_status.ok
    resp.media = {"hello": "world"}
    resp.text = ""
    resp.content = ""


class ThingsResource:
    def on_request(self, req, resp):
        resp.status = responser.status.HTTP_200



api.add_route("/{hello}", ThingsResource)
print(api.routes)

