#!/bin/sh
.venv/bin/python -m cProfile -o /tmp/prof "$1"
.venv/bin/python dumpprof.py /tmp/prof