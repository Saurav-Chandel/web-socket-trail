from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
# Create your models here.


class Profile(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE)
    FirstName=models.CharField(max_length=300)
    LastName=models.CharField(max_length=400)


class MessageModel(models.Model):
    """
    This class represents a chat message. It has a owner (user), timestamp and
    the message body.
    """

    user=models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name='sender',related_name='from_user')
    recipient=models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name='recipient',related_name='to_user',)
    timestamp = models.DateTimeField('timestamp', auto_now_add=True, editable=False)
    body = models.TextField('body')

    def __str__(self):
        return str(self.id)

    # def characters(self):
    #     """
    #     Toy function to count body characters.
    #     :return: body's char number
    #     """
    #     return len(self.body)

    # def notify_ws_clients(self):
    #     """
    #     Inform client there is a new message.
    #     """
    #     notification = {
    #         'type': 'recieve_group_message',
    #         'message': '{}'.format(self.id)
    #     }

    #     channel_layer = get_channel_layer()
    #     print("user.id {}".format(self.user.id))
    #     print("user.id {}".format(self.recipient.id))

    #     async_to_sync(channel_layer.group_send)("{}".format(self.user.id), notification)
    #     async_to_sync(channel_layer.group_send)("{}".format(self.recipient.id), notification)

    # def save(self, *args, **kwargs):
    #     """
    #     Trims white spaces, saves the message and notifies the recipient via WS
    #     if the message is new.
    #     """
    #     new = self.id
    #     self.body = self.body.strip()  # Trimming whitespaces from the body
    #     super(MessageModel, self).save(*args, **kwargs)
    #     if new is None:
    #         self.notify_ws_clients()

    # # Meta
    # class Meta:
    #     app_label = 'app'
    #     verbose_name = 'message'
    #     verbose_name_plural = 'messages'
    #     ordering = ('-timestamp',)    


