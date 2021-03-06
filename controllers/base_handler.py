import webapp2
import jinja2
import os
import time
head, tail   = os.path.split(os.path.dirname(__file__))
template_dir = os.path.join(head, "templates")
jinja_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = False)


class BaseHandler(webapp2.RequestHandler):
	def write(self, value):
		self.response.out.write(value)

	def render(self, template, vals={}):
		template = jinja_environment.get_template("%s" % template)
		self.response.out.write(template.render(vals))
	def redirectto(self, url):
		time.sleep(1)
		self.redirect(url)







































	#def set_cookie(self, name, value, expires = ''):
	#	name, value, expires = str(name), str(value), str(expires)
	#	self.response.headers.add_header('Set-Cookie', '%s=%s; Expires=%s; Path=/' % (name, value, expires))

	#def get_cookie(self, name):
	#	return self.request.cookies.get(name)

	#def remove_cookie(self, name):
	#	self.set_cookie(name, '', 'Thu, 01-Jan-1970 00:00:00 GMT')


	#def json_write(self, dict):
	#	self.write(json.dumps(dict))

