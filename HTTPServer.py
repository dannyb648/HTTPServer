from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
from os import curdir, sep
import threading
import urlparse
import mimetypes

PORT_NUMBER = 8080
VERSION_NUMBER = '1.0.0'

class Handler(BaseHTTPRequestHandler):

	def do_GET(self):
		
		#Parse path into dictionary and process

		url = urlparse.urlparse(self.path)
		url_dict = urlparse.parse_qs(url.query)

		if self.path=='/':
			self.path="index.html"
			self.respond('text/html')
			return

		mimetype = mimetypes.guess_type(self.path)
		mimetype = mimetype[0]
		try:
			self.respond(mimetype)
		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)
		return

	def respond(self, mimetype):
		#Open the static file requested and send it
		f = open(curdir + sep + self.path) 
		self.send_response(200)
		self.send_header('Content-type',mimetype)
		self.end_headers()
		self.wfile.write(f.read())
		f.close()
		return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	"""Handle Requests in a seperate thread."""

if __name__ == '__main__':
	server = ThreadedHTTPServer(('', PORT_NUMBER), Handler)
	print 'Starting Server on port ' + str(PORT_NUMBER)
	print 'Version Code: ' + VERSION_NUMBER
	print 'Author @dannyb648 | danbeglin.co.uk'
	server.serve_forever()
