# -*- coding: utf-8 -*-

import os

from nose.tools import eq_, assert_true, raises

from pypodofo.document import Document
from pypodofo.error import DocumentError


class TestFill(object):

    @classmethod
    def setup_class(cls):
        # Mantener la referencia al documento
        cls.document = Document(os.path.join(os.path.dirname(__file__), 'form.pdf'))

    def test_dump_fields(self):
        result = {
            'field_check_com': '',
            'field_check_oss': '',
            'field_clear': '',
            'field_combo': '',
            'field_comment': '',
            'field_mail': '',
            'field_name': '',
            'field_send': '',
            'ButtonFieldName': '',
            'ComboFieldName': '',
            'ListBoxFieldName': '',
            'TextFieldName': ''
        }
        for page in self.document.dump_fields():
            for key, value in page.items():
                assert_true(key in result)

    def test_fill_one_page(self):
        self.document.fill({
            'field_name': 'value'
        })
        eq_(self.document.pages[0].fields.field_name, 'value')
