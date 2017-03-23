import logging

from handlers.base import BaseHandler
from google.appengine.api import users, memcache

import uuid

from models.comment import Comment
from models.topic import Topic


class TopicCreateHandler(BaseHandler):
    def get(self):
        csrf_token = str(uuid.uuid4())

        logging.info("v get-u: " + csrf_token)

        user = users.get_current_user()

        memcache.add(key=csrf_token, value=user.email(), time=600)
        params={"csrf_token": csrf_token}
        return self.render_template("topic_create.html", params=params)

    def post(self):
        topic_title = self.request.get("title")
        the_content = self.request.get("content")
        user = users.get_current_user()

        if not user:
            return self.redirect_to("not-registered")
        csrf_token = self.request.get("csrf_token")

        logging.info("v post-u: " + csrf_token)

        csrf_value = memcache.get(csrf_token)

        if str(csrf_value) != user.email():
            return self.redirect_to("hacker-page")

        new_topic = Topic(title=topic_title, content=the_content, author_email=user.email())
        new_topic.put()

        return self.redirect_to("topic-details", topic_id = new_topic.key.id())

class TopicDetails(BaseHandler):
    def get(self, topic_id):
        csrf_token = str(uuid.uuid4())
        topic = Topic.get_by_id(int(topic_id))
        user = users.get_current_user()
        if not user:
            return self.redirect_to("not-registered")
        current_user = users.is_current_user_admin()
        memcache.add(key=csrf_token, value=user.email(), time=600)
        comments = Comment.query(Comment.topic_id == topic.key.id(), Comment.deleted == False).order(Comment.created).fetch()


        params = {'topic': topic, "csrf_token": csrf_token, "comments": comments, "current_user": current_user}

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