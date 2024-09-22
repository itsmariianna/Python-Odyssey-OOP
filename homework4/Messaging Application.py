from typing import List
from abc import ABC, abstractmethod
import time


class Message(ABC):
    # Fields
    def __init__(self, sender: 'User', conversation: 'Conversation', timestamp: float = None) -> None:
        self.setSender(sender)
        self.setConversation(conversation)
        self.timestamp = timestamp if timestamp is not None else time.time()


    # Setters
    def setSender(self, value):
        if not isinstance(value, User):
            raise ValueError('Sender must be a User')
        self.__sender = value

    def setConversation(self, value):
        if not isinstance(value, Conversation):
            raise ValueError('Conversation must be a Conversation instance.')
        self.__conversation = value


    # Getters
    def getSender(self):
        return self.__sender

    def getConversation(self):
        return self.__conversation


    # Methods
    @abstractmethod
    def display_content(self) -> str:
        ...

    @abstractmethod
    def get_message_type(self) -> str:
        ...




class TextMessage(Message):
    def __init__(self, sender: 'User', conversation: 'Conversation', content: str):
        super().__init__(sender, conversation)
        self.setContent(content)

    # Setter for content
    def setContent(self, value):
        if value == "":
            raise ValueError("Content cannot be an empty string")
        self.__content = value

    # Getter for content
    def getContent(self):
        return self.__content


    # Methods
    def display_content(self) -> str:
        return self.__content

    def get_message_type(self) -> str:
        return 'Text'




class MultimediaMessage(Message):
    def __init__(self, sender: 'User', conversation: 'Conversation', file_path: str, media_type: str):
        super().__init__(sender, conversation)
        self.setFile_path(file_path)
        self.setMedia_type(media_type)

    # Setters
    def setFile_path(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("File path cannot be an empty string")
        self.__file_path = value

    def setMedia_type(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Media type cannot be an empty string")
        self.__media_type = value

    # Getters
    def getFile_path(self):
        return self.__file_path

    def getMedia_type(self):
        return self.__media_type

    # Methods
    def display_content(self) -> str:
        return f'{self.getFile_path()} : {self.getMedia_type()}'

    def get_message_type(self) -> str:
        return self.getMedia_type()




class MessagingManager(ABC):
    @abstractmethod
    def send_message(self, message: 'Message') -> None:
        ...

    @abstractmethod
    def receive_message(self, message: 'Message') -> None:
        ...

    @abstractmethod
    def view_conversation_history(self, conversation: 'Conversation') -> List['Message']:
        ...



class Conversation:
    def __init__(self, participants: List['User'] = None) -> None:
        self.setParticipants(participants or [])
        self.message_history: List['Message'] = []

    # Setter
    def setParticipants(self, value):
        if not isinstance(value, list):
            raise ValueError("It should be a list")
        self.__participants = value

    # Getter
    def getParticipants(self):
        return self.__participants


    # Methods
    def add_message(self, message: 'Message') -> None:
        self.message_history.append(message)

    def add_user(self, user: 'User') -> None:
        self.__participants.append(user)

    def get_messages(self) -> List['Message']:
        return self.message_history




class User:
    def __init__(self, name: str, contact_info: str):
        self.setName(name)
        self.setContact_info(contact_info)
        self.conversations = []
    
    # Setters
    def setName(self, value: str):
        if value == "":
            raise ValueError("Name cannot be an empty string")
        self.__name = value

    def setContact_info(self, value: str):
        if value == "":
            raise ValueError("Contact info cannot be an empty string")
        self.__contact_info = value


    # Getters
    def getName(self):
        return self.__name

    def getContact_info(self):
        return self.__contact_info
    

    def __str__(self) -> str:
        return f'name: {self.getName()}, contact info: {self.getContact_info()}'
    
    # Methods
    def create_conversation(self, user: 'User') -> 'Conversation':
        conv = Conversation()
        conv.add_user(self)
        conv.add_user(user)
        message = TextMessage(self, conv, "Hello bro")
        conv.add_message(message)
        return conv

    def send_message(self, message: 'Message', conversation: 'Conversation') -> None:
        conversation.add_message(message)

    def receive_message(self, message: 'Message') -> None:
        print(f'{self.__name} received message: {message.display_content()}')

    def manage_settings(self) -> None:
        ...

    def get_conversations(self) -> List['Conversation']:
        return self.conversations


# Checking

if __name__=='__main__':

    user1 = User("Mary", "077772322")
    user2 = User("Lisa", "099876543")
    my_conv = Conversation()
    my_conv.add_user(user1)
    my_conv.add_user(user2)
    my_conv.add_message(TextMessage(user1, my_conv, "Hey There"))
    user1.send_message(TextMessage(user2, my_conv, "Hello"), my_conv)
    user1.receive_message(TextMessage(user2, my_conv, "Hello"))
    user1.get_conversations()