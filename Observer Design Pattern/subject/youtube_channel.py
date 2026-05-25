
class Youtube_Channel:
    def __init__(self, channel_name):
        self.channel_name = channel_name
        self.observers = []
    
    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, data):
        for observer in self.observers:
            observer.update(data)

    def upload_video(self, video_title):
        print(f"\n{self.channel_name} uploaded a new video: {video_title}\n")
        self.notify_observers(video_title)