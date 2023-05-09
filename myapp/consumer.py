from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync




class Notification(AsyncConsumer):

    async def websocket_connect(self, event):
        group_name = self.scope['url_route']['kwargs']["group_name"]
        # add chanel to group
        await self.channel_layer.group_add(group_name, self.channel_name)

        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        group_name = self.scope['url_route']['kwargs']["group_name"]
        # sending message to group
        # await self.channel_layer.group_send(group_name, {
        #     "type": "chat.message",
        #     "message": event["text"]
        # })

        await self.channel_layer.group_send("dgre", {
            "type": "message.notification",
            "message": event["text"]
        })

    async def chat_message(self, event):
        print("chat message event", event)
        await self.send({
            "type": "websocket.send",
            "text": event['message'],
        })

    async def message_notification(self, event):
        await self.send({
            "type": "websocket.send",
            "text": "new message received from DEAL",
        })
    async def websocket_disconnect(self, event):
        group_name = self.scope['url_route']['kwargs']["group_name"]
        await self.channel_layer.group_discard(
            group_name,
            self.channel_name
        )
        raise StopConsumer()





