@setlocal enableextensions
@cd /d "%~dp0"
@echo start
pip install cryptography
pip install getmac
python "%CD%\main.py" 1 %CD%
@pause