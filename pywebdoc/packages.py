"""The *packages* module manages installed PyPI packages."""
import os
import logging

from tqdm import tqdm

from pywebdoc.error import PywebdocError
from pywebdoc.pip import call, get_installed_packages
from pywebdoc.template import Templates


class Package:
    """Manage an installed PyPI package."""
    def __init__(self, name):
        """
        Init a package. The packages needs to be installed.
        Raise PywebdocError if the package is not found.
        """
        self._name = name
        self._url = 'https://pypi.org/project/{}/'.format(name)
        self._version, self._summary, self._home_page, self._license = (
            None, None, None, None
        )
        lines = call('show', name)
        if lines == '':
            raise PywebdocError('Package %s not found' % name)
        for line in lines.split('\n'):
            if line.startswith('Version: '):
                self._version = line.split(': ', 1)[1]
            elif line.startswith('Summary: '):
                self._summary = line.split(': ', 1)[1]
            elif line.startswith('Home-page: '):
                self._home_page = line.split(': ', 1)[1]
            elif line.startswith('License: '):
                self._license = line.split(': ', 1)[1]

    @property
    def name(self):
        """Get name."""
        return self._name

    @property
    def url(self):
        """Get PyPI url."""
        return self._url

    @property
    def version(self):
        """Get version."""
        return self._version

    @property
    def summary(self):
        """Get summary."""
        return self._summary

    @property
    def home_page(self):
        """Get home-page."""
        return self._home_page

    def __str__(self):
        """Get string format."""
        return '\n'.join(
            ['{}: {}'.format(i, j) for i, j in zip(
                ['Name', 'Version', 'Summary', 'Home-page', 'License'],
                [self.name, self.version, self.summary,
                 self.home_page, self._license]
            )])

    @staticmethod
    def get_list():
        """Return the list of installed packages."""
        logging.info('Getting PyPI packages informations...')
        return [Package(name) for name in tqdm(
            get_installed_packages(), desc='Packages', leave=False)]

    @staticmethod
    def make_html_list(filename):
        """Make html file with packages list."""
        path = os.path.dirname(os.path.realpath(__file__))
        templates = Templates(path)
        t = templates.get_template('packages.html.jinja')
        packages = Package.get_list()
        with open(filename, 'w') as f:
            f.write(t.render(path=path, packages=packages))
        logging.info('File %s created' % filename)
