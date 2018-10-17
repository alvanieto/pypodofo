# pypodofo

Python wrapper for C++ [podofo library](http://podofo.sourceforge.net/)

# Instructions

    #. Install podofo library. For example in archlinux, pacman -S podofo
    #. Install [swig tool](http://www.swig.org/). Note, you should have installed gcc and g++
       compilers
    #. Build wrapper. python setup.py build
    #. Copy dynamic library to python package. cp build/lib.linux-x86_64-3.7/_api.cpython-37m-x86_64-linux-gnu.so pypodofo/
    #. Install requirements. pip install -r requirements.txt (if possible in a virtualenv).
    #. Run tests. nosetests tests/


TODO: Improve install instructions. Currently they are complicated.
