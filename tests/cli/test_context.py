from json import JSONDecodeError
from unittest.mock import patch, mock_open

import botocore
import click
import pytest

from landingzone_organization import Organization
from landingzone_organization.cli import Context


def test_context_default(monkeypatch) -> None:
    monkeypatch.delenv("AWS_PROFILE", raising=False)

    with patch("click.echo") as mock_click:
        context = Context(False, None)
        context.debug("my message")
        mock_click.assert_called is False

    assert context.session.profile_name == "default"


def test_context_debug(monkeypatch) -> None:
    monkeypatch.delenv("AWS_PROFILE", raising=False)

    with patch("click.echo") as mock_click:
        context = Context(True, None)
        context.debug("my message")
        mock_click.assert_called_with("my message")

    assert context.session.profile_name == "default"


def test_context_info(monkeypatch) -> None:
    monkeypatch.delenv("AWS_PROFILE", raising=False)

    with patch("click.echo") as mock_click:
        context = Context(False, None)
        context.info("my message")
        mock_click.assert_called_with("my message")

    assert context.session.profile_name == "default"


def test_context_explicit_profile(monkeypatch) -> None:
    monkeypatch.delenv("AWS_PROFILE", raising=False)
    context = Context(False, "my-profile")

    try:
        context.session.profile_name
    except botocore.exceptions.ProfileNotFound as error:
        assert "The config profile (my-profile) could not be found" == str(error)


def test_context_implicit_profile(monkeypatch) -> None:
    monkeypatch.setenv("AWS_PROFILE", "my-profile")
    context = Context(False, None)

    try:
        context.session.profile_name
    except botocore.exceptions.ProfileNotFound as error:
        assert "The config profile (my-profile) could not be found" == str(error)


def test_context_read_config(organization: Organization) -> None:
    with patch(
        "landingzone_organization.cli.context.open",
        mock_open(read_data=organization.dump()),
    ):
        context = Context(False, None)
        assert organization == context.organization
        assert organization == context.organization


def test_context_read_config_file_not_found(organization: Organization) -> None:
    with patch("landingzone_organization.cli.context.open", mock_open()) as mocked_file:
        mocked_file.side_effect = FileNotFoundError()
        context = Context(False, None)

        with pytest.raises(click.Abort):
            context.organization


def test_context_read_config_invalid_file_format() -> None:
    with patch("landingzone_organization.cli.context.open", mock_open()) as mocked_file:
        mocked_file.side_effect = JSONDecodeError("", "", 1)
        context = Context(False, None)

        with pytest.raises(click.Abort):
            context.organization


def test_context_read_config_exception() -> None:
    with patch(
        "landingzone_organization.cli.context.open", mock_open(read_data="{}")
    ) as mocked_file:
        context = Context(False, None)

        with pytest.raises(click.Abort):
            context.organization
