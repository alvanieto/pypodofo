# pypodofo

Python wrapper for C++ [podofo library](http://podofo.sourceforge.net/)

# Instructions

    1. Install podofo library. For example in archlinux, pacman -S podofo
    2. Install [swig tool](http://www.swig.org/). Note, you should have installed gcc and g++
       compilers
    3. Build wrapper. python setup.py build
    4. Copy dynamic library to python package. cp build/lib.linux-x86_64-3.7/_api.cpython-37m-x86_64-linux-gnu.so pypodofo/
    5. Install requirements. pip install -r requirements.txt (if possible in a virtualenv).
    6. Run tests. nosetests tests/


TODO: Improve install instructions. Currently they are complicated.
