from github import Github
from datetime import datetime
import json
import requests
import pygal

# using username and password
g = Github("cc2d7ccf0f53669bec8d83b1cbac2683d543b534")

#for repo in g.get_user().get_repos():
#    branch = repo.get_branch("master")
#    print(str(repo), "        ", str(branch.commit))


java_repos = g.search_repositories(query='language:Java')
count = 0
for repo in java_repos:
    if count < 10:
        print("JAVA", repo.stargazers_count, str(repo))
        count += 1
    else:
        break

print()

python_repos = g.search_repositories(query='language:python')
count = 0
for repo in python_repos:
    if count < 10:
        print("PYTHON", repo.stargazers_count, str(repo))
        count += 1
    else:
        break

barchart = pygal.Bar()
barchart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13])
barchart.render_to_file('barchart.svg')
