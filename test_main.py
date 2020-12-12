import pytest
from main import create_folder, check_folder_exist


class TestMain:

    def test_success_create_folder(self):
        assert create_folder('Test12345').status_code == 201

    def test_failed_create_folder(self):
        assert create_folder('').status_code == 409

    def test_success_folder_present(self):
        assert check_folder_exist('Test12345').status_code == 200

    def test_failed_folder_present(self):
        assert check_folder_exist('dfksldkfklksdf').status_code == 404
