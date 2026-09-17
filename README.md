# Python Mini Projects

A collection of small Python practice projects, each focused on a different concept or use case.

## Repository Structure

```
python-mini-projects/
│
├── .vscode/
│   └── settings.json
│
├── Calculator/
│   └── main.py
│
├── DrinkWaterReminder/
│   └── main.py
│
├── PDFMerger/
│   ├── main.py
│   ├── merged-pdf.pdf
│   ├── pdf1.pdf
│   └── pdf2.pdf
│
├── QRCodeGenerator/
│   ├── main.py
│   └── youtube.png
│
├── QuizApp/
│   └── main.py
│
├── requirements.txt
└── README.md
```

## Projects

### 🧮 Calculator
A simple command-line calculator that performs basic arithmetic operations.

**Run:**
```bash
python Calculator/main.py
```

---

### 💧 DrinkWaterReminder
A script that reminds you to drink water at regular intervals.

**Run:**
```bash
python DrinkWaterReminder/main.py
```

---

### 📄 PDFMerger
Merges multiple PDF files into a single PDF using `PyPDF2`.

**Run:**
```bash
python PDFMerger/main.py
```

Includes sample files (`pdf1.pdf`, `pdf2.pdf`) and a sample output (`merged-pdf.pdf`) for demonstration.

---

### 🔗 QRCodeGenerator
Generates a QR code image from a given input (e.g. a URL) using the `qrcode` library.

**Run:**
```bash
python QRCodeGenerator/main.py
```

Includes a sample generated QR code (`youtube.png`).

---

### ❓ QuizApp
A terminal-based multiple-choice quiz game with a set of general knowledge questions and score tracking.

**Run:**
```bash
python QuizApp/main.py
```

## Requirements

See [`requirements.txt`](./requirements.txt) for external packages used across these projects:
- `PyPDF2` — PDF merging (PDFMerger)
- `qrcode` — QR code generation (QRCodeGenerator)
- `plyer` — cross-platform notifications (DrinkWaterReminder)