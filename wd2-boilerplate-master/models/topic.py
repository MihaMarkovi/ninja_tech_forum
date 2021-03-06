from google.appengine.ext import ndb

class Topic(ndb.Model):
    title = ndb.StringProperty()
    content = ndb.TextProperty()
    author_email = ndb.StringProperty()
    created = ndb.DateProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)

    @classmethod
    def delete(cls, topic):
        topic.deleted=True
        topic.put()

        return topic

    @classmethod
    def create(cls, topic_title, the_content, user):
        new_topic = Topic(title=topic_title, content=the_content, author_email=user.email())
        new_topic.put()
