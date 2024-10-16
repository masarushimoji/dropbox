# dropbox

[This is my attempt at creating an application with two components with the following functionality:]

1. A simple command line client which takes one directory (the source) as argument, keeps monitoring changes in that directory, and uploads any change to its server

2. A simple server which takes one directory (the destination) as argument and receives
any change from its client

[Side notes:]

The code is written in python and all of the testing has been done on a linux machine.