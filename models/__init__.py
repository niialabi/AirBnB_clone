#!/usr/bin/env python3
"""
create the variable storage, an instance of FileStorage
"""


from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()