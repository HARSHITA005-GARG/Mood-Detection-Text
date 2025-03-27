#!/bin/bash
apt-get update && apt-get install -y portaudio19-dev
python3 -m venv /opt/venv
source /opt/venv/bin/activate
pip install -r requirements.txt
