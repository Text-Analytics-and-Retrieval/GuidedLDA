#!/usr/bin/env python
# Copyright (c) 2014 lda developers, Vikash Singh (vi3k6i5)
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file, You
# can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup, Extension
# from Cython.Build import cythonize

module1 = Extension('guidedlda._guidedlda',
                    sources = ['guidedlda/_guidedlda.c', 'guidedlda/gamma.c'])

setup(
    setup_requires=['pbr'],
    pbr=True,
    # ext_modules = cythonize("guidedlda/_guidedlda.pyx"
    ext_modules=[module1]

)
