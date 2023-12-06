import unittest
import tempfile
import os
from repositories.reference_repository import ReferenceRepository

class TestReferenceRepository(unittest.TestCase):

    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.close()
        self.repository = ReferenceRepository(self.test_file.name, 'test_bib_file_path')

    def tearDown(self):
        os.remove(self.test_file.name)

    def test_check_file(self):
        self.repository._check_file()
        self.assertTrue(os.path.exists(self.test_file.name))

    def test_get_list_empty_file(self):
        references = self.repository._get_list()
        self.assertEqual(len(references), 0)

    def test_create_and_find_all(self):
        reference_data = "KA23;book;Kalle;Kallen OhTu seikkailut;2023;Kallen Omakustanne"
        with open(self.test_file.name, 'w', encoding="utf-8") as file:
            file.write(reference_data)

        references = self.repository.find_all()
        self.assertEqual(len(references), 1)

        reference = references[0]
        self.assertEqual(reference.author, "Kalle")
        self.assertEqual(reference.name, "Kallen OhTu seikkailut")
