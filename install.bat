@echo off
REM env variable setting
setlocal

REM check Python path
where python
if %errorlevel% neq 0 (
    echo "Error. Python path not found"
    pause
    exit /b %errorlevel%
)


REM create Python 3.8.10 env
python -m venv venv
if %errorlevel% neq 0 (
    echo "Error. Failed create Python env"
    pause
    pause
    exit /b %errorlevel%
)

REM venv active
call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo "Error. Failed active venv"
    pause
    exit /b %errorlevel%
)

REM lib install from requirements.txt
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo "Error. Failed lib install"
    pause
    exit /b %errorlevel%
)

mkdir input_wav
mkdir output_wav

echo "complite install!!"
endlocal
pause
