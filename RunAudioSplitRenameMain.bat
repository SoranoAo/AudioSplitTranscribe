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


call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo ���z���̃A�N�e�B�u���Ɏ��s���܂����B
    pause
    exit /b %errorlevel%
)



python AudioSplitRenameMain.py
if %errorlevel% neq 0 (
    echo �����t�@�C�������E�����N���E�t�@�C�����l�[���c�[���̋N���Ɏ��s���܂����B
    pause
    exit /b %errorlevel%
)


