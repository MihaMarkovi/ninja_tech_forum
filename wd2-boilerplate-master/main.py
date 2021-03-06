#!/usr/bin/env python
import webapp2

from crons.delete_comments import DeleteCommentsCron
from crons.delete_topics import DeleteTopicsCron
from crons.topics_subscribe import SubscribeTopicsCron
from handlers.gallery import GalleryHandler
from workers.email_new_comment import EmailNewCommentWorker
from handlers.comments import CommentAdd, CommentShow
from handlers.topics import TopicCreateHandler, TopicDetails, TopicEdit, TopicDelete
from handlers.base import MainHandler, CookieHandler, AboutHandler, HackerHandler, NotLoginHandler, SubscribeHandler

app = webapp2.WSGIApplication([

    #basic
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/about', AboutHandler, name="about-page"),
    webapp2.Route('/subscribe', SubscribeHandler, name="subscribe-page"),

    #cookie
    webapp2.Route('/set-cookie', CookieHandler, name="nastavi-cookie"),

    #topics
    webapp2.Route('/topic/add', TopicCreateHandler, name="topic-create"),
    webapp2.Route('/topic/<topic_id:(\d+)>', TopicDetails, name="topic-details"),
    webapp2.Route('/topic/<topic_id:(\d+)>/edit', TopicEdit, name="topic-edit"),
    webapp2.Route('/topic/<topic_id:(\d+)>/delete', TopicDelete, name="topic-delete"),
    webapp2.Route('/not_registered', NotLoginHandler, name="not-registered"),

    #hacker
    webapp2.Route('/hacker', HackerHandler, name="hacker-page"),

    #comment
    webapp2.Route('/topic/<topic_id:\d+>/comment/add', CommentAdd, name="comment-add"),
    webapp2.Route('/comment_list', CommentShow, name="comment-show"),

    #tasks
    webapp2.Route('/task/email-new-comment', EmailNewCommentWorker),

    #CRON
    webapp2.Route('/cron/delete-topics', DeleteTopicsCron, name='cron-delete-topics'),
    webapp2.Route('/cron/delete-comments', DeleteCommentsCron, name='cron-delete-comments'),
    webapp2.Route('/cron/subscribe-topics', SubscribeTopicsCron, name="subscribe-topics-cron"),

    #gallery
    webapp2.Route('/gallery', GalleryHandler, name="gallery"),
], debug=True)
