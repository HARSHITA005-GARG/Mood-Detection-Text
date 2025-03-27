#!/bin/bash
apt-get update && apt-get install -y portaudio19-dev
python3 -m venv myenv
source myenv/Scripts/activate
pip install -r requirements.txt
