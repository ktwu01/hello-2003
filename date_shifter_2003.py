#!/usr/bin/env python3
from datetime import datetime, timedelta
import re

def shift_date(date_str, days_to_shift):
    """Shift a date string by the specified number of days."""
    try:
        # Parse the date
        date_obj = datetime.strptime(date_str.strip(), '%Y-%m-%d')
        # Add the shift
        shifted_date = date_obj + timedelta(days=days_to_shift)
        # Return formatted date
        return shifted_date.strftime('%Y-%m-%d')
    except ValueError:
        # If it's not a valid date, return the original string
        return date_str

def process_file(input_file, output_file, shift_days):
    """Process the input file and write shifted dates to output file."""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regular expression to match YYYY-MM-DD format
    date_pattern = r'\d{4}-\d{2}-\d{2}'
    
    # Replace all dates with shifted dates
    shifted_content = re.sub(date_pattern, lambda match: shift_date(match.group(), shift_days), content)
    
    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(shifted_content)
    
    print(f"Processing complete!")
    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")
    print(f"Shift amount: {shift_days} days")

if __name__ == "__main__":
    # Calculate shift amount
    start_date = datetime(2003, 1, 10)
    end_date = datetime(2003, 3, 31)
    shift_days = (end_date - start_date).days
    
    print(f"Shift amount: {shift_days} days")
    print(f"Baseline: 2003-01-10 → {(start_date + timedelta(days=shift_days)).strftime('%Y-%m-%d')}")
    
    # Process the file
    input_file = "hello-2 copy.md"
    output_file = "hello-2_shifted.md"
    
    process_file(input_file, output_file, shift_days) 