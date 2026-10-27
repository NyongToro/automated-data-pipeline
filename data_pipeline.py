"""
Data Pipeline & Verification Script
Author: Torobong Nyong (nyongtoro)
Description: Ingests raw data lists, cleans null values, calculates metrics,
             and outputs formatted tabular reports.
"""

import csv
import json

# Sample input dataset simulating raw uncleaned data
raw_records = [
    {"user_id": "101", "name": " Alice ", "status": "active", "scans": "12"},
    {"user_id": "102", "name": "Bob", "status": "INACTIVE", "scans": "0"},
    {"user_id": "103", "name": " Charlie", "status": "active", "scans": "45"},
    {"user_id": "104", "name": "David ", "status": "active", "scans": "None"},
]

def clean_and_process(data):
    processed = []
    total_scans = 0

    print("⚡ Starting Data Ingestion & Transformation...")
    
    for row in data:
        # Strip whitespace
        clean_name = row["name"].strip()
        status = row["status"].strip().lower()
        
        # Handle invalid numeric data
        try:
            scans = int(row["scans"])
        except ValueError:
            scans = 0

        total_scans += scans

        processed.append({
            "user_id": row["user_id"],
            "name": clean_name,
            "status": status,
            "scan_count": scans,
            "eligible": scans > 10 and status == "active"
        })

    summary = {
        "total_records_processed": len(processed),
        "total_scans_logged": total_scans,
        "processed_data": processed
    }
    
    return summary

if __name__ == "__main__":
    result = clean_and_process(raw_records)
    print("\n✅ Execution Complete! Processed Output Summary:\n")
    print(json.dumps(result, indent=2))