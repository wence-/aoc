from distutils.core import setup
from distutils.extension import Extension

import numpy
from Cython.Build import build_ext
from setuptools import find_packages

setup(name="AOC",
      version="2019.1",
      cmdclass={"build_ext": build_ext},
      packages=find_packages("."),
      ext_modules=[Extension("intcode.cintcode",
                             sources=["intcode/cintcode.pyx"],
                             include_dirs=[numpy.get_include()])])
