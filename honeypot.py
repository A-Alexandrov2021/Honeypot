import pyinotify
from telethon import TelegramClient
from telethon import sync, events

api_id = XXXXXX
api_hash = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

client = TelegramClient('Alexander', api_id, api_hash)
client.start()

dlgs = client.get_dialogs()

class MyEventHandler(pyinotify.ProcessEvent):
    def send_alarm_message(self, event_type):
        client.send_message('Black Christmas', f"ALERT! A file operation of type {event_type} was detected in the monitored directory!")

    def process_IN_ACCESS(self, event):
        self.send_alarm_message("IN_ACCESS")

    def process_IN_ATTRIB(self, event):
        self.send_alarm_message("IN_ATTRIB")

    def process_IN_CLOSE_NOWRITE(self, event):
        self.send_alarm_message("IN_CLOSE_NOWRITE")

    def process_IN_CLOSE_WRITE(self, event):
        self.send_alarm_message("IN_CLOSE_WRITE")

    def process_IN_CREATE(self, event):
        self.send_alarm_message("IN_CREATE")

    def process_IN_DELETE(self, event):
        self.send_alarm_message("IN_DELETE")

    def process_IN_MODIFY(self, event):
        self.send_alarm_message("IN_MODIFY")

    def process_IN_OPEN(self, event):
        self.send_alarm_message("IN_OPEN")

def main():
    wm = pyinotify.WatchManager()
    wm.add_watch('/home/pentest/Desktop/', pyinotify.ALL_EVENTS, rec=True)
    eh = MyEventHandler()
    notifier = pyinotify.Notifier(wm, eh)
    notifier.loop()

if __name__ == '__main__':
    main()           
