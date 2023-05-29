from unittest import mock

from fastapi import status

from tests import client


def test_get_product_page():
    response = client.get("tools/product")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_get_category():
    response = client.get("tools/category")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


# Test case for /tools/product route
@mock.patch(
    "external_api.openai_api.TextHelper.get_product_search_queries",
    return_value="test1",
)
@mock.patch(
    "external_api.openai_api.TextHelper.get_product_description", return_value="test2"
)
def test_get_product_page(
    mock_get_product_search_queries, mock_get_product_description
):
    response = client.post("/tools/product", json={"input": "test input"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"tags": "test1", "description": "test2"}


@mock.patch(
    "external_api.openai_api.TextHelper.get_category_search_queries",
    return_value="test3",
)
@mock.patch(
    "external_api.openai_api.TextHelper.get_category_description", return_value="test4"
)
def test_get_category_page(
    mock_get_category_search_queries, mock_get_category_description
):
    response = client.post("/tools/category", json={"input": "test input"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"tags": "test3", "description": "test4"}
