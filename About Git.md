# How to use Git
## 1. Download installer at https://git-scm.com/. Install Git.
## 2. Configure Git.
Git keeps track of who makes changes to a project, so Git needs to know your username and email.

git config --global user.name "username"  
git config --global user.email "username@example.com"
## 3. Making a project and adding a Ignoring File if needed.
Create a folder such as git_practice somewhere on your computer, and make a simple program such as hello_git.py. 
Files with extension .pyc are automatically generated from .py file, so we don't need Git to track on them. 
These files are stored in a directory called \_\_pycache\_\_. To tell Git to ignore this directory, make a file called .gitignore and add following line to it.

\_\_pycache\_\_/
## 4. Initializing a Repository
A repository is the set of files in a program that Git is actively tracking. All the files Git uses to manage the repository are located in the hidden directory .git.    
To initialize a repository, navigate to the workplace and run the following command:

git init

## 5. Checking the status
To check the status of Git, run the following command:

git status

In Git, a branch is a version of the project. 
## 6. Adding files to the repository
Adding files to repository tells Git to start paying attention to them. To add files to the repository, run the following command:

git add .
## 7. Making a commit
A commit is a snapshot of the project at a particular point in time. To make a commit, run the following command:

git commit -m "Message"  (-m tells Git to record the message)
or  
git commit -am "Message" (-a tells Git to add all modified files in the repository to the current commit)
## 8. Checking the log
To check the log of all commits made to the project, run the following command:

git log
git log --pretty=oneline (short version)
## 9. Reverting a change
To abandon a change and revert back to the previous working state, run the following command:

git checkout .
## 10. Checking out previous commits
To checkout any previous commit, run the following command:

git checkout ****** (****** is the first 6 characters of the reference ID)

To go back to branch, eg. branch master, run the following command:

git checkout master

To revert to a commit permanently, run the following command:

git reset --hard ****** (****** is the first 6 characters of the reference ID)
## 11. Deleting the repository
To do this, either open a file browser and delete the .git repository or delete it from the command line. 
This will delete all the commits but will not affect the current state of any of the file in workplace. To delete the .git folder from command line, run the following command:

rm -rf .git
