"""Tests for auth.py"""

# pylint: disable=protected-access

import unittest

from mundane import app

from gas import auth


class MundaneCommandsTest(unittest.TestCase):

    def test_basic(self):
        my_app = app.ArgparseApp()

        auth.mundane_commands(my_app)


class NeverCallTest(unittest.TestCase):

    def test_auth(self):
        with self.assertRaises(auth.Error):
            auth._auth(None)

    def test_accounts(self):
        with self.assertRaises(auth.Error):
            auth._accounts(None)

    def test_secrets(self):
        with self.assertRaises(auth.Error):
            auth._secrets(None)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
