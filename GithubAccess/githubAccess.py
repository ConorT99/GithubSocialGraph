from github import Github
from datetime import datetime
import json
import requests

# using username and password
g = Github("2b5aca630caa6f0de36cd40f318a4c404845e307")

for repo in g.get_user().get_repos():
    branch = repo.get_branch("master")
    print(str(repo), "        ", str(branch.commit))


#public_repos = requests.get('https://api.github.com/repositories').json()
#for repo in public_repos:
#    repo_name = repo['name']
#    owner = repo['owner']['login']
#    repo_info = requests.get('https://api.github.com/repos/'+owner+'/'+repo_name)
#    stars = repo_info.json()['stargazers_count']
#    print(repo_name, stars)


java_repos = g.search_repositories(query='language:Java')
count = 0
for repo in java_repos:
    if count < 10:
        print(repo.stargazers_count)
        count += 1
