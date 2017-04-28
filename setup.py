import os
from setuptools import setup

import PyACO

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='PyACO',
    version=PyACO.__version__,
    author=PyACO.__author__,
    author_email='yajnab@gmail.com',
    description='Ant Colony Optimization (ACO) with constraint support',
    url='https://github.com/yajnab/PyACO',
    license='BSD License',
    long_description=read('README.rst'),
    packages=['PyACO'],
    install_requires=['numpy'],
    keywords=[
        'ACO',
        'Ant Colony Optimization',
        'optimization',
        'python'
        ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
        ]
    )
