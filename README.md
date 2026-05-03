# Python Object-Oriented Programming - Library Management System

A demonstration of core Object-Oriented Programming concepts in Python, built as a library management system. This project showcases fundamental OOP principles through a practical CLI application.

## OOP Concepts Demonstrated

| Concept | Implementation |
|---------|----------------|
| **Inheritance** | `User` → `Student`, `Profesor`; `Book` → `PhysicalBook`, `DigitalBook` |
| **Encapsulation** | Private attributes with double underscore (`__times_loaned`) |
| **Polymorphism** | Override `calculate_duration()` in subclasses |
| **Abstraction** | Abstract base classes `BaseUser`, `BaseBook` using `ABC` module |
| **Protocols** | `RequesterProtocol`, `BookProtocol` for structural typing |
| **Properties** | `@property` decorators for getters/setters |

## Project Structure

```
.
├── main.py          # CLI entry point
├── persistence.py  # JSON data persistence
├── library.py      # Core Library class
├── books.py        # Book models (Book, PhysicalBook, DigitalBook)
├── users.py       # User models (User, Student, Profesor)
├── exceptions.py  # Custom exception hierarchy
└── data.py        # Sample data definitions
```

## Running the Application

```bash
python main.py
```

The CLI prompts for user ID and book title, then handles the loan process while persisting data to JSON.

## Custom Exceptions

- `LibraryError` - Base exception
- `LoanLimitError`
- `InvalidTitleError`
- `NoAvailableBookError`
- `NoAvailableUserError`

## Key Features

- Book loan system with availability tracking
- User borrow limits (students: 3 books, professors: unlimited)
- JSON persistence for library data
- ISBN validation
- Popular book tracking via loan count