# App for finding all repositories on GitHub for a given GitHub_login

The application is built using the Flask framework. 

In the app/routes.py file in the 8th line, after the word "token" set your personal token instead of what is indicated in the code. You can generate it using the following link:
https://github.com/settings/tokens

After installing and launching the "app" application, you will see a page with a search engine, where you need to enter the user's GitHub_login. 

After that, you will get it's full name and a list of all its repositories.

### Example
```
Input: dhh

Output: 
David Heinemeier Hansson
- conductor
- asset-hosting-with-minimum-ssl
- remotelogger-server
- pasta
- credibles
- gemoji
- motion-settings-bundle
- sub
- tempusfugit
- ample-search
- code_metrics
- actionmailer-deliver_later
- activejob-stats
- stimulus
- textmate-rails-bundle
- rack-ratelimit
- tailwindcss-rails
- request.js
- requestjs-rails
```
