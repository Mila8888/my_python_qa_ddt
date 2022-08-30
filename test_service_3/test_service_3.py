import pytest

POST_MAX = 100
PHOTOS_MAX = 5000


@pytest.mark.parametrize("post_id", [1, POST_MAX])
def test_check_id(base_url, session, post_id):
    response = session.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id


@pytest.mark.parametrize("post_id", [-1, 0, "phy", POST_MAX + 1])
def test_negative_check(base_url, session, post_id):
    resp = session.get(f"{base_url}/posts/{post_id}")
    assert resp.status_code == 404
    assert resp.json() == {}


def test_check_lengt_lest(base_url, session):
    res = session.get(f"{base_url}/posts")
    assert len(res.json()) == 100


def test_photos_lengt(base_url, session):
    resp_check = session.get(f"{base_url}/photos")
    assert resp_check.status_code == 200
    assert len(resp_check.json()) == 5000


def test_create(session, base_url):
    payload = {"title": "footer", "body": "nsus", "userId": 1}
    response = session.post(f"{base_url}/posts", json=payload)

    assert response.status_code == 201
    json_resp = response.json()
    assert json_resp["id"] == POST_MAX + 1
    assert json_resp["userId"] == payload["userId"]
    assert json_resp["title"] == payload["title"]
    assert json_resp["body"] == payload["body"]


def test_delete(session, base_url):
    response = session.delete(f"{base_url}/posts/1")
    assert response.status_code == 200
    assert len(response.json()) == 0
