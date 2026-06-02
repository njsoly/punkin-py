#!/usr/bin/env bash

source ../.venv/bin/activate
python -m pip install -r ../requirements.txt
python app.py

deactivate