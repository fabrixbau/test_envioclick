# Python Technical Test – EnvíoClick

This repository contains the solution to the Python backend technical test provided by EnvíoClick. The test consists of two exercises that evaluate logical thinking, Python development skills, and compliance with coding standards (PEP8).

---

## 📌 Exercise Summary

### 🔹 Exercise 1 – Word Occurrence Counter

Write a function that returns how many times a given word appears in a paragraph.

**Constraints:**

- The word must be counted only if it appears as a standalone word (not as part of another word).
- Case-insensitive and accent-insensitive.
- Native Python functions such as `in`, `find`, `index`, etc. are **not allowed**.

### 🔹 Exercise 2 – Filter and Sort Objects

Filter a list of dictionaries based on a set of criteria, and sort the filtered items by `priority` (descending).

**Constraints:**

- Native functions like `sort()` or `sorted()` are **not allowed**.
- Only items matching all criteria should be sorted and moved to the beginning of the list.

---

## 📁 Project Structure

## 📁 Project Structure

```text
python-test/
├── exercise1.py             # Logic for counting word occurrences
├── exercise2.py             # Logic for filtering and manually sorting items
├── input.py                 # Dataset used in Exercise 2
├── main.py                  # Entry point for running both exercises
├── tests/
│   ├── test_exercise1.py    # Unit tests for Exercise 1
│   └── test_exercise2.py    # Unit tests for Exercise 2
├── .gitignore
└── README.md



## 💻 Quick Start

# Clone the repository (if not already)
git clone https://github.com/your-username/your-repo-name.git
cd python-test

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run the project
python main.py

# Run all unit tests
python -m unittest discover -s tests
```
