from database import Database
from transaction_manager import TransactionManager

def main():
    db = Database()
    transactionManager = TransactionManager()
    transactionManager.begin_transaction(db)

    db.insert("name", "harsh")
    db.insert("age", "23")

    db.display()

    transactionManager.commit_transaction()
    transactionManager.begin_transaction(db)

    db.delete("age")

    db.display()

    transactionManager.rollback_transaction(db)

    db.display()

    db.insert("123", "abc")

    transactionManager.commit_transaction()

    transactionManager.rollback_transaction(db)

if __name__ == "__main__":
    main()
