# README #

###CS322 Project 1: Basic Server###
###Author: Marc Leppold###

##Project Notes

A modified version of the first project in CS322. A very basic server in Python. Accepts incoming connections and serves them files depending on their query.
Prevents queries which attempt to change the directory (ones containing "~", ".." or "//") and ones that request anything other than an html or css file.
Hosts three .html files which each have their own .css files - home.html, trivia.html and colors.html. 

All three have very basic functionality and serve as sample pages. Currently works over the local network only. 

### USAGE ###

Execute pageserver.py, then enter 
```
localhost:PORT/FILE
```
into an internet browser, where FILE matches an appropriate html or css file on the server and PORT matches the port the server is running on (default 8000).

Can be executed via automated configure and makefile scripts as well:

```
git clone https://github.com/zenranda/proj-pageserver InstallDirectory
cd InstallDirectory
make configure
make run
```
where InstallDirectory is the directory you cloned the files to.