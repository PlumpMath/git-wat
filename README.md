`git-wat` (Web API Tool) is a tool for interacting with the web APIs on
sites like github, gitlab, bitbucket etc. It lets you do routine tasks
without leaving the command line. For example, on Github, without
`git-wat` Creating a repo:

    git init my-project
    cd my-project
    # Do stuff
    git add .
    git commit
    git remote add origin git@github.com:me/my-project
    # Go to github's website, log in, navigate to the create repo
    # dialog, and fill out the form.
    git push -u origin master


With `git-wat`:

    git init my-project
    cd my-project
    # Do stuff
    git add .
    git commit
    git remote add origin git@github.com:me/my-project
    git wat init origin my-project
    git push -u origin master


This is very WIP.

License: GPLv3 or later.
