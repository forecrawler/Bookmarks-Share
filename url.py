#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import bookmark
from tornado import web

router = [
    (r'/', bookmark.IndexHandler),
    (r'/index', bookmark.IndexHandler),
    (r'/api/v1/stories', bookmark.StoriesHandler),
    (r'/api/v1/stories/(.*)', bookmark.StoryHandler),
    ]
