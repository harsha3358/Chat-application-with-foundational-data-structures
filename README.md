#  Advanced Chat Engine

A command-line based one-to-one chat application built using foundational data structures implemented from scratch.  
This project demonstrates practical application of core Computer Science concepts in a clean, modular, and extensible architecture.

---

## Overview

GenAlpha Advanced Chat Engine is a terminal-based messaging system designed to showcase the real-world usage of fundamental data structures including Arrays, Stack, Linked List, HashMap, and HashSet.

The system simulates a structured chat workflow with session-based login, chat history management, undo functionality, and keyword search — all powered by custom data structure implementations.

This project is intended for academic submissions, data structures coursework, technical interviews, and placement preparation.

---

## Core Data Structures Used

| Data Structure | Implementation | Purpose |
|----------------|---------------|---------|
| Array | Python list | Stores registered users |
| HashSet | Python set | Tracks online users |
| Custom HashMap | Built from scratch | Maps user pairs to chat sessions |
| Linked List | Custom implementation | Stores chat history sequentially |
| Stack | Custom implementation | Enables undo functionality |

---

## Architecture

The system follows a modular, object-oriented architecture:

ChatEngine  
│  
├── UserManager (Array + HashSet)  
├── ChatManager (Custom HashMap)  
│     └── LinkedList (Chat History)  
├── UndoManager (Stack)  
└── Models (User, Message)  

Each module has a single responsibility, ensuring maintainability and clarity.

---

## Features

- User Registration
- Session-based Login
- One-to-one Chat
- Chat History Storage using Linked List
- Online User Tracking using HashSet
- Chat Routing using Custom HashMap
- Undo Last Message using Stack
- Keyword Search in Chat
- Clean CLI Interface

---

## Project Structure

genalpha_advanced_chat/  
│  
├── main.py  
├── models.py  
├── linked_list.py  
├── stack.py  
├── custom_hashmap.py  
├── user_manager.py  
├── chat_manager.py  
└── README.md  

---

## How to Run

1. Navigate to the project directory:

   cd genalpha_advanced_chat

2. Run the application:

   python main.py

No external dependencies are required.

---

## Functional Flow

1. Users register and are stored in an Array.
2. On login, users are added to the Online Users HashSet.
3. Messages are created as objects and stored in a Linked List.
4. Conversations are mapped using a Custom HashMap.
5. Every sent message is pushed to a Stack for undo support.
6. Chat history traversal displays conversation chronologically.

---

## Time Complexity Analysis

| Operation | Time Complexity |
|-----------|-----------------|
| Register User | O(1) |
| Login | O(n) |
| Send Message | O(1) average |
| View Chat | O(n) |
| Search Message | O(n) |
| Undo | O(1) |

---

## Technology Stack

- Python 3.x
- Object-Oriented Programming
- Core Data Structures Implementation

---

## License

This project is developed for academic and educational purposes.
