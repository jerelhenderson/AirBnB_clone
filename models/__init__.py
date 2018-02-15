#!/usr/bin/python3
''' initialize models package '''
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


available_models = {'BaseModel': BaseModel}
storage = FileStorage()
storage.reload()
