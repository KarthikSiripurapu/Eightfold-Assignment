# Multi-Source Candidate Data Transformer

## Overview

This project transforms structured and unstructured candidate data from multiple sources into a single canonical candidate profile.

---

## Features

- Parse recruiter CSV data
- Parse GitHub JSON profile
- Merge candidate information
- Normalize phone numbers
- Normalize skill names
- Calculate candidate confidence score
- Generate unified JSON output

---

## Project Structure

```
config/
docs/
input/
output/
src/
tests/
main.py
```

---

## Requirements

- Python 3.10+
- pandas

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python main.py
```

---

## Output

The generated candidate profile is saved to:

```
output/output.json
```
