import json

from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


from .models import Blog, Comment


class CommentConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.blog_id = self.scope['url_route']['kwargs']['blog_id']
        self.blog_group_name = 'blog_' + self.blog_id

        print (f"Connect consumer with group name {self.blog_group_name}")

        await self.channel_layer.group_add(self.blog_group_name, self.channel_name)
        await self.accept()


    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.blog_group_name, self.channel_name)


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        comment = text_data_json['message']
        name = text_data_json['name']

        print (f"name - {name} and comment - {comment}")
        print (f"scope:\t\t {self.scope}")
        new_comment = await self.create_new_comment(comment, name)

        data = {'name' : new_comment.name, 
                'created_on' : new_comment.created_on.ctime(),
                'body' : new_comment.body}

        await self.channel_layer.group_send(
            self.blog_group_name,
            {
              'type' : 'new_comment',
              'message' : data
            })


    async def new_comment(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({'message' : message}))


    @database_sync_to_async
    def create_new_comment(self, text, name):
        ct = ContentType.objects.get_for_model(Blog)
        #blog = Blog.objects.filter(id=self.blog_id)
        blog = get_object_or_404(Blog, pk=self.blog_id)
        print("type ct  " + str(type(blog)))
        new_comment = Comment.objects.create(
                      blog=blog,
                      name=name,
                      body=text)

        return new_comment


