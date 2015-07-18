# -*- coding: utf-8 -*-

import os

from nose.tools import eq_, assert_true

from pypodofo.document import Document, Page


class TestDocument(object):

    @classmethod
    def setup_class(cls):
        cls.document = Document(os.path.join(os.path.dirname(__file__), 'form.pdf'))

    def test_num_pages(self):
        eq_(len(list(self.document.pages)), 2)

    def test_get_pages(self):
        for page in self.document.pages:
            assert_true(isinstance(page, Page))


class TestPage(object):

    @classmethod
    def setup_class(cls):
        # Mantener la referencia al documento
        cls.document = Document(os.path.join(os.path.dirname(__file__), 'form.pdf'))
        cls.page = cls.document.pages.next()

    def test_num_fields(self):
        eq_(len(list(self.page.fields)), 8)

