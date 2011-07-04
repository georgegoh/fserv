fserv README
============

fserv is a web file manager that is intuitive and simple to use.

Features
--------
fserv is in a very early stage of development, and so has a
limited feature-set.

*   Familiar explorer-like interface to navigate.
*	Drag-and-drop files into browser to copy to server.

Set up
------
1.  Create a virtualenv environment.

    $ virtualenv --no-site-packages --distribute <directory>

2.  Activate the virtualenv.

    $ cd <directory>
    $ source ./bin/activate.sh

3.  Check out fserv into the virtualenv directory.

    $ cd <directory
    $ git clone git://github.com/georgegoh/fserv.git

4.  Install the dependencies.

    $ pip install -r dependencies.txt

5.  Run the server.

    $ paster serve development.ini

TODO
----
*   Unit tests.
*   Drop-and-drop files from browser to desktop.
*   Delete files.
*   CSS magic.
*   Proper logging messages and formatting.
