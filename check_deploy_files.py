#!/usr/bin/env python3
"""
Script to check if all required files for Fly.io deployment are present
"""

import os
import sys

def check_file_exists(filepath):
    """Check if a file exists and print status"""
    if os.path.exists(filepath):
        print(f"✓ {filepath} - Found")
        return True
    else:
        print(f"✗ {filepath} - Missing")
        return False

def main():
    """Main function to check all required deployment files"""
    print("Checking Fly.io deployment files...\n")
    
    required_files = [
        "Dockerfile",
        "fly.toml",
        "app.py",
        "requirements.txt",
        "models.py",
        "templates/index.html",
        "static/styles.css"
    ]
    
    all_good = True
    for file in required_files:
        if not check_file_exists(file):
            all_good = False
    
    print("\n" + "="*50)
    if all_good:
        print("✓ All required files for Fly.io deployment are present!")
        print("You can now run: flyctl deploy")
    else:
        print("✗ Some required files are missing.")
        print("Please check the missing files before deploying to Fly.io")
        sys.exit(1)

if __name__ == "__main__":
    main()