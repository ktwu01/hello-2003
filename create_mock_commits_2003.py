#!/usr/bin/env python3
import subprocess
import os
from datetime import datetime

def create_mock_commits():
    """Create mock commits for each date in 2003"""
    
    # Parse dates directly from the markdown file
    import re
    
    with open("hello-2003.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Find all YYYY-MM-DD patterns
    date_pattern = r'\d{4}-\d{2}-\d{2}'
    matches = re.findall(date_pattern, content)
    
    # Convert to datetime objects and sort
    dates = []
    for date_str in matches:
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            dates.append(date_obj)
        except ValueError:
            print(f"Invalid date format: {date_str}")
    
    # Remove duplicates and sort
    unique_dates = sorted(list(set(dates)))
    
    print(f"Creating commits for {len(unique_dates)} dates...")
    
    for i, date_obj in enumerate(unique_dates):
        date_str = date_obj.strftime('%Y-%m-%d')
        
        # Create a simple file with the date as content
        filename = f"activity_{date_str}.txt"
        
        with open(filename, "w") as f:
            f.write(f"Activity for {date_str}\n")
            f.write(f"This file represents activity on {date_str}\n")
            f.write(f"Created to show contribution on GitHub\n")
        
        # Add file to git
        subprocess.run(["git", "add", filename], check=True)
        
        # Create commit with custom date
        # Format: YYYY-MM-DD HH:MM:SS
        commit_date = f"{date_str} 12:00:00"
        commit_message = f"Add activity for {date_str}"
        
        subprocess.run([
            "git", "commit", 
            "--date", commit_date,
            "-m", commit_message
        ], check=True)
        
        print(f"Created commit {i+1}/{len(unique_dates)} for {date_str}")
    
    print(f"\n✅ Created {len(unique_dates)} mock commits!")
    print("You can now push this repository to GitHub to see the green squares.")

if __name__ == "__main__":
    create_mock_commits() 