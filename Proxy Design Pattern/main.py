from proxy.document_proxy import DocumentProxy
from models.user import User

def main():
    admin = User("Harsh", "admin")

    employee = User("John", "employee")

    document_proxy = DocumentProxy()


    document_proxy.view(admin)  # Should allow access
    document_proxy.view(employee)  # Should deny access

if __name__ == "__main__":
    main()