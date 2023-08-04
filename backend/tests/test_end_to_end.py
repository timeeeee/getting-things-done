def test_list_items(test_client):
    data = test_client.get("/in-items/").json()
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


def test_get_item(test_client):
    data = test_client.get("/in-items/1").json()
    expected_keys = set(["id", "description", "created_at", "processed_at"])
    assert set(data.keys()) == expected_keys
    assert data["id"] == 1
    assert data["description"] == "this is an in item"
    assert data["processed_at"] is None


def test_create_item(test_client):
    description = "a new thing"
    response = test_client.post("/in-items/", json={"description": description})
    assert response.status_code == 201
    data = response.json()
    assert data["id"] is not None
    assert data["description"] == description
    assert data["created_at"] is not None
    assert data["processed_at"] is None

    # now get it with a following get
    item_id = data["id"]
    response = test_client.get(f"/in-items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["description"] == description


def test_delete_item(test_client):
    response = test_client.delete("/in-items/1")
    assert response.status_code == 204
    
    response = test_client.get("/in-items/1")
    assert response.status_code == 404
