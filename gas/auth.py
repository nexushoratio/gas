"""Functions for all things authentication related."""

from __future__ import annotations

import pathlib
import pickle
import shutil
import typing

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    "https://www.googleapis.com/auth/script.projects",
]

if typing.TYPE_CHECKING:  # pragma: no cover
    import argparse

    from mundane import app


class Error(Exception):
    """Base module exception."""


CREDS_BASENAME = 'credentials.json'
TOKEN_BASENAME = '.token.pickle'


def mundane_commands(ctx: app.ArgparseApp):
    """Parser registration API."""
    default_creds_filename = pathlib.Path(
        ctx.dirs.user_config_path, CREDS_BASENAME
    )
    creds_flags = ctx.new_parser()
    creds_flags_req = ctx.new_parser()

    creds_flags.add_argument(
        '--creds',
        action='store',
        default=default_creds_filename,
        help='Google Cloud secrets file.  (Default: %(default)s)',
    )

    creds_flags_req.add_argument(
        '--creds',
        action='store',
        required=True,
        help='Source of the Google Cloud secrets file.',
    )

    creds_flags_req.add_argument(
        '--dest',
        action='store',
        default=default_creds_filename,
        help=(
            'Destination for the Google Cloud secrets'
            'file.  (Default: %(default)s)'
        ),
    )

    auth_cmds = ctx.new_subparser(
        ctx.register_command(_auth, name='auth', usage_only=True)
    )

    ctx.register_command(
        creds, subparser=auth_cmds, parents=[creds_flags_req]
    )
    ctx.register_command(login, subparser=auth_cmds, parents=[creds_flags])
    ctx.register_command(logout, subparser=auth_cmds)


def _auth(args: argparse.Namespace) -> int:
    """A family of commands for working with authentication."""
    raise Error('This function should never be called.')


def creds(args: argparse.Namespace) -> int:
    """Import the appropriate credentials file.

    The destination will be set to read-only by the user.  Future attempts
    will require manual deletion.
    """
    dest = pathlib.Path(args.dest)
    dest.parent.mkdir(exist_ok=True)
    shutil.copyfile(args.creds, args.dest)
    dest.chmod(0o400)
    return 0


def login(args: argparse.Namespace) -> int:
    """Log into Google Apps Script."""
    flow = InstalledAppFlow.from_client_secrets_file(args.creds, SCOPES)
    token = flow.run_local_server(port=0)
    # Save the credentials for the next run.
    # Older version of Credentials on Debian/bookworm does not have .to_json()
    with open(TOKEN_BASENAME, "wb") as token_fh:
        pickle.dump(token, token_fh)
    return 0


def logout(args: argparse.Namespace) -> int:
    """Log out of Google Apps Script."""
    del args
    pathlib.Path(TOKEN_BASENAME).unlink(missing_ok=True)
    return 0
