# pypodofo

Python wrapper for C++ [podofo library](http://podofo.sourceforge.net/)

# Instructions

    1. Install podofo library. For example in archlinux, pacman -S podofo
    1. Install [swig tool](http://www.swig.org/). Note, you should have installed gcc and g++
       compilers
    1. Build wrapper. python setup.py build
    1. Copy dynamic library to python package. cp build/lib.linux-x86_64-3.7/_api.cpython-37m-x86_64-linux-gnu.so pypodofo/
    1. Install requirements. pip install -r requirements.txt (if possible in a virtualenv).
    1. Run tests. nosetests tests/


TODO: Improve install instructions. Currently they are complicated.
