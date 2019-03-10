Basic Operations
----------------

* Clone repo ``git clone [uri]``
* Clone repo a specific branch other than default ``git clone -b <BRANCH> [uri]``
* Clone a bare repository ``git clone --bare [uri]``. Useful for git migration or rewriting history 
* add file to index for commit ``git add <FILE>``
* remove file from working tree and index ``git rm <FILE>`` for directory ``git rm -rf <DIR>``
* show working tree status ``git status``
* List git configuration ``git config -l``
* Set username and email attached to all commits in the repo ``git config user.name "<NAME>" user.email "<EMAIL>"``
* Set username and email attached to all commits for all repos ``git config --global user.name "<NAME>" user.email "<EMAIL>"``.


Git Log
--------

* View merge commits to a particular branch ``git log --merges``
* View commits in reverse order: ``git log --reverse``
* Commit Formatting: ``git log --oneline`` to view shorthand commit or ``git log --pretty=oneline`` 
* Commit Limit: ``git log -n 4``
* View Commit History by file ``git log -p <filename>``


Commit undo
------------

* Move HEAD by 3 ``git reset HEAD~3``
* Move HEAD to particular commit ``git reset 15a135162aa91515ef05ef48322db954ddf48c06``

Branches
--------

* View Branches: ``git branch``
* Create Branche:  ``git branch <BRANCH>``
* Create and Switch Branch: ``git checkout -b <BRANCH>``
* Delete Branch Locally: ``git branch -d <BRANCH>``
* Delete Remote Branch: ``git push origin :<BRANCH>``
* Delete Multiple Branch Local: ``git branch -d <BRANCH1> <BRANCH2> ...``
* Delete Multiple Branch Remote: ``git push origin :<BRANCH1> :<BRANCH2> ...``
* Rename Branch ``git branch -m <BRANCH> <NEW_BRANCH>``
* List Remote Tracking and Local Branch ``git branch -a``
* Pull remote branch and name branch ``git fetch origin <BRANCH>:<BRANCH_NAME>``
* Checkout remote branch ``git checkout -b LocalName origin/remotebranchname``
* Checkout a particular commit ``git checkout -b <BRANCH> <COMMIT_SHA>``
* Fetch all branches ``git fetch origin``
* Pulling a PR ``git fetch origin pull/ID/head:BRANCHNAME`` then switch to the branch ``git checkout BRANCHNAME``. You can push to the PR by ``git push origin BRANCHNAME``

Git Remote
------------

* View remote ``git remote``
* View remote with verbose output ``git remote -v``
* Adding new remote ``git remote add <alias> <URI>`` for example run ``git remote add upstream git@github.com:PfizerRD/hpcdocs.git``
* Rename alias ``git remote rename <old> <new>``
* Remove alias ``git remote remove <name>``

Git Commit
------------
Apply a commit ``git commit``
Commit at command line ``git commit -m <MESSAGE>``
Commit with custom author ``git commit -m <MESSAGE> --author="<NAME EMAIL>"``
Commit amend: ``git commit --amend``

Git Show
--------

* View changes ``git show``
* Show changes between index and the HEAD ``git diff --cached``
* Show all changes between working directory and HEAD ``git diff HEAD``
