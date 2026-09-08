# csv-cleaner-python
# CSV Cleaner (Python)

Clean messy CSV exports in one command: normalize column names, drop empty rows, remove duplicates, and standardize dates.

## What it does

- `"Email Address "` -> `email_address`
- `N/A`, `None`, `nan`, `-` -> empty
- Skips fully empty rows
- Removes duplicate rows
- Converts `2026/01/05` or `01/05/2026` -> `2026-01-05`

## Usage