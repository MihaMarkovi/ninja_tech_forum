import os
import jinja2
import webapp2
from google.appengine.api import users

from models.topic import Topic

template_dir = os.path.join(os.path.dirname(__file__), "../templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}

        cookie = self.request.cookies.get("ninja-cookie")

        if cookie:
            params["piskotki"] = True

        #googlov login

        user = users.get_current_user()
        if user:
            params["user"] = user
            params["logout_url"] = users.create_logout_url(self.request.uri)

        else:
            params["login_url"] = users.create_login_url(self.request.uri)

        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        seznam = Topic.query( Topic.deleted == False).order(-Topic.updated).fetch()
        params = {"seznam": seznam}
        return self.render_template("main.html", params=params)

class NotLoginHandler(BaseHandler):
    def get(self):
        return self.render_template("not_registered.html")

class AboutHandler(BaseHandler):
    def get(self):
        return self.render_template("about.html")

class HackerHandler(BaseHandler):
    def get(self):
        return self.render_template("hacker.html")


class CookieHandler(BaseHandler):
    def post(self):
        self.response.set_cookie(key="ninja-cookie", value="accepted")
        return self.redirect_to("main-page")
