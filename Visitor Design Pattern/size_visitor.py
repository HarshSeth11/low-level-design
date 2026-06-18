from visitors import Visitor

class SizeVisitor(Visitor):

    def visit_audio(self, audio_file):
        print(" "*4, f"Calculating the Size for {audio_file.name} : {audio_file.size}\n")


    def visit_image(self, image_file):
        print(" "*4, f"Calculating the Size for {image_file.name} : {image_file.size}\n")


    def visit_video(self, video_file):
        print(" "*4, f"Calculating the Size for {video_file.name} : {video_file.size}\n")


    def visit_text(self, text_file):
        print(" "*4, f"Calculating the Size for {text_file.name} : {text_file.size}\n")
