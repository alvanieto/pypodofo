# -*- coding: utf-8 -*-

from document import Document


class Form(object):

    def __init__(self, document):
        self._document = document

    def dump(self):
        ''' Dump document structure as dict

        :rtype: dict
        '''
        for page in self._document.pages():
            pass
