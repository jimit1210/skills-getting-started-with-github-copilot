from app import activities
from tests.utils import signup, remove_participant


def test_get_activities_returns_activities(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert expected_activity in payload
    assert isinstance(payload[expected_activity]["participants"], list)


def test_signup_adds_participant(client):
    # Arrange
    activity_name = "Chess Club"
    student_email = "newstudent@mergington.edu"

    # Act
    response = signup(client, activity_name, student_email)

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {student_email} for {activity_name}"
    assert student_email in activities[activity_name]["participants"]


def test_signup_duplicate_returns_400(client):
    # Arrange
    activity_name = "Chess Club"
    existing_email = activities[activity_name]["participants"][0]
    before_count = len(activities[activity_name]["participants"])

    # Act
    response = signup(client, activity_name, existing_email)

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]
    assert len(activities[activity_name]["participants"]) == before_count


def test_signup_for_missing_activity_returns_404(client):
    # Arrange
    activity_name = "Nonexistent Activity"
    student_email = "someone@mergington.edu"

    # Act
    response = signup(client, activity_name, student_email)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_remove_participant_success(client):
    # Arrange
    activity_name = "Chess Club"
    participant_email = activities[activity_name]["participants"][0]

    # Act
    response = remove_participant(client, activity_name, participant_email)

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {participant_email} from {activity_name}"
    assert participant_email not in activities[activity_name]["participants"]


def test_remove_missing_participant_returns_404(client):
    # Arrange
    activity_name = "Chess Club"
    missing_email = "missing@mergington.edu"

    # Act
    response = remove_participant(client, activity_name, missing_email)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"


def test_remove_from_missing_activity_returns_404(client):
    # Arrange
    activity_name = "Nonexistent Activity"
    student_email = "someone@mergington.edu"

    # Act
    response = remove_participant(client, activity_name, student_email)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
