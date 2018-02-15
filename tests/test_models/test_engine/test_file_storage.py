 #!/usr/bin/python3
'''
Module: File Storage Test
file_storage.py - FileStorageDocs tests
'''
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class test_file_storage(unittest.TestCase):
    ''' FileStorage Tests '''
    def set_up_base_model(self):
        ''' assign BaseModel '''
        self.basemodel = BaseModel()

    def set_up_file_storage(self):
        ''' assign FileStorage '''
        self.filestorage = FileStorage()

    def test_file_storage_instance(self):
        ''' test instance exists '''
        inst_1 = FileStorage()
        self.assertTrue(inst_1)

#    def test_all(self):
#        ''' test console method 'all' '''
#        inst_2 = self.filestorage.all()
#        self.assertIsInstance(type(inst_2), dict)

#    def test_new(self):
#        ''' test console method 'new' '''
#        inst_3 = BaseModel()
#        self.filestorage.new(inst_3)
#        inst_3_str = "{}.{}".format(inst_3.__class__.__name__, inst_3.id)
#        inst_3_dict = self.filestorage.all()
#        self.assertIn(inst_3_str, inst_3_dict)
