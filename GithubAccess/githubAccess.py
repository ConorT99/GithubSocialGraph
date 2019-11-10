from github import Github

# using username and password
g = Github("ConorT99", "redacted")

for repo in g.get_user().get_repos():
    branch = repo.get_branch("master")
    print(str(repo), "        ", str(branch.commit))
