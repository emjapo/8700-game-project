#!/bin/bash

# Define the virtual environment folder
VENV_DIR="venv"
LOCAL_DIR="$HOME/local"  # Directory for local SDL2 installation

# Create the virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv "$VENV_DIR"
    echo "Virtual environment created."
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"
echo "Virtual environment activated."

# Ensure SDL2 libraries are installed locally
SDL2_VERSION="2.28.4"
SDL2_MIXER_VERSION="2.6.4"

# Function to build SDL2 from source
build_sdl2() {
    SDL_NAME=$1
    SDL_VERSION=$2
    SDL_URL=$3
    SDL_DIR=$SDL_NAME-$SDL_VERSION

    if [ ! -d "$SDL_DIR" ]; then
        echo "Downloading $SDL_NAME..."
        wget $SDL_URL -O $SDL_DIR.tar.gz
        tar -xvzf $SDL_DIR.tar.gz
    fi

    cd $SDL_DIR
    echo "Building $SDL_NAME..."
    ./configure --prefix=$LOCAL_DIR --with-sdl-prefix=$LOCAL_DIR
    make
    make install
    cd ..
}

# Ensure the local installation directory exists
mkdir -p $LOCAL_DIR

# Build and install SDL2
build_sdl2 "SDL2" $SDL2_VERSION "https://www.libsdl.org/release/SDL2-$SDL2_VERSION.tar.gz"
build_sdl2 "SDL2_mixer" $SDL2_MIXER_VERSION "https://www.libsdl.org/projects/SDL_mixer/release/SDL2_mixer-$SDL2_MIXER_VERSION.tar.gz"

# Update environment variables
export LD_LIBRARY_PATH=$LOCAL_DIR/lib:$LD_LIBRARY_PATH
export PKG_CONFIG_PATH=$LOCAL_DIR/lib/pkgconfig:$PKG_CONFIG_PATH

# Add these environment variables to .bashrc for persistence (optional)
if ! grep -q "export LD_LIBRARY_PATH=$LOCAL_DIR/lib" ~/.bashrc; then
    echo "export LD_LIBRARY_PATH=$LOCAL_DIR/lib:\$LD_LIBRARY_PATH" >> ~/.bashrc
fi

if ! grep -q "export PKG_CONFIG_PATH=$LOCAL_DIR/lib/pkgconfig" ~/.bashrc; then
    echo "export PKG_CONFIG_PATH=$LOCAL_DIR/lib/pkgconfig" >> ~/.bashrc
fi

# Check if pygame is installed
if ! python3 -c "import pygame" &>/dev/null; then
    echo "pygame is not installed. Installing pygame..."
    pip install pygame
    echo "pygame installed."
else
    echo "pygame is already installed."
fi

# Run the Python script
echo "Running main.py..."
python3 main.py

