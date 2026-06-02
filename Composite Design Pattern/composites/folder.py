from components.file_system_components import FileSystemComponent

class Folder(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name
        self.children = []
    
    def add(self, component: FileSystemComponent) -> None:
        self.children.append(component)
    
    def display(self, indent: int = 0) -> None:
        print(" " * indent + f"📁 {self.name}")
        for child in self.children:
            child.display(indent + 4)