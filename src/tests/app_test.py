import unittest
from unittest.mock import Mock, patch
from app import App

class TestApp(unittest.TestCase):
    def setUp(self):
        self.mock_ref_service = Mock()
        self.mock_io = Mock()
        self.app = App(self.mock_ref_service, self.mock_io)

    def test_add_book_command(self):
        self.mock_io.read.side_effect = ['a', 'b', 'Author Name', 'Book Title', '2023', 'Publisher Name', '', '']
        self.app.run()
        self.mock_ref_service.create_reference.assert_called_once_with(
            'book', ['Author Name', 'Book Title', '2023', 'Publisher Name', '']
        )
        self.mock_io.write.assert_any_call("Reference type book added")

if __name__ == '__main__':
    unittest.main()
