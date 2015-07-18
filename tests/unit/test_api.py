# -*- coding: utf-8 -*-

import os
from nose.tools import eq_, assert_true, assert_false

from pypodofo import api


class Pdf(object):

    @classmethod
    def setup_class(cls):
        path = os.path.dirname(__file__)
        # De momento tengo que mantener la referencia porque sino el objecto C++ PdfMemDocument se
        # borra automáticamente
        cls.document = api.PdfMemDocument(os.path.join(path, 'form.pdf'))


class TestForm(Pdf):

    def test_page_count(self):
        eq_(self.document.GetPageCount(), 2)

    def test_get_page(self):
        assert_true(self.document.GetPage(0))

    def test_get_num_fields(self):
        eq_(self.document.GetPage(0).GetNumFields(), 8)

    def test_get_field(self):
        eq_(self.document.GetPage(0).GetField(0).GetFieldName(), 'field_name')


class Field(Pdf):

    @classmethod
    def setup_class(cls):
        super(Field, cls).setup_class()
        page = cls.document.GetPage(0)
        cls.fields = [page.GetField(index) for index in range(page.GetNumFields())]


class TestField(Field):

    @classmethod
    def setup_class(cls):
        super(TestField, cls).setup_class()
        cls.field = api.PdfField(cls.fields[0])

    def test_get_page(self):
        eq_(self.field.GetPage().GetPageNumber(), 1)

    def test_get_set_field_name(self):
        self.field.SetFieldName('field_name')

        eq_(self.field.GetFieldName(), 'field_name')

    def test_get_type(self):
        eq_(self.field.GetType(), api.ePdfField_TextField)


class TestTextField(Field):

    @classmethod
    def setup_class(cls):
        super(TestTextField, cls).setup_class()
        cls.field = api.PdfTextField(cls.fields[0])

    def test_get_set_text_field(self):
        self.field.SetText('text_field')

        eq_(self.field.GetText(), u'text_field')

    def test_set_max_len(self):
        self.field.SetMaxLen(9)
        self.field.SetText('0123456789')

        eq_(self.field.GetText(), u'012345678')

    def test_get_max_len(self):
        eq_(self.field.GetMaxLen(), -1)


class ListField(Field):

    def test_set_get_selected_item(self):
        self.field.SetSelectedItem(1)

        eq_(self.field.GetSelectedItem(), 1)

    def test_insert_get_and_delete_item(self):
        self.field.InsertItem('list_item')

        index = self.field.GetItemCount() - 1
        eq_(self.field.GetItem(index), 'list_item')
        self.field.RemoveItem(index)


class TestListField(ListField):

    @classmethod
    def setup_class(cls):
        super(ListField, cls).setup_class()
        page = cls.document.GetPage(1)
        cls.field = api.PdfListField(page.GetField(3))

    def test_get_item_count(self):
        eq_(self.field.GetItemCount(), 3)


class TestComboBox(ListField):

    @classmethod
    def setup_class(cls):
        super(ListField, cls).setup_class()
        cls.field = api.PdfComboBox(cls.fields[2])

    def test_set_editable(self):
        self.field.SetEditable(True)
        assert_true(self.field.IsEditable())


class TestCheckBoxField(Field):

    @classmethod
    def setup_class(cls):
        super(TestCheckBoxField, cls).setup_class()
        cls.field = api.PdfCheckBox(cls.fields[3])

    def test_set_checked(self):
        self.field.SetChecked(True)
        assert_true(self.field.IsChecked())

    def test_not_checked(self):
        assert_false(self.field.IsChecked())


class TestPushButton(Field):

    @classmethod
    def setup_class(cls):
        super(TestPushButton, cls).setup_class()
        cls.field = api.PdfButton(cls.fields[6])

    def test_is_push_button(self):
        assert_true(self.field.IsPushButton())

    def test_set_get_caption(self):
        self.field.SetCaption('push_button')
        eq_(self.field.GetCaption(), u'push_button')
