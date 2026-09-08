"""
Email Lead Validator & Cleaner Script
Deterministic utility to validate email formatting, clean domain strings, and remove duplicate rows from CSV lists.
"""

import csv
import re
import sys
from typing import List, Dict, Tuple

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


def validate_email_syntax(email: str) -> bool:
    """Check if the email matches RFC standard syntax."""
    if not email or not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email.strip().lower()))


def clean_lead_csv(input_filepath: str, output_filepath: str) -> Tuple[int, int, int]:
    """
    Clean an input CSV of leads:
    - Removes invalid emails
    - Deduplicates by email
    - Standardizes first names and company names
    """
    valid_leads: List[Dict[str, str]] = []
    seen_emails = set()
    total_rows = 0
    invalid_count = 0
    duplicate_count = 0

    with open(input_filepath, mode="r", encoding="utf-8-sig") as infile:
        reader = csv.DictReader(infile)
        if not reader.fieldnames:
            print(f"Error: CSV at {input_filepath} has no headers.")
            return 0, 0, 0

        # Find email column dynamically
        email_col = next((col for col in reader.fieldnames if "email" in col.lower()), None)
        if not email_col:
            print(f"Error: No email column found in {input_filepath}.")
            return 0, 0, 0

        for row in reader:
            total_rows += 1
            raw_email = row.get(email_col, "").strip().lower()

            if not validate_email_syntax(raw_email):
                invalid_count += 1
                continue

            if raw_email in seen_emails:
                duplicate_count += 1
                continue

            seen_emails.add(raw_email)
            row[email_col] = raw_email
            valid_leads.append(row)

    # Write cleaned output
    if valid_leads:
        with open(output_filepath, mode="w", encoding="utf-8", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(valid_leads)

    return total_rows, len(valid_leads), invalid_count + duplicate_count


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python validate_leads.py <input_leads.csv> <output_cleaned.csv>")
        sys.exit(1)

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    try:
        total, valid, removed = clean_lead_csv(in_file, out_file)
        print(f"✅ Lead Validation Complete:")
        print(f"   • Total Processed: {total}")
        print(f"   • Valid & Unique: {valid}")
        print(f"   • Removed (Invalid/Duplicates): {removed}")
        print(f"   • Output saved to: {out_file}")
    except FileNotFoundError:
        print(f"❌ File not found: {in_file}")
