# -*- coding: utf-8 -*-

import error
from pypodofo import api


class FieldError(Exception):

    pass


class Field(object):

    def __init__(self, field):
        self.__field = field

    @property
    def name(self):
        return self.__field.GetFieldName()

    @property
    def value(self):
        raise NotImplemented

    @value.setter
    def value(self, value):
        raise NotImplemented


@error.ApiError
class Text(Field):

    @property
    def value(self):
        return self.__field.GetText()

    @value.setter
    def value_setter(self, value):
        self.__field.SetText(value)


class List(Field):

    @property
    def value(self):
        return self.__field.GetSelectedItem()

    @value.setter
    def value_setter(self, value):
        self.__field.SetSelectedItem(value)


@error.ApiError
class Combo(List):

    pass


@error.ApiError
class Check(Field):

    @property
    def value(self):
        return self.__field.IsChecked()

    @value.setter
    def value_setter(self, value):
        self.__field.SetChecked(value)


@error.ApiError
class PushButton(Field):

    pass


__TYPES = {
    api.ePdfField_TextField: Text,
    api.ePdfField_ListBox: List,
    api.ePdfField_ComboBox: Combo,
    api.ePdfField_CheckBox: Check,
    api.ePdfField_PushButton: PushButton
}

def builder(field):
    type_ = field.GetType()
    if type_ not in __TYPES:
        raise FieldError("Field type: {} doesn't exists".format(type_))

    return __TYPES[type_](field)
