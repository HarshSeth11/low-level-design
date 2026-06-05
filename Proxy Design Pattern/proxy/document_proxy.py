from subject.confidential_document import ConfidentialDocument

class DocumentProxy(ConfidentialDocument):
    def __init__(self):
        self.document = ConfidentialDocument()
    
    def view(self, user):
        if user.role == "admin":
            self.document.view()
        else:
            print(
                f"Access denied for {user.name}"
            )