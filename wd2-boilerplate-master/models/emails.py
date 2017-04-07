from google.appengine.ext import ndb

class Email(ndb.Model):
    email = ndb.StringProperty()
    name = ndb.StringProperty()
    updated = ndb.DateTimeProperty(auto_now=True)

