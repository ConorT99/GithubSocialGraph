from github import Github
from datetime import datetime
import json
import requests
import pygal

# using username and password
g = Github("")

#for repo in g.get_user().get_repos():
#    branch = repo.get_branch("master")
#    print(str(repo), "        ", str(branch.commit))
java_stars = []
java_repo_names = []

# -- GATHERING 10 Most STARRED JAVA REPOS -- #
java_repos = g.search_repositories(query='language:Java')
count = 0
for repo in java_repos:
    if count < 10:
        #print("JAVA", repo.stargazers_count, str(repo))
        java_stars.insert(count, repo.stargazers_count)
        java_repo_names.insert(count, repo.name)
        count += 1
    else:
        break

# -- END GATHERING JAVA INFORMATION -- #

python_stars = []
python_repo_names = []

# -- GATHERING 10 MOST STARRED PYTHON REPOS -- #

python_repos = g.search_repositories(query='language:python')
count = 0
for repo in python_repos:
    if count < 10:
        #print("PYTHON", repo.stargazers_count, str(repo))
        python_stars.insert(count, repo.stargazers_count)
        python_repo_names.insert(count, repo.name)
        count += 1
    else:
        break

# -- END GATHERING PYTHON INFORMATION -- #

pystars_total = 0
for i in range(0, len(python_stars)):
    pystars_total += python_stars[i]
print("Python repo stars (in toto): " + str(pystars_total))

py_share_of_total = []
for i in range(0, len(python_stars)):
    py_share_of_total.insert(i, (python_stars[i]/pystars_total) * 100)

print(py_share_of_total)

java_bars = pygal.Bar()
for i in range(0, len(java_repo_names)):
    java_bars.add(java_repo_names[i], java_stars[i])
java_bars.render_to_file('javaBarchart.svg')

pypie = pygal.Pie()
for i in range(0, len(python_repo_names)):
    pypie.add(python_repo_names[i], py_share_of_total[i])
pypie.render_to_file('pyPie.svg')
