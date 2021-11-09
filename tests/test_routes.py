from app import app
import http


def test_main_page_route():
    # Arrange
    client = app.test_client()

    # Act
    query = client.get('/')

    # Assert
    assert query.status_code == http.HTTPStatus.OK


def test_list_page_route_returns_status_code_500_without_user_data():
    # Arrange
    client = app.test_client()

    # Act
    query = client.get('/list')

    # Assert
    assert query.status_code == http.HTTPStatus.INTERNAL_SERVER_ERROR
