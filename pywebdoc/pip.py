"""
The **pip** module can call the ``pip`` command to get informations
about installed PyPI packages.
"""
import os
import sys
import logging
import subprocess


def call(*args):
    """Call pip command and get result."""
    python_location = os.environ.get(
        'PIPAPI_PYTHON_LOCATION', sys.executable
    )
    try:
        result = subprocess.check_output(
            [python_location, '-m', 'pip'] + list(args)
        )
    except subprocess.CalledProcessError:
        return ''
    return result.decode()


def get_installed_packages():
    """Return the list of installed packages."""
    lines = call('list').split('\n')
    return [line.split()[0] for line in lines[2:-1]]


def get_url(package):
    """
    Get the home-page url of a PyPI package.
    The package must be installed.
    """
    info = call('show', package)
    if info != '':
        for line in info.split('\n'):
            if line.startswith('Home-page: '):
                return line.split(': ', 1)[1]
    logging.error('Package %s not found' % package)
    return ''
