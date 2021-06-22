from __future__ import print_function
from github import Github
import os

g = Github("ghp_1cZCjQesq1m0n5ccRX0i9W7DybYipAf2gwZtT1")
user =g.get_user()
repo = user.create_repo('gitte31')
repo.create_file("nsktest.txt","commit","this is test file")

# os.system('git add .  > /dev/null 2>&1')
# os.system('git commit -q -nm "Automated commit" > /dev/null 2>&1')
# os.system('git remote add origin "git@github.com:nsivakrishna/gitte33.git" > /dev/null 2>&1')
# os.system('git push -q -u origin master > /dev/null 2>&1')
print(repo.name)

