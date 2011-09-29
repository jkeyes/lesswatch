# lesswatch

Watches LESS files, and automatically compiles them when they
are changed.

## Usage

    $ lesswatch <DIR>

## Installation

    pip install lesswatch
    
or

    git clone https://github.com/jkeyes/lesswatch.git
    cd lesswatch
    python setup.py install

## External Dependencies

lesswatch used the [lessc compiler](http://lesscss.org/#guide)
and it must be on the PATH.

First you need to download and install node.js. Download the latest 
stable version of [node.js](http://nodejs.org/#download) and 
extract the contents from the archive: `tar xf node-v0.4.12.tar.gz`.

Then:

    $ cd node-v0.4.12
    $ ./configure
    $ make
    $ make install

Then you need to install LESS:

    $ npm install -g less

Try `lessc` to see if this was successful:

    $ which lessc
    /usr/bin/lessc
    $ echo "body  {  color:  red; }"  > test.less
    $ lessc test.less
    body {
      color: red;
    }
