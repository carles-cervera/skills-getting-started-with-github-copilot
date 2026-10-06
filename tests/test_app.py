from fastapi.testclient import TestClient

from src.app import activities, app


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    activity_name = "Soccer Team"
    email = "student@example.edu"
    activities[activity_name]["participants"].append(email)

    response = client.delete(
        f"/activities/{activity_name}/participants/{email}"
    )

    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]


def test_unregister_participant_returns_not_found_for_missing_email():
    activity_name = "Soccer Team"
    email = "missing@example.edu"

    response = client.delete(
        f"/activities/{activity_name}/participants/{email}"
    )

    assert response.status_code == 404
