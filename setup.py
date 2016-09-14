#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

extra = {}

setup(
    name="dcm-spec-tools",
    packages=['dcm_spec_tools.spec_reader', 'dcm_spec_tools.validator'],
    include_package_data=True,
    version="0.0.2",
    install_requires=['pydicom'],
    description="Python DICOM tools using input from DICOM specs in docbook format",
    author="mrbean-bremen",
    author_email="hansemrbean@googlemail.com",
    url="http://github.com/mrbean-bremen/dcm_spec_tools",
    keywords="dicom python",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    long_description="""
    Toy project for getting information from the DICOM standard
    and using this information in command line tools.
    Aims to be usable with various versions of the DICOM standard.
    """,
    **extra
)
