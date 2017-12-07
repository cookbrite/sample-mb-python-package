#!/usr/bin/env python
"""
A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages, Extension

# To use a consistent encoding
from codecs import open
import os
import re

# To build cython+numpy packages properly on osx, we need this here to get its
# includefile path for make_ext_modules().  Unfortunately, this also means
# that there is no automated way to install numpy and running `setup.py` will
# fail if you do not already have it installed.
import numpy


# Package configuration should all be defined here for easy access.
# Update these values as best fits your particular package.

name = 'mb_sample_package'

description = 'MetaBrite Sample Package.'

author = 'MetaBrite, Inc.'

author_email = 'metabrite@example.com'

url = 'https://github.com/cookbrite/mb_sample_package'

license = 'Proprietary License'

keywords = 'metabrite'

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: Other/Proprietary License',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
]

setup_requires = (
    # CHANGEME: By default, we assume you will want to eventually use cython and nummpy.
    # CHANGEME: If you don't need them, you can comment them out here, above, and in tox.ini
    'cython',
    'numpy',
)
install_requires = setup_requires + (
    # CHANGEME: Put your package's requirements here.  A requirements.txt file is not recommended.
    # 'mb_sample_package',
    # 'other_sample_package',
)

tests_require = install_requires + (
    'pytest', 'pytest-runner',
    'tox',
)

################################################
# Please try not to touch things below this line
################################################

here = os.path.abspath(os.path.dirname(__file__))
module_path = os.path.join(here, name.replace('-', '_'))

# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Load the version by reading the package directly, so we don't run into
# dependency loops by importing it into setup.py
version = None
with open(os.path.join(module_path, '__init__.py')) as file:
    for line in file:
        m = re.search(r'\b(?:__version__|VERSION)\b\s*=\s*(.+?\n)', line)
        if m:
            version = eval(m.group(1))
            break
assert version is not None, "Couldn't find version string."


def make_ext_modules():
    """
    Walk the module tree looking for cython files and return a list of Extensions() from them.
    See: http://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html
    """
    extensions = []
    if 'cython' in setup_requires:
        cur_dir = os.getcwd()
        (parent_dir, module_dir) = os.path.split(module_path)
        try:
            if parent_dir:
                os.chdir(parent_dir)
            for info in os.walk(module_dir):
                dir_path = info[0]
                # subdirs = info[1]
                pyx_files = [f for f in info[2] if f.endswith('.pyx')]
                pxd_files = [f for f in info[2] if f.endswith('.pxd')]
                for f in pyx_files:
                    sources = [os.path.join(dir_path, f)]
                    module = f[:-4]
                    pxd = module + '.pxd'
                    if pxd in pxd_files:
                        sources.append(os.path.join(dir_path, pxd))
                    if sources:
                        ext_name = '.'.join(dir_path.split(os.sep) + [module])
                        extensions.append(Extension(
                            ext_name, sources=sources,
                            include_dirs=[numpy.get_include()]
                        ))
        finally:
            os.chdir(cur_dir)
    return extensions


setup(
    name=name,
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    url=url,
    license=license,
    classifiers=classifiers,
    keywords=keywords,

    setup_requires=setup_requires,

    # Specify the specific modules that cython should compile
    ext_modules=make_ext_modules(),

    # This package only installs its base module, and a bunch of dependencies
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=install_requires,

    # In order to keep tox *and* setup happy, we need to define the test requirements twice...
    extras_require={
        'test': tests_require,
    },
    tests_require=tests_require,
    test_suite='py.test',
)
