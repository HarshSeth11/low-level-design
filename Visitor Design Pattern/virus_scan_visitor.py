from visitors import Visitor

class VirusScanVisitor(Visitor):

    def visit_audio(self, audio_file):
        print(" "*4, f"{audio_file.name} Scaning the file\n")


    def visit_image(self, image_file):
        print(" "*4, f"{image_file.name} Scaning the file\n")


    def visit_video(self, video_file):
        print(" "*4, f"{video_file.name} Scaning the file\n")


    def visit_text(self, text_file):
        print(" "*4, f"{text_file.name} Scaning the file\n")