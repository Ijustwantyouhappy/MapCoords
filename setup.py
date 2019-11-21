# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re


setup(
    name="MapCoords",
    version=re.findall('__version__\s*=\s*"(.*?)"', open("MapCoords/__init__.py", "r", encoding="utf-8").read())[0],
    author='Ijustwantyouhappy',
    author_email='',
    description="A Python library about map coordinates",
    long_description=open('README.rst').read(),  # todo write README seriously
    # long_description_content_type="text/markdown",
    url='',
    # maintainer='',
    # maintainer_email='',
    license='MIT',
    packages=find_packages(),
    # package_data={
    #     '': ['*.hdf5', '*.html', '*.ipynb', '*.jpg', '*.npz']
    # },
    include_package_data=True,
    zip_safe=False,
    # platforms=["all"],
    python_requires='>=3.5',
    install_requires=["numpy>=1.14.2", 
                      "scipy>=1.1.0", 
                      "pandas>=0.22.0", 
                      "matplotlib>=2.0.2", 
                      "h5py>=2.8.0", 
                      "requests>=2.14.2"],
    classifiers=[
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Windows',
        'Operating System :: MacOS',
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python :: 3',
    ],
    keywords='map coordinates'
)
