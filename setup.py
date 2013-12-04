# Copyright 2011-2012 OpenStack, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

setuptools.setup(
    name='quark_python_neutronclient_ext.py',
    version='0.01',
    description='Adds support for Quark extensions to python-neutronclient',
    long_description=open('README.rst').read(),
    author='Rackspace',
    author_email='matt.dietz@rackspace.com',
    url='https://github.com/rackspace/quark_python_neutronclient_ext',
    license='Apache License, Version 2.0',
    py_modules=['quark_python_neutronclient_ext'],
    install_requires=['python-neutronclient'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
