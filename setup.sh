#!/usr/bin/env bash
set -e

echo "Setting up bookbot data..."
mkdir -p books

download_book() {
    local filename="$1"
    local url="$2"

    if [ ! -f "books/$filename" ]; then
        echo "Downloading $filename..."
        wget -O "books/$filename" "$url"
    else
        echo "books/$filename already exists, skipping."
    fi
}

download_book "frankenstein.txt" "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/frankenstein.txt"

echo "Done."
