from config import TOKEN
from app.github_service import GitHubService
import http

service = GitHubService(TOKEN, 'tetiana-oprysk')


def test_github_service_send_request_returns_status_code_ok():
    # Arrange
    query = '''{
                  user(login: "tetiana-oprysk"){
                  name
                  repositories(first: 50,) {
                      nodes {
                        name

                      }
                    }
                  }
                }
                '''

    # Act
    result = service.send_request(query)

    # Assert
    assert result is not None
    assert result.status_code == http.HTTPStatus.OK


def test_github_service_send_request_returns_status_code_unauthorized_if_token_invalid():
    # Arrange
    temp_service = GitHubService('bad_token', 'tetiana-oprysk')
    query = '''{
                  user(login: "tetiana-oprysk"){
                  name
                  repositories(first: 50,) {
                      nodes {
                        name

                      }
                    }
                  }
                }
                '''

    # Act
    result = temp_service.send_request(query)

    # Assert
    assert result.status_code == http.HTTPStatus.UNAUTHORIZED


def test_github_service_send_request_returns_none_if_wrong_login():
    # Arrange
    temp_service = GitHubService(TOKEN, 'tetiana_oprysk')
    query = '''{
                  user(login: "tetiana_oprysk"){
                  name
                  repositories(first: 50,) {
                      nodes {
                        name

                      }
                    }
                  }
                }
                '''

    # Act
    result = temp_service.get_user_repos()

    # Assert
    assert result['data']['user'] is None
