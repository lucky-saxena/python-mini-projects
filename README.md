# Python Mini Projects

A collection of small Python practice projects, each focused on a different concept or use case.

---

## 🧮 Calculator

**Concepts learned**
- Python's `match`/`case` statement (structural pattern matching, Python 3.10+) as a cleaner alternative to a long `if`/`elif` chain
- Using `try`/`except ValueError` to catch bad numeric input from `float(input(...))`
- Guarding against division by zero before performing the operation
- Using `.strip()` to clean up user input before comparing it

**Future improvements**
- Loop back to the menu after a calculation instead of exiting after one operation
- Catch invalid input for the *operator* too (currently only `a`/`b` parsing is wrapped in `try`/`except`)
- Add more operations (exponent, modulus, square root)
- Round or format the result output for cleaner display

---

## 💧 DrinkWaterReminder

**Concepts learned**
- Using the `plyer` library to send cross-platform desktop notifications
- Running an infinite loop (`while True`) combined with `time.sleep()` to trigger a repeated action on an interval
- Gracefully exiting a long-running loop with `try`/`except KeyboardInterrupt`

**Future improvements**
- Let the user set the reminder interval instead of a hardcoded 1 hour (`60*60`)
- Add a way to pause/snooze reminders without stopping the whole program
- Track how many times the user has been reminded/hydrated in a session

---

## 📄 PDFMerger

**Concepts learned**
- Using `PyPDF2`'s `PdfWriter` to combine multiple PDF files into one
- Dynamically building a list of filenames based on user-specified count (`n = int(input(...))` + loop)
- Writing output to a new file and properly closing the writer

**Future improvements**
- Validate that each entered filename actually exists before trying to append it
- Let the user pick the output filename instead of hardcoding `merged-pdf.pdf`
- Handle corrupted/invalid PDF files without crashing the whole merge
- Support drag-and-drop or a folder scan instead of typing filenames manually

---

## 🔗 QRCodeGenerator

**Concepts learned**
- Using the `qrcode` library to encode a URL/string into a scannable QR code image
- String methods (`.endswith()`) to validate and auto-correct a filename extension
- Saving generated image output to disk

**Future improvements**
- Validate that the entered URL is well-formed before generating the code
- Let the user customize size, color, and error-correction level
- Support generating and saving multiple QR codes in one run (batch mode)

---

## ❓ QuizApp

**Concepts learned**
- Storing structured quiz data as a list of lists (`[question, opt1, opt2, opt3, opt4, correct_index]`)
- Iterating through questions with a `for` loop and checking answers with conditionals
- Modeling an escalating "prize ladder" (KBC-style) tied to an index counter, ending the game early on a wrong answer

**Future improvements**
- Move questions/prizes into an external file (JSON/CSV) instead of hardcoding them in the script
- Guard the `input()` call against non-numeric answers (currently `int(input(...))` will crash on bad input)
- Add a "walk away with current winnings" option instead of all-or-nothing
- Shuffle question order and answer choices on each run

---

## 📇 Contact Book

**Concepts learned**
- Using nested dictionaries to model structured records (a contact with multiple fields) keyed by name
- Building a persistent menu-driven loop (`while True` + numbered choices) that runs until an explicit exit
- CRUD operations in practice: Create, Read (view/search), Update, Delete, all working off the same dictionary
- Case-insensitive substring search using `.lower()` and `in`

**Future improvements**
- Fix "View contact" and "Search contact" to read from the looked-up `contact` dictionary (e.g. `contact['age']`) instead of stale bare variables left over from earlier in the loop
- Fix the `if not found` check in Search, which currently runs inside the `for` loop and can print "No contact found" multiple times instead of once after checking everyone
- Persist contacts to a file (JSON/CSV) so data isn't lost when the program exits
- Validate that age/mobile are numeric before casting, and normalize names (e.g. `.strip()`) before comparing

---

## ☕ PyCafe (Cafe Management)

**Concepts learned**
- Using a dictionary to store structured data (item name → price)
- Checking membership with `in` to validate user input against known keys
- Using f-strings for dynamic output and an accumulator variable for running totals

**Future improvements**
- Allow unlimited items via a loop instead of hardcoding "item 1" and "item 2"
- Make the "add another item?" check case-insensitive
- Support quantities per item, not just single units

---

## 🕐 PyClock (Digital Clock)

**Concepts learned**
- Building a basic GUI with Tkinter (`Tk()`, `Label`, `pack()`)
- Formatting date/time strings with `strftime`
- Using `.after()` for non-blocking, event-driven scheduling instead of a blocking loop, keeping the GUI responsive

**Future improvements**
- Add a toggle between 12-hour and 24-hour format
- Add a stopwatch/timer mode
- Improve styling (themes, resizable window, digital-style font)

---

## 🏠 Rent Calculator

**Concepts learned**
- Taking multiple user inputs and type-casting with `int(input(...))`
- Doing arithmetic across several inputs to derive a computed value
- Using integer division (`//`) to split a total evenly among people

**Future improvements**
- Use float/decimal division so remainders aren't silently dropped
- Validate `persons > 0` before dividing, to avoid a `ZeroDivisionError`
- Support itemized/unequal splits instead of a flat even split

---

## ✂️ Rock, Paper, Scissors

**Concepts learned**
- Using the `random` module (`random.choice`) to simulate randomness
- Mapping out game rules in a docstring before writing code — planning like a truth table
- Structuring decision logic with nested `if`/`elif`/`else` chains

**Future improvements**
- Validate user input so a typo doesn't silently fall through every condition
- Add a score tracker across multiple rounds and a "play again?" loop
- Refactor the win/lose logic into a lookup table instead of long if/elif chains

---

## Requirements

External packages used across these projects:
- `PyPDF2` — PDF merging (PDFMerger)
- `qrcode` — QR code generation (QRCodeGenerator)
- `plyer` — cross-platform notifications (DrinkWaterReminder)

All other projects (Calculator, QuizApp, Contact Book, PyCafe, PyClock, Rent Calculator, Rock Paper Scissors) use only the Python standard library (`tkinter`, `random`, `time`, etc.).
