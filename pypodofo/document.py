# -*- coding: utf-8 -*-

import api
import field
import error


class Page(object):

    def __init__(self, page):
        self.__page = page
        self.__fields = Page._Fields(page)

    @property
    def fields(self):
        return self.__fields

    class _Fields(object):

        def __init__(self, page):
            self.__page = page
            self.__fields = self.__load_fields(page)

        def __len__(self):
            return self.__page.GetNumFields()

        def __getattr__(self, field_name):
            if field_name in self.__fields:
                return self.__fields[field_name]

            raise AttributeError(field_name)

        def __iter__(self):
            for field in self.__fields.values():
                yield field

        def __load_fields(self, page):
            res = {}
            for field_index in range(page.GetNumFields()):
                field_pdf = field.builder(page.GetField(field_index))
                res[field_pdf.name] = field_pdf
            return res


@error.ApiError
class Document(object):

    def __init__(self, pdf_name):
        self.__document = api.PdfMemDocument(pdf_name)
        self.__pdf_name = pdf_name
        self.__pages = None

    @property
    def pages(self):
        if not self.__pages:
            self.__pages = tuple(Page(self.__document.GetPage(page_index))
                                 for page_index in range(self.__document.GetPageCount()))

        return self.__pages

    def save(self, pdf_name=None):
        self.__document.Write(pdf_name if pdf_name else self.__pdf_name)

    def fill(self, values):
        # Only fill the first page
        if isinstance(values, dict):
            if not self.__document.GetPageCount():
                raise error.DocumentError('The document hat 0 pages')

            for field, value in values.iteritems():
                setattr(self.pages[0].fields, field, value)

    def dump_fields(self):
        pages = []
        for page in self.pages:
            res = {}
            for field in page.fields:
                res[field.name] = ''
            pages.append(res)
        return pages
