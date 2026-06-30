# Multi-Source Candidate Data Transformer

## Overview

Transforms structured and unstructured candidate data into one canonical candidate profile.

## Features

- Parse CSV recruiter data
- Parse GitHub JSON profile
- Merge candidate information
- Normalize phones
- Normalize skills
- Calculate confidence score
- Generate JSON output

## Project Structure

config/
docs/
input/
output/
src/
tests/

main.py

## Requirements

Python 3.10+

pandas

## Install

pip install -r requirements.txt

## Run

python main.py

Output is saved in

output/output.json
