# noting on ubuntu
1 connect the local repository to remote
	cmd:	git remote add origin <server>

2 add all change to cache areas
	cmd:	git add *

3 push your branch to remote
	cmd:	git push origin <branch>

4 update your local repository to the up-to-date change
	cmd:	git pull

5 merge branch
	cmd:	git merge <branch>

6 built a tag 
	cmd:	git tag 1.0.0 <ID>

7 get log (ID)
	cmd:	git log --oneline

8 replace local file with file in repository
	cmd:	git checkout -- <filename>

9 open a graphical git
	cmd:	gitk 

10 delete the remote branch
	cmd:	git push origin :<branch name>

11 delete the remote repository
	cmd:	git remote rm [alias]