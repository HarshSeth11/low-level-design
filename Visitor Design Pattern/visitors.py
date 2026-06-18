from abc import ABC, abstractmethod


class Visitor(ABC):

    @abstractmethod
    def visit_audio(self, audio_file):
        pass

    @abstractmethod
    def visit_image(self, image_file):
        pass

    @abstractmethod
    def visit_video(self, video_file):
        pass

    @abstractmethod
    def visit_text(self, text_file):
        pass