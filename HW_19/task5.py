# Type
# Only for 'Bot' class

def init_function(self, name):
    self.name = name


def say_name_function(self):
    print(self.name)


def send_message_function(self, message):
    print(message)


Bot = type(
    "Bot",
    (),
    {
        "__init__": init_function,
        "say_name": say_name_function,
        "send_message": send_message_function
    }
)

some_bot = Bot('Marvin')
# print(dir(some_bot))
some_bot.say_name()
some_bot.send_message("Hello")


# Type & Lambda
# Bot and TelegramBot classes

Bot = type(
    "Bot",
    (),
    {
    '__init__': lambda self, value_as_attr: setattr(self, 'name', value_as_attr),  # is it right?
    'say_name': lambda self: print(self.name),
    'send_message': lambda self, message: print(message)
    }
)

some_bot = Bot('Marvin')
# print(dir(some_bot2))

some_bot.say_name()
some_bot.send_message("Hello")


TelegramBot = type(
    "TelegramBot",
    (Bot, ),
    {
    'url': None,
    'chat_id': None,
    'set_url': lambda self, value_as_attr: setattr(self, 'url', value_as_attr),
    'set_chat_id': lambda self, value_as_attr: setattr(self, 'chat_id', value_as_attr),
    'send_message': lambda self, value_as_attr: print(f"{self.name} bot says {value_as_attr} to chat {self.chat_id} using {self.url}")
    }
)


telegram_bot = TelegramBot("TG")
# print(dir(telegram_bot))

telegram_bot.say_name()
telegram_bot.set_chat_id(1)
telegram_bot.send_message('Hello')
