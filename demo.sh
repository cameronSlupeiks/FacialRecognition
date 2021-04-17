#! /usr/bin/env bash

# SET COLOR VARS.
RED=`tput setaf 1`
GREEN=`tput setaf 2`
BLUE=`tput setaf 4`
RESET=`tput sgr0`

# SET LOG LEVELS.
INFO="${BLUE}[INFO]${RESET}"
ERROR="${RED}[ERROR]${RESET}"

# CHECK FOR VALID PYTHON INSTALLATION.
if ! hash python; then
    echo -e "${ERROR} Python is not installed."
    exit 1
fi

# CHECK FOR VALID PYTHON VERSION.
PYTHON_VERSION=$(python -V 2>&1 | sed 's/.* \([0-9]\).\([0-9]\).*/\1\2/')
if [ "$PYTHON_VERSION" -lt "38" ]; then
    echo -e "${ERROR} This script requires python v3.8.0 or greater."
    exit 1
fi

# INSTALL REQUIREMENTS.
echo -e "${INFO} Installing Requirements..."
pip3 install -r requirements.txt > /dev/null
echo -e "${INFO} ${GREEN}Requirements installation complete!${RESET}"

# RUN FACIAL ENCODER SCRIPT.
echo -e "${INFO} Starting facial encoder..."
python3 facial_encoder.py
echo -e "${INFO} ${GREEN}Facial encoding complete!${RESET}"

# RUN FACIAL RECOGNITION SCRIPT.
echo -e "${INFO} Starting facial recognition program..."
python3 facial_recognition.py
echo -e "${INFO} ${GREEN}Program terminated successfully!${RESET}"

exit 0