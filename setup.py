# -*- coding: utf-8 -*-

from setuptools import setup, Extension

setup(
    name='pypodofo',
    version='0.0.1',
    author='Álvaro Nieto',
    author_email='alvaro.nieto@gmail.com',
    license='LGPL',
    ext_modules=[Extension('_pypodofo', ['pypodofo/pypodofo.i'],
                           swig_opts=['-c++', '-I/usr/include/podofo'],
                           include_dirs=['/usr/include/podofo'])],
    py_modules=['pypodofo']
)
