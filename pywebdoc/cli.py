"""
The **cli** module manages the command line interface of *pywebdoc*.
It uses *click*.
"""
import os
import logging
import webbrowser

import click

import pywebdoc
from pywebdoc.logger import logger_config
from pywebdoc.packages import Package
from pywebdoc.pip import get_url
from pywebdoc.url import UrlTemplate, open_url


lang_choices_py = ['en', 'es', 'fr', 'ja', 'ko', 'pt-br', 'zh-cn', 'zh-tw']
lang_choices_rtd = ['en', 'es', 'fr']


@click.group()
@click.version_option(pywebdoc.__version__)
@click.option('-v', '--verbose', is_flag=True, help='Give more output')
def cli(verbose):
    """Open Python packages url."""
    level = logging.DEBUG if verbose else logging.INFO
    logger_config(level)


@cli.command()
@click.option('-v', '--version', type=click.STRING, default=3,
              show_default=True, help='Python version')
@click.option('-l', '--lang', type=click.Choice(lang_choices_py,
              case_sensitive=False), default='en', show_default=True,
              help='Language')
def py(version, lang):
    """Open the Python official documentation."""
    template = (
        'https://docs.python.org/{lang}/{version}/',
        'https://docs.python.org/{version}/'
    )[lang == 'en']
    url = UrlTemplate(template)
    url.open_url(version=version, lang=lang)


@cli.command()
@click.argument('library')
@click.option('-v', '--version', type=click.STRING, default=3,
              show_default=True, help='Python version')
@click.option('-l', '--lang', type=click.Choice(lang_choices_py,
              case_sensitive=False), default='en', show_default=True,
              help='Language')
def std(library, version, lang):
    """Open the documentation page of a standard Python library."""
    template = (
        'https://docs.python.org/{lang}/{version}/library/{library}.html',
        'https://docs.python.org/{version}/library/{library}.html'
    )[lang == 'en']
    url = UrlTemplate(template)
    url.open_url(library=library, version=version, lang=lang)


@cli.command()
@click.argument('package')
def home(package):
    """
    Open the home-page of a PyPI package.

    The package must be installed.
    """
    url = get_url(package)
    if url != '':
        open_url(url)


@cli.command()
@click.argument('package')
@click.option('-v', '--version', type=click.STRING, default='latest',
              show_default=True, help='Release version')
def pypi(package, version):
    """Open the PyPI web page of a package."""
    template = (
        'https://pypi.org/project/{package}/{version}/',
        'https://pypi.org/project/{package}/'
    )[version == 'latest']
    url = UrlTemplate(template)
    url.open_url(package=package, version=version)


@cli.command()
@click.argument('package')
@click.option('-v', '--version', type=click.STRING, default='latest',
              show_default=True, help='RTD documentation version')
@click.option('-l', '--lang', type=click.Choice(lang_choices_rtd,
              case_sensitive=False), default='en', show_default=True,
              help='Language')
def rtd(package, version, lang):
    """Open the documentation page of a package on ReadTheDocs."""
    url = UrlTemplate('https://{package}.readthedocs.io/{lang}/{version}/')
    url.open_url(package=package, version=version, lang=lang)


@cli.command()
@click.option('-u', '--update', is_flag=True, help='Update HTML file')
def list_packages(update):
    """Make HTML file with the list of installed PyPI packages."""
    path = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(path, 'packages.html')
    if update or not os.path.exists(filename):
        msg = """The program needs to read informations about packages.
This operation may take several minutes.
Do you want to continue?"""
        if click.confirm(msg):
            Package.make_html_list(filename)
            webbrowser.open_new_tab(filename)
    else:
        webbrowser.open_new_tab(filename)


@cli.command()
@click.option('-v', '--version', type=click.STRING, default=3,
              show_default=True, help='Python version')
@click.option('-l', '--lang', type=click.Choice(lang_choices_py,
              case_sensitive=False), default='en', show_default=True,
              help='Language')
def list_std(version, lang):
    """List standard libraries documentation urls."""
    template = (
        'https://docs.python.org/{lang}/{version}/py-modindex.html',
        'https://docs.python.org/{version}/py-modindex.html'
    )[lang == 'en']
    url = UrlTemplate(template)
    url.open_url(version=version, lang=lang)
