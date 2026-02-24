from user_manager import UserManager
from chat_manager import ChatManager
from stack import Stack
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_header(username=None):
    print("="*50)
    print("🚀 GenAlpha Advanced Chat Engine")
    print("="*50)
    if username:
        print(f"Logged in as: {username}")
    print("-"*50)

def main():
    user_manager = UserManager()
    chat_manager = ChatManager()
    undo_stack = Stack()

    current_user = None
    current_chat_partner = None

    while True:
        clear()
        print_header(current_user)

        if not current_user:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("\nSelect option: ")

            if choice == "1":
                username = input("Enter username: ")
                user_manager.register(username)
                input("Press Enter to continue...")

            elif choice == "2":
                username = input("Enter username: ")
                if user_manager.login(username):
                    current_user = username
                input("Press Enter to continue...")

            elif choice == "3":
                break

        else:
            print("1. Open Chat")
            print("2. Send Message")
            print("3. View Chat")
            print("4. Search Messages")
            print("5. Undo Last Message")
            print("6. Logout")
            print("7. Exit")

            choice = input("\nSelect option: ")

            if choice == "1":
                current_chat_partner = input("Enter username to chat with: ")
                input("Chat opened. Press Enter to continue...")

            elif choice == "2":
                if not current_chat_partner:
                    input("Open chat first. Press Enter...")
                    continue

                content = input("Enter message: ")
                chat_manager.send_message(
                    current_user,
                    current_chat_partner,
                    content,
                    user_manager,
                    undo_stack
                )
                input("Message sent. Press Enter...")

            elif choice == "3":
                if not current_chat_partner:
                    input("Open chat first. Press Enter...")
                    continue

                clear()
                print_header(current_user)
                print(f"Chat with: {current_chat_partner}")
                print("-"*50)
                chat_manager.show_chat(current_user, current_chat_partner)
                print("-"*50)
                input("Press Enter to continue...")

            elif choice == "4":
                keyword = input("Search keyword: ")
                chat_manager.search_chat(current_user, current_chat_partner, keyword)
                input("Press Enter to continue...")

            elif choice == "5":
                data = undo_stack.pop()
                if data:
                    key, msg = data
                    print("Last message undone.")
                else:
                    print("Nothing to undo.")
                input("Press Enter...")

            elif choice == "6":
                current_user = None
                current_chat_partner = None

            elif choice == "7":
                break

if __name__ == "__main__":
    main()