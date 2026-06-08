def test_get_activities(client):
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_signup_and_unregister(client):
    activity = "Chess Club"
    email = "tester@example.com"

    # Sign up
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert resp.status_code == 200
    assert email in client.get("/activities").json()[activity]["participants"]

    # Duplicate signup should fail
    resp2 = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert resp2.status_code == 400

    # Unregister
    resp3 = client.delete(f"/activities/{activity}/participants", params={"email": email})
    assert resp3.status_code == 200
    assert email not in client.get("/activities").json()[activity]["participants"]


def test_activity_not_found(client):
    resp = client.post("/activities/Nonexistent/signup", params={"email": "a@b.com"})
    assert resp.status_code == 404
