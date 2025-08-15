#!/bin/bash
set -o errexit
echo "==> Upgrading pip..."
python -m pip install --upgrade pip
echo "==> Installing dependencies..."
pip install -r requirements.txt
echo "==> Build completed successfully!"
