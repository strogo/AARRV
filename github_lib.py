from github2.client import Github
from github2.repositories import Repositories

def numWatchers(repoName):
  github = Github()
  num = len(github.repos.watchers("opengovernment/" + repoName))
  return num

def numCoders(repoName):
  github = Github()
  num = len(github.repos.list_contributors("opengovernment/" + repoName))
  return num
