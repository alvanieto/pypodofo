# -*- coding: utf-8 -*-

from . import api as basic_api


def error_parser(function):

    def decorator(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except basic_api.PdfError as error:
            raise DocumentError(error.ErrorMessage(error.GetError()))
    return decorator


def api(cls):

    class ErrorFree(cls):

        def __init__(self, *args, **kwargs):
            try:
                super(ErrorFree, self).__init__(*args, **kwargs)
            except basic_api.PdfError as error:
                raise DocumentError(error.ErrorMessage(error.GetError()))

        def __getattribute__(self, attr_name):
            obj = super(ErrorFree, self).__getattribute__(attr_name)
            if hasattr(obj, '__call__'):
                return error_parser(obj)
            return obj

    return ErrorFree


class DocumentError(Exception):
    pass
