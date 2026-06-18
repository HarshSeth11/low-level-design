from audio_file import AudioFile
from image_file import ImageFile
from text_file import TextFile
from video_file import VideoFile
from size_visitor import SizeVisitor
from virus_scan_visitor import VirusScanVisitor

def main():
    audiofile = AudioFile("audio", 5)
    imagefile = ImageFile("image", 10)
    textfile = TextFile("text", 2)
    videofile = VideoFile("video", 69)

    size_visitor = SizeVisitor()
    virus_scan_visitor = VirusScanVisitor()

    audiofile.accept(size_visitor)
    audiofile.accept(virus_scan_visitor)
    
    imagefile.accept(size_visitor)
    imagefile.accept(virus_scan_visitor)

    textfile.accept(size_visitor)
    textfile.accept(virus_scan_visitor)

    videofile.accept(size_visitor)
    videofile.accept(virus_scan_visitor)

if __name__ == "__main__":
    main()
