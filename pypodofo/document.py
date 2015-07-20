# -*- coding: utf-8 -*-

import api
import field
import error

@error.ApiError
class Page(object):

    def __init__(self, page):
        self.__page = page

    @property
    def fields(self):
        for field_index in range(self.__page.GetNumFields()):
            yield field.builder(self.__page.GetField(field_index))


@error.ApiError
class Document(object):

    def __init__(self, pdf_name):
        self.__document = api.PdfMemDocument(pdf_name)

    @property
    def pages(self):
        for page_index in range(self.__document.GetPageCount()):
            yield Page(self.__document.GetPage(page_index))

    def fill(self, values):
        # Only fill the first page
        if isinstance(values, dict):
            if not self.__document.GetPageCount():
                raise error.DocumentError('The document hat 0 pages')
            page = self.pages.next()
            fields = {field.name: field for field in page.fields}
            for field, value in values.iteritems():
                if field in fields:
                    fields[field].value = value
                else:
                    print('The field {} does not exists in the document'.format(field))

    def dump_fields(self):
        result = []
        for page in self.pages:
            result.append({field.name: '' for field in page.fields})
        return result
