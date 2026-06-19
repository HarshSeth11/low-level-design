from database import Database

class TransactionManager:
    def __init__(self):
        self.backup = None

    def begin_transaction(self, db : Database):
        print("=== Begin Transaction ===")
        self.backup = db.create_memento()

    def commit_transaction(self):
        print("=== Commit Transaction ===")
        if self.backup is not None:
            self.backup = None
        
        print("Transaction Committed successfully!\n")
    
    def rollback_transaction(self, db: Database):
        print("=== Rollback initialized ===")
        if self.backup is not None:
            db.restore_from_memento(self.backup)
            self.backup = None
            print("Transaction rolled back successfully!\n")
        else:
            print("None backup to rollback!\n")
