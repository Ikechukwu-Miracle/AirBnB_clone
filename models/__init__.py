#!/usr/bin/python3
"""Makes module directory into package"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
