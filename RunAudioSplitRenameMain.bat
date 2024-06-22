@echo off
REM 環境変数の設定
setlocal

REM Pythonのパスを確認する
where python
if %errorlevel% neq 0 (
    echo Pythonのパスが見つかりません。
    pause
    exit /b %errorlevel%
)


call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo 仮想環境のアクティブ化に失敗しました。
    pause
    exit /b %errorlevel%
)



python AudioSplitRenameMain.py
if %errorlevel% neq 0 (
    echo 音声ファイル分割・文字起こ・ファイルリネームツールの起動に失敗しました。
    pause
    exit /b %errorlevel%
)


