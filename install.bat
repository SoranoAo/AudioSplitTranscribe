@echo off
REM ���ϐ��̐ݒ�
setlocal

REM Python�̃p�X���m�F����
where python
if %errorlevel% neq 0 (
    echo Python�̃p�X��������܂���B
    pause
    exit /b %errorlevel%
)


REM Python 3.8.10�̉��z�����쐬
python -m venv venv
if %errorlevel% neq 0 (
    echo ���z���̍쐬�Ɏ��s���܂����B
    pause
    pause
    exit /b %errorlevel%
)

REM ���z�����A�N�e�B�u��
call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo ���z���̃A�N�e�B�u���Ɏ��s���܂����B
    pause
    exit /b %errorlevel%
)

REM requirements.txt���烉�C�u�������C���X�g�[��
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ���C�u�����̃C���X�g�[���Ɏ��s���܂����B
    pause
    exit /b %errorlevel%
)

mkdir input_wav
mkdir output_wav

echo ���z���̐ݒ肪�������܂����I
endlocal
pause
