import uuid

from handlers.base import BaseHandler
from google.appengine.api import users, memcache

from models.comment import Comment
from models.topic import Topic
from utils.decorators import validate_csrf


class TopicCreateHandler(BaseHandler):
    def get(self):
        return self.render_template("topic_create.html")

    @validate_csrf
    def post(self):

        user = users.get_current_user()

        topic_title = self.request.get("title")
        the_content = self.request.get("content")
        user = users.get_current_user()

        if not user:
            return self.redirect_to("not-registered")

        Topic.create()

        return self.redirect_to("topic-details", topic_id = new_topic.key.id())

class TopicDetails(BaseHandler):
    def get(self, topic_id):
        topic = Topic.get_by_id(int(topic_id))
        user = users.get_current_user()
        if not user:
            return self.redirect_to("not-registered")
        comments = Comment.query(Comment.topic_id == topic.key.id(), Comment.deleted == False).order(Comment.created).fetch()


        params = {'topic': topic, "comments": comments}

        return self.render_template('topic_details.html', params=params)

class TopicEdit(BaseHandler):
    def get(self, topic_id):
        topic = Topic.get_by_id(int(topic_id))
        params = {"topic": topic}
        return self.render_template("edit_topic.html", params=params)

    def post(self, topic_id):
        content = self.request.get("content")
        sporocilo = Topic.get_by_id(int(topic_id))
        sporocilo.content = content
        sporocilo.put()
        return self.redirect_to("main-page")

class TopicDelete(BaseHandler):
    def get(self, topic_id):
        topic = Topic.get_by_id(int(topic_id))
        params = {"topic": topic}
        return self.render_template("delete_topic.html", params=params)

    def post(self, topic_id):
        topic = Topic.get_by_id(int(topic_id))
        topic.deleted = True
        topic.put()
        return self.redirect_to("main-page")