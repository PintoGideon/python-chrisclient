
import unittest

from chrisclient.client import Client


class ClientTests(unittest.TestCase):

    def setUp(self):
        self.chris_url = "http://localhost:8000/api/v1/"
        self.username = "cube"
        self.password = "cube1234"
        self.client = Client(self.chris_url, self.username, self.password)

    def test_get_plugin(self):
        """
        Test whether get_plugin method can get a plugin representation from ChRIS.
        """
        pass

