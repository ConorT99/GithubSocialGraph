from github import Github
from datetime import datetime
import json
import requests
import pygal

# using an access token to authenticate with GitHub
g = Github("")

#for repo in g.get_user().get_repos():
#    branch = repo.get_branch("master")
#    print(str(repo), "        ", str(branch.commit))
java_stars = []
java_repo_names = []

# -- GATHERING 10 MOST STARRED JAVA REPOS -- #
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

haskell_stars = []
haskell_repo_names = []

# -- GATHERING 10 MOST STARRED HASKELL REPOS -- #

haskell_repos = g.search_repositories(query='language:haskell')
count = 0
for repo in haskell_repos:
    if count < 10:
        #print("HASKELL", repo.stargazers_count, str(repo))
        haskell_stars.insert(count, repo.stargazers_count)
        haskell_repo_names.insert(count, repo.name)
        count += 1
    else:
        break

# -- END GATHERING HASKELL INFORMATION

prolog_stars = []
prolog_repo_names = []

# -- GATHERING 10 MOST STARRED PROLOG REPOS -- #

prolog_repos = g.search_repositories(query='language:prolog')
count = 0
for repo in prolog_repos:
    if count < 10:
        #print("PROLOG", repo.stargazers_count, str(repo))
        prolog_stars.insert(count, repo.stargazers_count)
        prolog_repo_names.insert(count, repo.name)
        count += 1
    else:
        break

# -- END GATHERING PROLOG INFORMATION -- #


bf_stars = []
bf_repo_names = []

# -- GATHERING 10 MOST STARRED BRAINFUCK REPOS -- #

bf_repos = g.search_repositories(query='language:brainfuck')
count = 0
for repo in bf_repos:
    if count < 10:
        #print("BRAINFUCK", repo.stargazers_count, str(repo))
        bf_stars.insert(count, repo.stargazers_count)
        bf_repo_names.insert(count, repo.name)
        count += 1
    else:
        break

# -- END GATHERING BRAINFUCK INFORMATION -- #

cobol_stars = []
cobol_repo_names = []

# -- GATHERING 10 MOST STARRED COBOL REPOS -- #

cobol_repos = g.search_repositories(query='language:cobol')
count = 0
for repo in cobol_repos:
    if count < 10:
        #print("COBOL", repo.stargazers_count, str(repo))
        cobol_stars.insert(count, repo.stargazers_count)
        cobol_repo_names.insert(count, repo.name)
        count += 1
    else:
        break

# -- END GATHERING COBOL INFORMATION -- #

html_stars = []
html_repo_names = []

# -- GATHERING 10 MOST STARRED HTML REPOS -- #

html_repos = g.search_repositories(query='language:html')
count = 0
for repo in html_repos:
    if count < 10:
        #print("HTML", repo.stargazers_count, str(repo))
        html_stars.insert(count, repo.stargazers_count)
        html_repo_names.insert(count, repo.name)
        count += 1
    else:
        break

# -- END GATHERING HTML INFORMATION -- #

css_stars = []
css_repo_names = []

# -- GATHERING 10 MOST STARRED CSS REPOS -- #

css_repos = g.search_repositories(query='language:css')
count = 0
for repo in css_repos:
    if count < 10:
        #print("CSS", repo.stargazers_count, str(repo))
        css_stars.insert(count, repo.stargazers_count)
        css_stars.insert(count, repo.name)
        count += 1
    else:
        break

# - END GATHERING CSS INFROMATION -- #

js_stars = []
js_repo_names = []

# -- GATHERING 10 MOST STARRED JS REPOS -- #

js_repos = g.search_repositories(query='language:javascript')
count = 0
for repo in js_repos:
    if count < 10:
        print("JAVASCRIPT", repo.stargazers_count, str(repo))
        js_stars.insert(count, repo.stargazers_count)
        js_repo_names.insert(count, repo.name)
        count += 1
    else:
        break

# -- END GATHERING JAVASCRIPT INFORMATION -- #

php_stars = []
php_repo_names = []

# --  GATHERING 10 MOST STARRED PHP REPOS -- #

php_repos = g.search_repositories(query='language:php')
count = 0
for repo in php_repos:
    if count < 10:
        print("PHP", repo.stargazers_count, str(repo))
        php_stars.insert(count, repo.stargazers_count)
        php_repo_names.insert(count, repo.name)
        count += 1
    else:
        break

# -- END GATHERING PHP INFORMATION -- #


pystars_total = 0
for i in range(0, len(python_stars)):
    pystars_total += python_stars[i]
#print("Python repo stars (in toto): " + str(pystars_total))

py_share_of_total = []
for i in range(0, len(python_stars)):
    py_share_of_total.insert(i, (python_stars[i]/pystars_total) * 100)

#print(py_share_of_total)


# Creating a Bar Chart to represent data gathered on public Java repos
java_bars = pygal.Bar()
for i in range(0, len(java_repo_names)):
    java_bars.add(java_repo_names[i], java_stars[i])
java_bars.render_to_file('javaBarchart.svg')

# Creating a Pie Chart to represent data gathered on public Python repos
pypie = pygal.Pie()
for i in range(0, len(python_repo_names)):
    pypie.add(python_repo_names[i], py_share_of_total[i])
pypie.render_to_file('pyPie.svg')

# Creating a Line Graph to show the difference in count between the top 10 of three more esoteric languages:
#       Prolog, Brainfuck, and COBOL
esoteric_line = pygal.Line()
esoteric_line.title = 'Comparison of the 10 highest Star Counts of public Prolog, Brainfuck, and COBOL repos'
esoteric_line.add('Prolog', prolog_stars)
esoteric_line.add('Brainfuck', bf_stars)
esoteric_line.add('COBOL', cobol_stars)
esoteric_line.render_to_file('esoteric.svg')

# Creating a Line Graph to compare how many stars the 10 largest repos for four main programming languages java_repos
#       Languages referenced here are HTML, CSS, JavaScript, and PHP

webdev_line = pygal.Line()
