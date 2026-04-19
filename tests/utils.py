import urllib.parse


def quote_activity_name(activity_name: str) -> str:
    return urllib.parse.quote(activity_name)


def activity_signup_url(activity_name: str) -> str:
    return f"/activities/{quote_activity_name(activity_name)}/signup"


def activity_remove_url(activity_name: str) -> str:
    return f"/activities/{quote_activity_name(activity_name)}/participants"


def signup(client, activity_name: str, email: str):
    return client.post(activity_signup_url(activity_name), params={"email": email})


def remove_participant(client, activity_name: str, email: str):
    return client.delete(activity_remove_url(activity_name), params={"email": email})
