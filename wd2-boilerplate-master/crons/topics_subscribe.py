import datetime

from handlers.base import BaseHandler
from models.topic import Topic


class SubscribeTopicsCron(BaseHandler):
    def get(self):
        topics = Topic.query(Topic.created >= datetime.datetime.now() - datetime.timedelta(days=1)).fetch


