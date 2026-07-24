# AI Assignment Assistant

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

**AI Assignment Assistant** is a simple desktop application built with **Python** and **Tkinter** that helps students quickly generate assignment content using information from **Wikipedia**. The application fetches a topic summary from Wikipedia, displays it in an easy-to-read format, and allows users to save the generated content as a PDF document.

This project is designed for educational purposes and demonstrates the integration of:

- Python GUI development using Tkinter
- Wikipedia API for information retrieval
- PDF generation using ReportLab

> **Note:** The generated content is sourced from Wikipedia and should be reviewed before submitting it as an academic assignment.

---

## Features

- 📚 Search any topic from Wikipedia
- 📝 Automatically generate a summarized answer
- 🔗 Displays the original Wikipedia reference link
- 📄 Export the generated answer as a PDF
- 🖥️ Simple and user-friendly graphical interface
- ⚡ Lightweight and easy to use

---

## Technologies Used

- Python 3
- Tkinter
- Wikipedia Python Library
- ReportLab

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/uttaran-cut/Draftora
```

Move into the project directory:

```bash
cd Draftora
```

### Step 2: Create a Virtual Environment (Recommended)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---


### Step 3: Run the Application

```bash
python main.py
```

The GUI window will open.

---

## How to Use

1. Launch the application.
2. Enter a topic in the text box.
3. Click **Generate Answer**.
4. The application fetches the topic summary from Wikipedia.
5. Review the generated content.
6. Click **Save as PDF** to export the answer.

---

## Example

### Input

```
Artificial Intelligence
```

### Output

```
Topic: Artificial Intelligence

Answer:
Artificial intelligence (AI) is intelligence demonstrated by machines...

Reference:
https://en.wikipedia.org/wiki/Artificial_intelligence
```

---

## Dependencies

- Python 3.8 or higher
- Tkinter (usually included with Python)
- wikipedia
- reportlab

---

## Installing Dependencies Individually

```bash
pip install wikipedia
pip install reportlab
```

---

## requirements.txt

Create a file named `requirements.txt` containing:

```txt
wikipedia
reportlab
```

Then install everything with:

```bash
pip install -r requirements.txt
```

---

## Future Improvements

- Support multiple information sources
- AI-based answer generation
- Citation generation (APA, MLA, IEEE)
- Grammar correction
- Multiple language support
- DOCX export
- Dark mode
- Search history
- Offline document support
- AI summarization using LLMs

---

## Limitations

- Requires an active internet connection.
- Information depends on Wikipedia availability.
- Some topics may have ambiguous names.
- Generated answers should be verified for academic use.

---

## License

This project is licensed under the **MIT License**.

---

## Acknowledgements

- Python
- Tkinter
- Wikipedia Python Library
- ReportLab
- Wikipedia Contributors

---

## Disclaimer

This application is intended **only for educational purposes**. The generated content is retrieved from Wikipedia and may not always be complete or academically appropriate. Users are encouraged to verify the information and cite the original sources when preparing assignments.
