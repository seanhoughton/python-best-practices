@echo off
.venv\scripts\python -m cProfile -o %TEMP%\prof "%1"
.venv\scripts\python dumpprof.py %TEMP%\prof