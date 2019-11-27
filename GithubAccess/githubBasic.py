from github import Github

g = Github("")

for repo in g.get_user().get_repos():
    branch = repo.get_branch("master")
    print(str(repo), "        ", str(branch.commit))
