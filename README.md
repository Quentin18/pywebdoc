# pywebdoc
[![Documentation Status](https://readthedocs.org/projects/pywebdoc/badge/?version=latest)](https://pywebdoc.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/Quentin18/pywebdoc.svg?branch=master)](https://travis-ci.org/Quentin18/pywebdoc)
![PyPI](https://img.shields.io/pypi/v/pywebdoc)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pywebdoc)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**pywebdoc** is a CLI application to quickly open web documentation about Python. This tool works for standard libraries and PyPI packages. It opens web pages on your default web browser.

![Demo](https://github.com/Quentin18/pywebdoc/blob/master/docs/source/img/demo.gif)

## Installing
*pywebdoc* can be installed using [pip](https://pip.pypa.io/en/stable/):
```bash
pip3 install pywebdoc
```

## Usage
You can see below the list of all commands you can use with *pywebdoc*. For more details, you can read the complete documentation [here](https://pywebdoc.readthedocs.io/en/latest/). 

* **Open the Python official documentation**:
```bash
pywebdoc py [OPTIONS]
```
* **Open the documentation page of a standard Python library**:
```bash
pywebdoc std [OPTIONS] LIBRARY
```
* **Open the PyPI web page of a package**:
```bash
pywebdoc pypi [OPTIONS] PACKAGE
```
* **Open the home-page of an installed PyPI package**:
```bash
pywebdoc home [OPTIONS] PACKAGE
```
* **Open the documentation page of a package on [ReadTheDocs](https://readthedocs.org)**:
```bash
pywebdoc rtd [OPTIONS] PACKAGE
```
* **Get the list of standard Python libraries**:
```bash
pywebdoc list-std [OPTIONS]
```
* **Get the list of installed PyPI packages**
```bash
pywebdoc list-packages [OPTIONS]
```

## Links
- GitHub: https://github.com/Quentin18/pywebdoc/
- PyPI: https://pypi.org/project/pywebdoc/
- Documentation: https://pywebdoc.readthedocs.io/en/latest/
- Travis: https://travis-ci.org/github/Quentin18/pywebdoc/

## Author
Quentin Deschamps: quentindeschamps18@gmail.com

## License
[MIT](https://choosealicense.com/licenses/mit/)