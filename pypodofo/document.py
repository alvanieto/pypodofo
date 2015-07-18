# -*- coding: utf-8 -*-

import api


class Field(object):

    def __init__(self, field):
        self.__field = field

    @property
    def value(self):
        raise NotImplemented

    @value.setter
    def value_setter(self):
        raise NotImplemented


class Page(object):

    def __init__(self, page):
        self.__page = page

    @property
    def fields(self):
        for field_index in range(self.__page.GetNumFields()):
            yield Field(self.__page.GetField(field_index))


class Document(object):

    def __init__(self, pdf_name):
        self.__document = api.PdfMemDocument(pdf_name)

    @property
    def pages(self):
        for page_index in range(self.__document.GetPageCount()):
            yield Page(self.__document.GetPage(page_index))
