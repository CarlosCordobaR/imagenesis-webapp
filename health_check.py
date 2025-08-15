#!/usr/bin/env python3
"""
Health check endpoint for Render
"""
import requests
import sys
import os

def health_check():
    try:
        port = os.environ.get('PORT', 5000)
        url = f"http://localhost:{port}/"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("✅ Health check passed")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

if __name__ == "__main__":
    if health_check():
        sys.exit(0)
    else:
        sys.exit(1)
