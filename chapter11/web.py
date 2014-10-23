import os

import jinja2


templates_dir = os.path.join(os.path.dirname(__file__), 'templates')

loader = jinja2.FileSystemLoader(templates_dir)

env = jinja2.Environment(loader=loader)


def render(template_name, context):
    template = env.get_template(template_name)
    return template.render(context)
