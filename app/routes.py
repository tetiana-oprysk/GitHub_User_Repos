import os

import requests
from flask import render_template, redirect, url_for, request
from app import app
from app.forms import Form


def run_query(github_login):
    headers = {"Authorization": f"token {os.environ.get('GITHUB_API')}"}

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
    """ % (github_login)

    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


@app.route('/', methods=['GET', 'POST'])
def form():
    form = Form()
    if request.method == 'POST':
        github_login = request.form.get('github_login')
        query = run_query(github_login)
        return redirect(url_for('list_of_repos', query=query))
    return render_template('form.html', form=form)


@app.route('/list')
def list_of_repos():
    query = eval(request.args.get('query', None))
    names = []
    for name in query['data']['user']['repositories']['nodes']:
        names.append(name['name'])
    user = query['data']['user']['name']
    return render_template('list_of_user_repos.html', names=names, user=user)
