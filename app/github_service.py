import requests


class GitHubService:
    def __init__(self, github_token, github_login):
        self.github_token = github_token
        self.github_login = github_login

    def send_request(self, query):
        headers = {"Authorization": f"{self.github_token}"}
        response = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)

        return response

    def get_user_repos(self):
        query = """{
                  user(login: "%s"){
                  name
                  repositories(first: 50,) {
                      nodes {
                        name

                      }
                    }
                  }
                }
                """ % (self.github_login)
        result = self.send_request(query)

        if result.status_code == 200:
            return result.json()

        return None
