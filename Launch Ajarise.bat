@echo off
setlocal
title Ajarise
set "AJARISE_DIR=%~dp0"
set "AJARISE_PYTHON=%AJARISE_DIR%.venv\Scripts\python.exe"

if exist "%AJARISE_PYTHON%" goto check_dependencies
echo Setting up the Python environment...
py -3.11 -m venv "%AJARISE_DIR%.venv" 2>nul
if not errorlevel 1 goto install_dependencies
python -m venv "%AJARISE_DIR%.venv"
if errorlevel 1 goto setup_failed

:install_dependencies
"%AJARISE_PYTHON%" -m pip install -r "%AJARISE_DIR%requirements.txt"
if errorlevel 1 goto setup_failed
"%AJARISE_PYTHON%" -B -c "import customtkinter, CTkMessagebox, psycopg, PyQt5.QtWebEngineWidgets, markdown_it, tkinterweb" >nul 2>&1
if errorlevel 1 goto setup_failed
goto launch

:check_dependencies
"%AJARISE_PYTHON%" -B -c "import customtkinter, CTkMessagebox, psycopg, PyQt5.QtWebEngineWidgets, markdown_it, tkinterweb" >nul 2>&1
if errorlevel 1 goto install_dependencies
:launch
start "" /d "%AJARISE_DIR%" "%AJARISE_DIR%.venv\Scripts\pythonw.exe" -B "%AJARISE_DIR%main.py"
exit /b 0

:setup_failed
echo.
echo Setup failed. Install Python 3.11 (64-bit) and check your internet connection.
echo Then run this launcher again.
pause
exit /b 1
