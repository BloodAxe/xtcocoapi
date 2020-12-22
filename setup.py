from setuptools import setup, Extension
import numpy as np

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

ext_modules = [
    Extension(
        'xtcocotools._mask',
        sources=['./common/maskApi.c', 'xtcocotools/_mask.pyx'],
        include_dirs = [np.get_include(), './common'],
        extra_compile_args=['-std=c99'],
    )
]

setup(
    name='xtcocotools',
    packages=['xtcocotools'],
    package_dir = {'xtcocotools': 'xtcocotools'},
    install_requires=[
        'setuptools>=18.0',
        'cython>=0.27.3',
        'matplotlib>=2.1.0'
    ],
    version='1.6',
    description="Extended COCO API",
    url="https://github.com/jin-s13/xtcocoapi",
    ext_modules= ext_modules
)
