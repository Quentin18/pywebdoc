"""The **template** module manages templates. It uses *jinja2*."""
from jinja2 import Environment, FileSystemLoader


class Templates:
    """Manage the templates."""
    def __init__(self, directory):
        """Init the templates environment."""
        file_loader = FileSystemLoader(directory)
        self._env = Environment(loader=file_loader)

    @property
    def env(self):
        """Get environment."""
        return self._env

    def get_template(self, filename):
        """Return a template."""
        return self.env.get_template(filename)
