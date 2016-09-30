# README #

A modified version of the first project in CS322. A very basic web server in Python. Accepts incoming connections and serves them files depending on their query.
Prevents queries which attempt to change the directory (ones containing "~", ".." or "//") and ones that request anything other than an html or css file.
Hosts three .html files which each have their own .css files - home.html, trivia.html and colors.html. 

All three have very basic functionality and serve as sample pages.

### USAGE ###

Run the program, then enter 
```
localhost:PORT/pages/FILE
```
into a web browser. Only serves .html and .css files.

Can be run via automated configure and makefile scripts as well:

```
git clone ThisRepositoryURL InstallDirectory
cd InstallDirectory
make configure
make run
```