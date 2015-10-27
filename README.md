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

