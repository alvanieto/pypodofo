# -*- coding: utf-8 -*-

import os
from nose.tools import eq_, assert_true

from pypodofo import pypodofo


class TestForm(object):

    @classmethod
    def setup_class(cls):
        path = os.path.dirname(__file__)
        cls.document = pypodofo.PdfMemDocument(os.path.join(path, 'form.pdf'))

    def test_page_count(self):
        eq_(self.document.GetPageCount(), 2)

    def test_get_page(self):
        assert_true(self.document.GetPage(0))

    def test_get_num_fields(self):
        eq_(self.document.GetPage(0).GetNumFields(), 8)

    def test_get_field(self):
        eq_(self.document.GetPage(0).GetField(0).GetFieldName(), 'field_name')
