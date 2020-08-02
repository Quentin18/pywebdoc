"""
The **url** module manages the URLS.
The URLS are ckecked with *requests*.
"""
import logging
import webbrowser

import requests


def check_url(url, log=True):
    """Return True if no 404 error on url, else False."""
    try:
        r = requests.get(url)
    except requests.exceptions.SSLError:
        logging.error('No internet access')
        return False
    if r.status_code != 404:
        if log:
            logging.info('URL Found: {url}'.format(url=url))
        return True
    if log:
        logging.error('404 Not Found: %s' % url)
    return False


def open_url(url):
    """Open url if no 404 error is catched."""
    if check_url(url):
        webbrowser.open_new_tab(url)


class UrlTemplate:
    """Manage an url template."""
    def __init__(self, template):
        """Init an url template."""
        self._template = template

    @property
    def template(self):
        """Get url template."""
        return self._template

    def render(self, **kwargs):
        """Render url template."""
        return self.template.format(**kwargs)

    def open_url(self, **kwargs):
        """Render the url template and open it."""
        open_url(self.render(**kwargs))
