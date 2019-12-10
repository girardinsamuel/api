"""New Resource Command."""
from masonite.view import View
from masonite.app import App
from masonite.helpers.filesystem import make_directory

from cleo import Command


class ResourceCommand(Command):
    """
    Creates an api resource

    resource
        {name : Name of the resource you would like to create}
        {--m|--model=User : Link your model with the resource}
    """

    def handle(self):
        resource = self.argument('name')
        model = self.option('model')
        view = View(App())

        if not make_directory('app/resources/{0}.py'.format(resource)):
            return self.error('{0} Resource Exists!'.format(resource))

        with open('app/resources/{0}.py'.format(resource), 'w+') as f:
            if view.exists('/masonite/api/snippets/scaffold/resource'):
                # TODO: allow to create resource without model
                template = '/masonite/api/snippets/scaffold/resource'
                f.write(
                    view.render(
                        template, {'class': resource,
                                   'model': model}).rendered_template
                )

        self.info('Resource Created Successfully!')
