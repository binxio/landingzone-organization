from landingzone_organization import Organization, Profile

sso_profile_input = {
    "sso_start_url": "https://acme.awsapps.com/start",
    "sso_region": "eu-central-1",
    "sso_role_name": "my-global-read-only-role",
    "role_session_name": "John.Doe@acme.com",
}


def test_generate_profiles(monkeypatch, organization: Organization) -> None:
    mpa_profile = Profile(
        **sso_profile_input, account_id="000000000000", account_name="root-account"
    )
    profiles = organization.sso_profiles(**sso_profile_input)
    assert len(profiles) == 14
    assert mpa_profile in profiles


def test_profile_equal() -> None:
    assert Profile(
        **sso_profile_input, account_id="000000000000", account_name="root-account"
    ) == Profile(
        **sso_profile_input, account_id="000000000000", account_name="root-account"
    )


def test_profile_not_equal() -> None:
    profile1 = Profile(
        **sso_profile_input, account_id="000000000000", account_name="root-account"
    )
    profile2 = Profile(
        **sso_profile_input, account_id="111111111111", account_name="root-account"
    )
    assert profile1 != profile2

    profile1 = Profile(
        **sso_profile_input, account_id="000000000000", account_name="root-account"
    )
    profile2 = Profile(
        **sso_profile_input, account_id="000000000000", account_name="other-account"
    )
    assert profile1 != profile2


def test_profile_compare_hash() -> None:
    profile1 = hash(
        Profile(
            **sso_profile_input, account_id="000000000000", account_name="root-account"
        )
    )
    profile2 = hash(
        Profile(
            **sso_profile_input, account_id="000000000000", account_name="root-account"
        )
    )
    assert profile1 == profile2
