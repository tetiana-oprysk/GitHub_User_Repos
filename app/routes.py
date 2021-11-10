from config import TOKEN
import os
from boto.s3.connection import S3Connection
from flask import render_template, redirect, url_for, request
from app import app
from app.forms import Form
from app.github_service import GitHubService


@app.route('/', methods=['GET', 'POST'])
def form():
    form = Form()
    if request.method == 'POST':
        t = S3Connection(os.environ['TOKEN'])
        github_login = request.form.get('github_login')
        github_token = f'token {t}'
        github_service = GitHubService(github_token, github_login)

        return redirect(url_for('list_of_repos', query=github_service.get_user_repos()))

    return render_template('form.html', form=form)


@app.route('/list')
def list_of_repos():
    query = eval(request.args.get('query', None))
    names = []
    if query['data']['user'] is None:
        return render_template('something_went_wrong.html')
    for name in query['data']['user']['repositories']['nodes']:
        names.append(name['name'])
    user = query['data']['user']['name']
    return render_template('list_of_user_repos.html', names=names, user=user)
