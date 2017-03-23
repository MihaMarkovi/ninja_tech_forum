from handlers.base import BaseHandler
from models.emails import Email


class SubscribeHandler(BaseHandler):
    def get(self):
        return self.render_template_with_csrf("subscribe_user.html")


    def post(self):

        subscribe_email = self.request.get("email")

        Email.create(subscribe_email=subscribe_email)

        return self.redirect_to("main-page")