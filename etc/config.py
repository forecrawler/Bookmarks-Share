#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pymongo import MongoClient

ROOT = os.getcwd()

settings = {
        'template_path': os.path.join(ROOT, "templates"),
        'static_path': os.path.join(ROOT, "static"),
        "debug": True,
        "autoreload": True
        }

MONGODB_DB_URL = 'mongodb://localhost:27017'
MONGODB_DB_NAME = 'bookmarks'

client = MongoClient(MONGODB_DB_URL)
db = client[MONGODB_DB_NAME]
