#!/usr/bin/env python3
# encoding=utf-8


import pytest

def test_assert():
    assert True

import inspect
def check(fn):
    def wrapper(*args,**kwargs):
        sig = inspect.signature(fn)
        param = sig.parameters
        values = list(param.values())
        for i,v in enumerate(args):
            if values[i].annotation is not inspect._empty and not isinstance(v,values[i].annotation):
                print('!==')
            for k,t in kwargs.items():
                if param[k].annotation is not inspect._empty and not isinstance(t,param[k].annotation):
                    print('!===')
            ret = fn(*args,**kwargs)
            return ret
        return wrapper

@check
def add(x:int,y:int=7)-> int:
    return x + y

print(add(x=1,y=1))

