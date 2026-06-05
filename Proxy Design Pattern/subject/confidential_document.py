from subject.document import Document

class ConfidentialDocument(Document):

    def view(self):
        print("Viewing confidential company document")