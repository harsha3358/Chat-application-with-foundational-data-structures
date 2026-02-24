from linked_list import LinkedList
from custom_hashmap import CustomHashMap
from models import Message

class ChatManager:
    def __init__(self):
        self.chats = CustomHashMap()

    def _chat_key(self, u1, u2):
        return tuple(sorted([u1, u2]))

    def send_message(self, sender, receiver, content, user_manager, undo_stack):
        msg = Message(sender, receiver, content)

        if user_manager.is_online(receiver):
            msg.status = "Delivered"

        key = self._chat_key(sender, receiver)

        chat = self.chats.get(key)
        if not chat:
            chat = LinkedList()
            self.chats.put(key, chat)

        chat.append(msg)
        undo_stack.push((key, msg))

        print("Message processed.")

    def show_chat(self, u1, u2):
        key = self._chat_key(u1, u2)
        chat = self.chats.get(key)

        if chat:
            chat.display()
        else:
            print("No chat found.")

    def search_chat(self, u1, u2, keyword):
        key = self._chat_key(u1, u2)
        chat = self.chats.get(key)
        if chat:
            chat.search(keyword)