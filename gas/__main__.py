"""Manage Google Apps Script projects from the command line.

Mostly a work-alike for Google's own "clasp", only in Python.
"""

import sys
import typing

from mundane import app
from mundane import log_mgr

from gas import auth


def main() -> typing.NoReturn:
    """The GAS app."""
    log_mgr.set_root_log_level('INFO')
    gas_app = app.ArgparseApp(
        use_log_mgr=True, use_docstring_for_description=sys.modules[__name__]
    )
    modules = (auth,)
    gas_app.register_global_flags(modules)
    gas_app.register_shared_flags(modules)
    gas_app.register_commands(modules)

    sys.exit(gas_app.run())


if __name__ == '__main__':  # pragma: no cover
    main()
