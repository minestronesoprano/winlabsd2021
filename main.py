import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomeHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        home_template = jinja_env.get_template('templates/index.html')
        self.response.write(home_template.render())

class AboutHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        about_template = jinja_env.get_template('templates/about.html')
        self.response.write(about_template.render())


app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/about', AboutHandler)
], debug=True)
