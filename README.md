# HTTPServer
A Simple HTTP Server implemented in Python.

##Why?
During my first attempt at creating a Home Automation System for my home, I realised I needed a flexible HTTP Server which I could easily interface with, using Python commands. Not having done much research originally, I smashed out a prototype and ended up coding my own HTTPServer using the python classes it ships with. I spent a decent amount of time perfecting the HTTP Server, and learnt alot in the process.

However, six months down the line, I began a second, more professional attempt at a Home Automation System which used Jetty. This negated the need for HTTPServer.py. 

I've uploaded it here in its own repository, mainly because I'm proud of the time I put into learning this technology and developing it, but also because some people wanted it use it for their own learning. 

Enjoy! 

##How?

The Code is very simple, it extends the BaseHTTPServer module which ships with Python 2.7. The code runs on the specified port, and waits for any GET requests on that port. This triggers the Do_GET() Method of the BaseHTTPServer class. I've implimented the logic which will parse the URL, look up the Mimetype and then return the file from the directory it is running in. 
