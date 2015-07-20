# -*- coding: utf-8 -*-

import api


class ApiError(object):

    def __init__(self, function):
        self.__function = function

    def __call__(self, *args, **kwargs):
        try:
            return self.__function(*args, **kwargs)
        except api.PdfError as error:
            raise DocumentError(error.ErrorMessage(error.GetError()))


class DocumentError(Exception):

    pass
