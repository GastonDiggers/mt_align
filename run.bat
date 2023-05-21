@echo off

echo Installing requirements...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo Running the script...
python form.py

pause
