"""Tests for config.py"""

# pylint: disable=protected-access

import pathlib
import tempfile
import unittest

from mundane import app

from gas import config


class MundaneGlobalFlagsTest(unittest.TestCase):

    def test_basic(self):
        my_app = app.ArgparseApp()

        config.mundane_global_flags(my_app)
        flags = vars(my_app.parser.parse_args([]))

        self.assertIn('conf_dir', flags)


class InitTest(unittest.TestCase):

    def test_creates_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            conf_dir = pathlib.Path(tmpdir, self.id())
            my_app = app.ArgparseApp()
            config.mundane_global_flags(my_app)
            args = my_app.parser.parse_args(['--conf-dir', str(conf_dir)])

            self.assertFalse(conf_dir.exists())
            config._init(args)
            self.assertTrue(conf_dir.is_dir())

    def test_accepts_existing_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            conf_dir = pathlib.Path(tmpdir, self.id())
            my_app = app.ArgparseApp()
            config.mundane_global_flags(my_app)
            args = my_app.parser.parse_args(['--conf-dir', str(conf_dir)])

            self.assertFalse(conf_dir.exists())
            config._init(args)
            config._init(args)
            self.assertTrue(conf_dir.is_dir())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
