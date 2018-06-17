class Contact():
    def __init__(self, name):
        self.name = name
        self.status = 1
        self.messages = []

    def add_msg(self, sender, msg, time):
        self.messages.append([sender, msg, time])
        