# README #

###CS322 Project 1: Basic Web Server###
###Author: Marc Leppold###

##Project Notes## 

A modified version of the first project in CS322. A very basic web server in Python. Accepts incoming connections and serves them files depending on their query.
Prevents queries which attempt to change the directory (ones containing "~", ".." or "//") and ones that request anything other than an html or css file.
Hosts three .html files which each have their own .css files - home.html, trivia.html and colors.html. 

All three have very basic functionality and serve as sample pages.

### USAGE ###

Execute pageserver.py, then enter 
```
localhost:PORT/pages/FILE
```
into a web browser.

Can be run via automated configure and makefile scripts as well:

```
git clone https://github.com/zenranda/proj-pageserver InstallDirectory
cd InstallDirectory
make configure
make run
```
where InstallDirectory is the directory you clone the files to.