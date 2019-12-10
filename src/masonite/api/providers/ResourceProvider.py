"""A ResourceProvider Service Provider."""

from masonite.provider import ServiceProvider
from ..commands.ResourceCommand import ResourceCommand


class ResourceProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        # self.app.bind('ResourceCommand', ResourceCommand())
        self.commands(ResourceCommand())
        pass

    def boot(self):
        """Boots services required by the container."""
        pass
