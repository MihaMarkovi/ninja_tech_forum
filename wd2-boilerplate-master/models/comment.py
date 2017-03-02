from google.appengine import ndb

class Comment(ndb.Model):
    content = ndb.TextProperty
    author_email = ndb.StringProperty
    topic_id = ndb.IntegerProperty
    topic_title = ndb.StringProperty()
