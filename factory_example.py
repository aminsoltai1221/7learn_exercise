from abc import ABC, abstractmethod

class FileBase(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def openfile(self):
        pass

    @abstractmethod
    def editfile(self, content):
        pass


class XMLFile(FileBase):
    def openfile(self):
        with open(self.path, "r") as file:
            return file.read()

    def editfile(self, content):
        with open(self.path, "w") as file:
            file.write(content)


class JSONFile(FileBase):
    def openfile(self):
        with open(self.path, "r") as file:
            return file.read()

    def editfile(self, content):
        with open(self.path, "w") as file:
            file.write(content)


class WordFile(FileBase):
    def openfile(self):
        with open(self.path, "r") as file:
            return file.read()

    def editfile(self, content):
        with open(self.path, "w") as file:
            file.write(content)


class MarkdownFile(FileBase):
    def openfile(self):
        with open(self.path, "r") as file:
            return file.read()

    def editfile(self, content):
        with open(self.path, "w") as file:
            file.write(content)


class TXTFile(FileBase):
    def openfile(self):
        with open(self.path, "r") as file:
            return file.read()

    def editfile(self, content):
        with open(self.path, "w") as file:
            file.write(content)


class EditFile:
    formats = {"xml": XMLFile, "md": MarkdownFile, "doc": WordFile, "json": JSONFile, "txt": TXTFile}

    def __init__(self, path):
        self.path = path
        self.filetype = self.filetype()
        self.file_instance = self.formats[self.filetype](path)

    def filetype(self):
        return self.path.split(".")[-1]

    def readfile(self):
        return self.file_instance.openfile()

    def editting(self, content):
        self.file_instance.editfile(content)


# Example Usage
if __name__ == "__main__":
    file_path = "example.txt"

    # Writing to a file
    editor = EditFile(file_path)
    editor.editting("This is a new content for the TXT file.")

    # Reading from a file
    content = editor.readfile()
    print(content)
