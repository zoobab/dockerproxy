#!/bin/bash
set -e
export FLASK_APP=dockerproxy.py
flask run
