# Automated Data Validation & Reporting Bot

A Python automation script that reads raw data, automatically checks it for
errors, cleans it, and generates a summary report — removing the need to
review and fix data by hand.

## What it does

1. **Reads data** from an Excel file (`raw_tickets.xlsx`)
2. **Checks for issues** automatically:
   - Missing values (blank issue type, blank status)
   - Invalid numbers (negative or unrealistic resolution times)
3. **Cleans the data** by removing the bad rows
4. **Builds a summary report** showing ticket counts by issue type
5. **Logs every run** to `automation_log.txt`, recording how many records
   were processed and what issues were found — similar to a basic
   monitoring system

## Why I built this

This project reflects the kind of work involved in application
maintenance and process automation — using automation to reduce manual
effort, catch data issues early, and produce ready-to-use reports without
someone doing it by hand each time.

## How to run it

1. Install the required libraries:
pip install pandas openpyxl
2. Generate sample data (or replace with your own Excel file):
python generate_data.py
3. Run the automation:
python automate_report.py
4. Check the results:
   - `automated_report.xlsx` — cleaned data + summary report
   - `automation_log.txt` — log of what the bot found and fixed

## Tech used

- Python
- Pandas
- OpenPyXL

## Automatic scheduling

This script can also be scheduled to run on its own every day (for
example, using `cron` on Mac or Task Scheduler on Windows) — so the
validation and reporting happen automatically without manual effort.