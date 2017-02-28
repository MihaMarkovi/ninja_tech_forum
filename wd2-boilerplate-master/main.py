#!/usr/bin/env python
import webapp2
from handlers.base import MainHandler, CookieHandler, AboutHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/about', AboutHandler, name="about-page"),
    webapp2.Route('/set-cookie', CookieHandler, name="nastavi-cookie")
], debug=True)
