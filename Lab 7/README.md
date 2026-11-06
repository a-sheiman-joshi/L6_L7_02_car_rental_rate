# Lab 7 — Fuzz Testing with Hypothesis

**Student:** PES2UG24CS003  
**Repository:** Lab7-FuzzTesting-PES2UG24CS003

## Overview
This submission hardens three input-processing functions and tests their behaviour with Hypothesis property-based tests.

## Files
- `processor.py` — fixed application.
- `test_processor.py` — Hypothesis property-based tests and regression tests.
- `requirements.txt` — test dependencies.
- `report/Lab7_FuzzTesting_Report.pdf` — lab report.
- `screenshots/` — terminal-output evidence captured while checking the starter and fixed implementations.
- `evidence/processor_buggy.py` — original starter implementation retained for comparison.

## Setup (Ubuntu/Linux)
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run the application
```bash
python processor.py
```

Example inputs:
- License plate: `KA-01_AB#1234`
- Mileage CSV: `100.5, 45.2, 80.0`
- Rental record: `Asha:2:SUV`

## Run tests
```bash
python -m pytest -v test_processor.py
```

## Input-handling decisions
- `sanitize_license_plate`: non-string input returns `""`; supported delimiters are removed and output is uppercased.
- `parse_trip_mileage`: empty or invalid input returns `[]`; malformed tokens, negative values, NaN and infinity reject the whole input.
- `format_rental_invoice`: invalid records return `"Invalid rental record"`; valid records require exactly three colon-separated fields, a non-empty driver/category and a positive integer day count.
- Original pricing logic is preserved: SUV = $50/day; all other categories = $30/day.

## Evidence note
The screenshots in this package show reproducible command output from the starter and fixed code paths. Hypothesis is a required dependency; run the command above on the submission machine to execute the generated property-based cases. Do not represent a local dependency/setup error as a passing Hypothesis run.
