# pypodofo

Python wrapper for C++ [podofo library](http://podofo.sourceforge.net/)

# Instructions

    #. Install podofo library. For example in archlinux, pacman -S podofo
    #. Install [swig tool](http://www.swig.org/). Note, you should have installed gcc and g++
       compilers
    #. Build wrapper. python setup.py build
    #. Install requirements. pip install -r requirements.txt (if possible in a virtualenv).
    #. Run tests. nosetests tests/
