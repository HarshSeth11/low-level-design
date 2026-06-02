from composites.folder import Folder
from leaves.file import File

def main():
    root = Folder("root")

    folder1 = Folder("folder1")
    folder2 = Folder("folder2")
    folder3 = Folder("folder3")

    root.add(folder1)
    root.add(folder2)

    file1 = File("file1.txt")
    file2 = File("file2.txt")

    folder1.add(file1)
    folder2.add(file2)
    folder2.add(folder3)

    root.display()

if __name__ == "__main__":
    main()