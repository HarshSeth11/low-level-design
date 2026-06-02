from components.file_system_components import FileSystemComponent

class File(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name
    
    def display(self, indent: int = 0) -> None:
        print(" " * indent + f"📄 {self.name}")