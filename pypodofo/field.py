from . import error, api


class FieldError(Exception):
    pass


class Field:

    def __init__(self, field):
        self._field = field

    @property
    def name(self):
        return self._field.GetFieldName()

    @property
    def value(self):
        raise NotImplementedError

    @value.setter
    def value(self, value):
        raise NotImplementedError


@error.api
class Text(Field):

    def __init__(self, field):
        self._field = api.PdfTextField(field)

    @property
    def value(self):
        return self._field.GetText()

    @value.setter
    def value(self, value):
        self._field.SetText(value)


class List(Field):

    @property
    def value(self):
        return self._field.GetSelectedItem()

    @value.setter
    def value(self, value):
        self._field.SetSelectedItem(value)


@error.api
class Combo(List):

    def __init__(self, field):
        self._field = api.PdfComboBox(field)


@error.api
class Check(Field):

    def __init__(self, field):
        self._field = api.PdfCheckBox(field)

    @property
    def value(self):
        return self._field.IsChecked()

    @value.setter
    def value(self, value):
        self._field.SetChecked(value)


@error.api
class PushButton(Field):

    def __init__(self, field):
        self._field = field  # api.PdfPushButton(field)


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
