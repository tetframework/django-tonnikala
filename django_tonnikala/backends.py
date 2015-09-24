from __future__ import absolute_import, unicode_literals

import sys

import tonnikala

from django.conf import settings
from django.template import TemplateDoesNotExist, TemplateSyntaxError
from django.utils import six

from django.template.backends.base import BaseEngine
from django.template.backends.utils import csrf_input_lazy, csrf_token_lazy


class Tonnikala(BaseEngine):

    app_dirname = 'tonnikala'

    def __init__(self, params):
        params = params.copy()
        options = params.pop('OPTIONS').copy()
        super(Tonnikala, self).__init__(params)

        debug = options.get('debug', settings.DEBUG)
        reload = options.get('reload', debug)
        syntax = options.get('syntax', 'tonnikala')

        self.loader = tonnikala.loader.FileLoader(
            paths=self.template_dirs,
            debug=debug,
            syntax=syntax,
        )
        self.loader.set_reload(reload)

    def from_string(self, template_code):
        return Template(self.loader.load_string(template_code))

    def get_template(self, template_name):
        try:
            return Template(self.loader.load(template_name))
        except tonnikala.runtime.exceptions.TemplateSyntaxError as exc:
            six.reraise(TemplateSyntaxError, TemplateSyntaxError(exc.args),
                        sys.exc_info()[2])
        except FileNotFoundError as exc:
            six.reraise(TemplateDoesNotExist, TemplateDoesNotExist(exc.args),
                        sys.exc_info()[2])


class Template(object):

    def __init__(self, template):
        self.template = template

    def render(self, context=None, request=None):
        if context is None:
            context = {}
        if request is not None:
            context['request'] = request
            context['csrf_input'] = csrf_input_lazy(request)
            context['csrf_token'] = csrf_token_lazy(request)
        return self.template.render(context)
