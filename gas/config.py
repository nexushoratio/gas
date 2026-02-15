"""Functions for managing application configuration."""

from __future__ import annotations

import pathlib
import typing

if typing.TYPE_CHECKING:  # pragma: no cover
    import argparse

    from mundane import app


class Error(Exception):
    """Base module exception."""


def mundane_global_flags(ctx: app.ArgparseApp):
    """Register global flags."""

    ctx.global_flags.add_argument(
        '--conf-dir',
        help='Configuration files directory (Default: %(default)s)',
        action='store',
        default=ctx.dirs.user_config_dir
    )

    ctx.register_after_parse_hook(_init)


def _init(args: argparse.Namespace):
    """Initialize the configuration directory."""
    pathlib.Path(args.conf_dir).mkdir(exist_ok=True)
