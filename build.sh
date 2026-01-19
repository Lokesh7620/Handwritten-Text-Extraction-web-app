#!/bin/bash
# Render.com Build Script
# Install system dependencies and Python packages

set -e  # Exit on error

echo "=== Starting Render.com Build ==="

# Install Python dependencies first
echo "Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.render.txt

echo "=== Build Complete ==="
