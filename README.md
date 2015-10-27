# Simple Markdown Wiki

This project includes a single python script which takes all the markdown files
in the adjacent source directory and uses the python markdown library to generate
html. The script then uses jinja2 to insert the generated html into the tmeplate.html
file and writes it to a files in the adjacent build directory, mirroring the folder structure in
the source directory.

## License

see COPYING.txt

## Planned Features

- adding style sheets
- add sidebar and header to template (and decide what to put in them)
- create a python-based web server framework to allow in-browser edits that get tracked in a git repo (use gitpython)

## Webserver

Process for a user to update a page:
	1. User clicks the 'edit' button
	2. Load edit page for the chosen page file
		1. The edit page contains the git commit id for the version of the file that was being viewed
	3. Make changes in the test box
	4. Click 'submit'
	5. On the server, a new git-branch is created
	6. On the new branch, the file is replaced with the user's submission
	7. The branch is committed and merged with the master branch
		1. If a merge conflict occurs (happens only if another user submitted an edit AFTER THIS USER LOADED THE VIEW PAGE FROM WHICH EDIT WAS PRESSED)
			1. Again in a new branch, load an edit page with the file at the merged commit
			1. Return to step 3
		1. Else, the master branch should now be clean and contain the user's changes

