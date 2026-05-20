Here’s a good professional README for your current project.

You can place this inside:

```text id="w7m2qx"
README.md
```

---

````md id="y4k8pn"
# Low Level Design - Strategy & Factory Pattern

This project was built to deeply understand Low Level Design concepts using Python.

The project demonstrates:
- Strategy Design Pattern
- Factory Design Pattern
- SOLID Principles
- Runtime Behavior Switching
- Metrics Tracking
- Clean Modular Architecture

---

# Project Overview

A dynamic sorting system where users can choose different sorting algorithms at runtime.

The application supports:
- Bubble Sort
- Merge Sort
- Insertion Sort
- Quick Sort

The selected sorting algorithm is created using the Factory Pattern and executed using the Strategy Pattern.

---

# Concepts Implemented

## 1. Strategy Design Pattern

The Strategy Pattern is used to encapsulate sorting algorithms into separate interchangeable classes.

This allows:
- dynamic runtime switching,
- loose coupling,
- scalable architecture.

### Benefits
- avoids large if-else chains,
- improves extensibility,
- follows Open/Closed Principle.

---

## 2. Factory Design Pattern

The Factory Pattern centralizes object creation logic.

Instead of directly creating strategy objects inside `main.py`, object creation is delegated to `StrategyFactory`.

### Benefits
- cleaner client code,
- reduced coupling,
- easier scalability.

---

# SOLID Principles Used

## Single Responsibility Principle
Each class has a single responsibility.

## Open/Closed Principle
New sorting algorithms can be added without modifying existing code.

## Dependency Inversion Principle
`Sorter` depends on abstractions instead of concrete implementations.

---

# Features

- Dynamic sorting algorithm selection
- Runtime strategy switching
- Execution time tracking
- Comparisons tracking
- Data movement tracking
- CLI-based interaction
- Clean folder structure

---

# Folder Structure

```text
low-level-design/
│
├── strategies/
│   ├── base_strategy.py
│   ├── bubble_sort.py
│   ├── merge_sort.py
│   ├── insertion_sort.py
│   └── quick_sort.py
│
├── factory/
│   └── strategy_factory.py
│
├── context/
│   └── sorter.py
│
├── utils/
│   └── metrics.py
│
└── main.py
````

---

# How to Run

## Clone Repository

```bash
git clone https://github.com/HarshSeth11/low-level-design.git
```

---

## Run Application

```bash
python main.py
```

---

# Sample Output

```text
Choose Sorting Algorithm:

1. Bubble Sort
2. Merge Sort
3. Insertion Sort
4. Quick Sort

Enter your choice: 2

Enter numbers separated by space:
5 2 9 1 7

Sorted Data: [1, 2, 5, 7, 9]

Metrics:
Comparisons: 8
Data Movements: 12
Execution Time: 0.000041 sec
```

---

# Learning Outcome

This project helped in understanding:

* scalable software architecture,
* design patterns,
* clean code practices,
* modular backend engineering.

---

# Future Improvements

* Observer Pattern integration
* Logging support
* Unit Testing
* Custom Exceptions
* Visualization
* Benchmarking
* Async execution

---

# Tech Stack

* Python
* OOP
* Design Patterns

```

---

# Small Recommendation

After pasting:
1. commit README,
2. push to GitHub,
3. add screenshots in repo,
4. pin repo on GitHub profile.

This already looks strong for a 2 YOE backend portfolio.
```
