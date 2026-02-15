"""Functions for all things authentication related."""

from __future__ import annotations

import typing

from google_auth_oauthlib.flow import InstalledAppFlow

if typing.TYPE_CHECKING:  # pragma: no cover
    import argparse

    from mundane import app

Secret: typing.TypeAlias = dict[str, typing.Any]
Secrets: typing.TypeAlias = dict[str, Secret]

_SCOPES = [
    "https://www.googleapis.com/auth/script.projects",
]

_SECRETS_JSON = 'secrets.json'
_CREDENTIALS_JSON = 'credentials.json'


class Error(Exception):
    """Base module exception."""


def mundane_commands(ctx: app.ArgparseApp):
    """Parser registration API."""
    auth_cmds = ctx.new_subparser(
        ctx.register_command(_auth, name='auth', usage_only=True)
    )

    secrets_cmds = ctx.new_subparser(
        ctx.register_command(
            _secrets, name='secrets', usage_only=True, subparser=auth_cmds
        )
    )

    accounts_cmds = ctx.new_subparser(
        ctx.register_command(
            _accounts, name='accounts', usage_only=True, subparser=auth_cmds
        )
    )

    ctx.register_command(_accounts_list, name='list', subparser=accounts_cmds)
    ctx.register_command(
        _accounts_login, name='login', subparser=accounts_cmds
    )
    ctx.register_command(
        _accounts_logout, name='logout', subparser=accounts_cmds
    )

    ctx.register_command(_secrets_list, name='list', subparser=secrets_cmds)
    ctx.register_command(_secrets_add, name='add', subparser=secrets_cmds)
    ctx.register_command(_secrets_del, name='del', subparser=secrets_cmds)


def _auth(args: argparse.Namespace) -> int:
    """A family of commands for working with authentication."""
    raise Error('This function should never be called.')


def _accounts(args: argparse.Namespace) -> int:
    """A family of command for managing account credentials.

    Multiple accounts may be logged in system wide.

    Each GAS project will have a default account associated with it.
    """
    raise Error('This function should never be called.')


def _secrets(args: argparse.Namespace) -> int:
    """A family of commands for managing Google Cloud Platform secrets.

    Different GCP projects can be used for authentication.  If only a single
    one is registered, it will be always be used.  Otherwise, the specific
    project must be specified.

    To generate a secrets file:

    * Visit https://console.cloud.google.com/auth/clients

    * Select (or create) appropriate project.

    * Click [+ Create client] to create an OAuth client ID.

    * Set "Application type" to "Desktop app"

    * Click [Create] button.

    * Use to "Download JSON" feature to get the client secrets file.

    * Import it with `add` command.
    """
    raise Error('This function should never be called.')


def _secrets_list(args: argparse.Namespace) -> int:
    """List the GCP projects with registered secrets.

    The destination will be set to read-only by the user.  Future attempts
    will require manual deletion.
    """
    print(f'{args.name}: TBD')
    return 0


def _secrets_add(args: argparse.Namespace) -> int:
    """Register secrets for a GCP project.

    The destination will be set to read-only by the user.  Future attempts
    will require manual deletion.
    """
    print(f'{args.name}: TBD')
    return 0


def _secrets_del(args: argparse.Namespace) -> int:
    """Delete the registered secrets for a GCP project.

    The destination will be set to read-only by the user.  Future attempts
    will require manual deletion.
    """
    print(f'{args.name}: TBD')
    return 0


def _accounts_list(args: argparse.Namespace) -> int:
    """List accounts logged into Google Apps Script."""
    print(f'{args.name}: TBD')
    return 0


def _accounts_login(args: argparse.Namespace) -> int:
    """Log into Google Apps Script."""
    flow = InstalledAppFlow.from_client_secrets_file(args.creds, _SCOPES)
    token = flow.run_local_server(port=0)
    # Save the credentials for the next run.
    del token
    return 0


def _accounts_logout(args: argparse.Namespace) -> int:
    """Log out of Google Apps Script."""
    del args
    return 0


def _secrets_read() -> Secrets:
    """Read a collection of GCP secrets."""
    return {}


def _secrets_write(secrets: Secrets):
    """Write a collection of GCP secrets."""
    del secrets
