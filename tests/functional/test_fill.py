# -*- coding: utf-8 -*-

import os

from nose.tools import eq_

from pypodofo.document import Document


class TestFill(object):

    @classmethod
    def setup_class(cls):
        # Mantener la referencia al documento
        cls.document = Document(os.path.join(os.path.dirname(__file__), 'form.pdf'))

    def test_dump_fields(self):
        eq_(self.document.dump_fields(),
            [{'field_check_com': '',
              'field_check_oss': '',
              'field_clear': '',
              'field_combo': '',
              'field_comment': '',
              'field_mail': '',
              'field_name': '',
              'field_send': ''},
             {'ButtonFieldName': '',
              'ComboFieldName': '',
              'ListBoxFieldName': '',
              'TextFieldName': ''}])

    def test_fill_one_page(self):
        self.document.fill({
            'field_name': 'value'
        })
