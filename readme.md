# IPO Application Automator

## Overview

This project automates the process of applying to IPOs on the MeroShare platform. Given a list of applicants, it logs in on their behalf, navigates to the IPO application page, lists open IPOs, and allows applying for selected IPOs automatically.

The project is built using **Python** and **Selenium WebDriver**, enabling automated browser interactions.

---

## Features

- Load applicant data from CSV or string input  
- Automated login for multiple applicants  
- Navigate to the "Apply for Issue" section of MeroShare  
- List all currently open IPOs with clickable options  
- Automate IPO application by filling required details and submitting  
- Take screenshots at key steps for debugging and verification  
- Robust error handling with logs and screenshots on failure

---

## Project Structure

```plaintext
ipo-alert/
├── data/                # Contains applicant CSV files  
├── screenshots/         # Automatically saved screenshots during runs  
├── src/                 # Source code organized by functionality  
│   ├── login.py         # Handles login flow  
│   ├── navigation.py    # Functions for navigating MeroShare pages  
│   ├── ipo.py           # IPO-specific actions like listing and applying  
│   ├── utils.py         # Utility functions (CSV loader, screenshot, etc.)  
│   └── main.py          # Entry point that runs the workflow  
├── requirements.txt     # Python dependencies  
├── .gitignore           # Ignore files/folders like screenshots, __pycache__  
└── README.md            # This documentation file  

---

## How to run

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/ipo-alert.git
cd ipo-alert

### 02. Create and activate a virtual environment

```python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

### 03.  Install dependencies

```pip install -r requirements.txt

### 04.  Prepare applicant data

Add your applicants CSV file (with real or test data) inside the data/ folder as applicants.csv.

Note: This file is gitignored, so it won’t be uploaded accidentally.

### 05.  Run the automation

```python src/main.py```
