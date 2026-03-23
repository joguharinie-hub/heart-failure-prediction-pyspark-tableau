#!/bin/bash

echo "Setting up environment..."

# Create virtual environment
python3 -m venv venv

# Activate environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install pyspark pandas scikit-learn

echo "Environment setup complete!"
