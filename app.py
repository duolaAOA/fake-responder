#!/usr/bin/env python3
# encoding=utf-8

import graphene

import responser

api = responser.API(static="static")
# api.mount('/subapp', other_wsgi_app)


@api.route("/")
def hello(req, resp):
    print(resp)
    # resp.status = responser.status.ok
    resp.media = {"hello": "world"}


class ThingsResource:
    def on_request(self, req, resp):
        resp.status = responser.status.HTTP_200
        resp.media = ["ylolo"]


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return "Hello " + name


schema = graphene.Schema(query=Query)

print(api.session().get(
    "http://app/graph?q={ hello }",
    headers={
        "Accept": "application/x-yaml"
    },
    # data="hello",
).text)
