from handlers.base import BaseHandler
from google.appengine.api import users

from models.topic import Topic


class TopicCreateHandler(BaseHandler):
    def get(self):
        return self.render_template("topic_create.html")

    def post(self):
        topic_title = self.request.get("title")
        the_content = self.request.get("content")
        user = users.get_current_user()

        if not user:
            return self.write("You are not registered. Please log in.")

        new_topic = Topic(title=topic_title, content=the_content, author_email=user.email())
        new_topic.put()

        return self.write("Topic successfully created")

class TopicDetails(BaseHandler):
    def get(self, topic_id):
        topic = Topic.get_by_id(int(topic_id))

        params = {'topic': topic}

        return self.render_template('topic_details.html', params=params)
