# -*- coding: utf-8 -*-

import os

from nose.tools import eq_, assert_true, raises

from pypodofo.document import Document
from pypodofo.error import DocumentError


class TestDocument(object):

    @classmethod
    def setup_class(cls):
        cls.document = Document(os.path.join(os.path.dirname(__file__), 'form.pdf'))

    @raises(DocumentError)
    def test_document_not_exists(self):
        Document('foo.bar')

    def test_num_pages(self):
        eq_(len(self.document.pages), 2)

    def test_get_pages(self):
        for page in self.document.pages:
            assert_true(page)


class TestPage(object):

    @classmethod
    def setup_class(cls):
        # Mantener la referencia al documento
        cls.document = Document(os.path.join(os.path.dirname(__file__), 'form.pdf'))
        cls.page = cls.document.pages[0]

    def test_num_fields(self):
        eq_(len(self.page.fields), 8)
