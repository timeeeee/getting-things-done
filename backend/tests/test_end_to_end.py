from tests.conftest import client

# =====
# items
# =====

def test_list_items():
    data = client.get("/in-items/").json()
    assert len(data) == 2

    item1, item2 = data

    expected_keys = set(["id", "description", "created_at", "processed_at"])
    assert set(item1.keys()) == expected_keys
    assert set(item2.keys()) == expected_keys
    
    assert item1["id"] == 1
    assert item1["description"] == "this is an in item"
    assert item1["processed_at"] is None

    assert item2["id"] == 2
    assert item2["description"] == "this is another item"
    assert item2["processed_at"] is None


def test_get_item():
    data = client.get("/in-items/1").json()
    expected_keys = set(["id", "description", "created_at", "processed_at"])
    assert set(data.keys()) == expected_keys
    assert data["id"] == 1
    assert data["description"] == "this is an in item"
    assert data["processed_at"] is None


def test_create_item():
    description = "a new thing"
    response = client.post("/in-items/", json={"description": description})
    assert response.status_code == 201
    data = response.json()
    assert data["id"] is not None
    assert data["description"] == description
    assert data["created_at"] is not None
    assert data["processed_at"] is None

    # now get it with a following get
    item_id = data["id"]
    response = client.get(f"/in-items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["description"] == description


def test_update_item():
    raise NotImplementedError


def test_delete_item():
    response = client.delete("/in-items/1")
    assert response.status_code == 204
    
    response = client.get("/in-items/1")
    assert response.status_code == 404


# ========
# projects
# ========

def test_list_projects():
    data = client.get("/projects/").json()
    project1, project2, project3 = data

    expected_keys = [
        "id", "name", "notes", "bucket", "next_step", "created_at", "updated_at"
    ]
    
    assert set(project1.keys()) == set(expected_keys)
    assert set(project2.keys()) == set(expected_keys)
    assert set(project3.keys()) == set(expected_keys)
    
    assert project1["name"] == "Getting Things Done website"
    assert project1["notes"] == "fastapi back-end, react front-end"
    assert project1["bucket"] == "active"
    assert project1["next_step"] == "test"

    assert project2["name"] == "Apply for jobs"
    assert project2["notes"] is None
    assert project2["bucket"] == "active"
    assert project2["next_step"] == "sign up on tutoring website"

    assert project3["name"] == "The Contraption"
    assert project3["notes"] is None
    assert project3["bucket"] == "complete"
    assert project3["next_step"] is None


def test_get_project():
    data = client.get("/projects/1").json()
    expected_keys = [
        "id", "name", "notes", "bucket", "next_step", "created_at", "updated_at"
    ]

    assert set(data.keys()) == set(expected_keys)
    assert data["id"] == 1
    assert data["name"] == "Getting Things Done website"
    assert data["notes"] == "fastapi back-end, react front-end"
    assert data["bucket"] == "active"
    assert data["next_step"] == "test"
    assert data["created_at"] is not None
    assert data["updated_at"] is not None


def test_create_project():
    project = {
        "name": "build a still",
        "notes": "should I malt grain myself?",
        "bucket": "maybe",
        "next_step": "re-read the lore of still-building",
    }
    
    expected_keys = [
        "id", "name", "notes", "bucket", "next_step", "created_at", "updated_at"
    ]

    response = client.post("/projects/", json=project)
    assert response.status_code == 201
    data = response.json()
    assert set(data.keys()) == set(expected_keys)
    assert data["id"] is not None
    assert data["created_at"] is not None
    assert data["updated_at"] is not None
    assert data["name"] == project["name"]
    assert data["notes"] == project["notes"]
    assert data["bucket"] == "maybe"
    assert data["next_step"] == project["next_step"]

    # now get it with a following get
    project_id = data["id"]
    response = client.get(f"/projects/{project_id}")
    assert response.status_code == 200
    data = response.json()
    assert set(data.keys()) == set(expected_keys)
    assert data["id"] is not None
    assert data["created_at"] is not None
    assert data["updated_at"] is not None
    assert data["name"] == project["name"]
    assert data["notes"] == project["notes"]
    assert data["bucket"] == "maybe"
    assert data["next_step"] == project["next_step"]


def test_update_project():
    raise NotImplementedError


def test_delete_project():
    response = client.delete("/projects/1")
    assert response.status_code == 204
    
    response = client.get("/projects/1")
    assert response.status_code == 404
