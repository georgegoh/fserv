fserv README
============

fserv is a web file manager that is intuitive and simple to use.

WARNING: This code is in a very early stage of development.
Many features are still yet to be implemented.

Features
--------
fserv is in a very early stage of development, and so has a
limited feature-set.

*   Familiar explorer-like interface to navigate.
*	Drag-and-drop files into browser to copy to server.

Set up
------
Create a virtualenv environment.

    $ virtualenv --no-site-packages --distribute <directory>

Activate the virtualenv.

    $ cd <directory>
    $ source ./bin/activate.sh

Check out fserv into the virtualenv directory.

    $ cd <directory>
    $ git clone git://github.com/georgegoh/fserv.git

Install the dependencies.

    $ cd fserv
    $ pip install -r dependencies.txt

Run the server.

    $ paster serve development.ini

TODO
----
*   Unit tests.
*   Drop-and-drop files from browser to desktop.
*   Delete files.
*   CSS magic.
*   Proper logging messages and formatting.
