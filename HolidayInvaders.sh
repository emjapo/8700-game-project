#!/bin/bash

# Define the virtual environment folder
VENV_DIR="venv"

# Create the virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv "$VENV_DIR"
    echo "Virtual environment created."
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"
echo "Virtual environment activated."

# Check if pygame is installed
if ! python3 -c "import pygame" &>/dev/null; then
    echo "pygame is not installed. Installing pygame..."
    python3 -m pip install pygame
    echo "pygame installed."
else
    echo "pygame is already installed."
fi

# Run the Python script
echo "Running HolidayInvaders..."
python3 main.py

