# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class PostConfig(AppConfig):
    name = 'post'
    verbose_name = 'Blog Posts'

    def ready(self):
        pass
