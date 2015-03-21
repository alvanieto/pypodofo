# -*- coding: utf-8 -*-

from contexlib import contextmanager

from pypodofo import pypodofo


class Field(object):

    def __init__(self, field):
        self.__field = field


class Page(object):

    def __init__(self, page):
        self.__page = page

    @contextmanager
    def fields(self):
        for field_index in range(self.__page.GetNumFields()):
            yield self.__page.GetField(field_index)


class Document(object):

    def __init__(self, pdf_name):
        self.__document = pypodofo.PdfMemDocument(pdf_name)

    @contextmanager
    def pages(self):
        for page_index in range(self.__document.GetPageCount()):
            yield Page(self.__document.GetPage(page_index))
