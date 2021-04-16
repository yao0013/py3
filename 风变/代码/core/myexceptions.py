# -*- coding: utf-8 -*-


class JsonSerializeException(Exception):
    def __str__(self):
        print("Api fields parse json fail")


class RequestMethodException(Exception):
    def __str__(self):
        print("api request method not supported, The following types of request methods are supported: "
              "get/post/put/delete/patch")

    def __init__(self, err="api request method not supported"):
        Exception.__init__(self, err)


class ResponseJsonException(Exception):
    def __str__(self):
        print("serialize api response to json format fail")

    def __init__(self, err="serialize api response to json format fail"):
        Exception.__init__(self, err)


class TestcaseTypeErrorException(Exception):
    def __str__(self):
        print("testcase type is not a dict type")

    def __init__(self, err="testcase type is not a dict type"):
        Exception.__init__(self, err)


class ObjectTypeErrorException(Exception):
    def __str__(self):
        print("need to compare object type error")

    def __init__(self, err="need to compare object type error"):
        Exception.__init__(self, err)


class VarReplaceException(Exception):
    def __str__(self):
        print("testcase var replace fail")

    def __init__(self, err="testcase var replace fail"):
        Exception.__init__(self, err)


