from file_system import FileSystem
from visitors import Visitor

class VideoFile(FileSystem):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def accept(self, visitor : Visitor):
        visitor.visit_video(self)
