#!/usr/bin/env python3
"""Defines unittests for BaseModel Class"""

import unittest
import models
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """unittests for testing the BaseModel Class."""

    def test_new_instance(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id(self):
        selt.assertEqual(str, type(BaseModel().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))
