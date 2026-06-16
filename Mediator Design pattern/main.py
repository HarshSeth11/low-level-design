from employee import Employee
from chatroom import ChatRoom

def main():
    chat_room = ChatRoom()

    harsh = Employee("Harsh", chat_room)
    rahul = Employee("Rahul", chat_room)
    harman = Employee("Harman", chat_room)

    harsh.send("Hey all. How are you doing?")
    harman.send_private(harsh, "I'm good harsh.")
    rahul.send("Great!! How are you.")

if __name__ == "__main__":
    main()