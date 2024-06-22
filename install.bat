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


REM Python 3.8.10の仮想環境を作成
python -m venv venv
if %errorlevel% neq 0 (
    echo 仮想環境の作成に失敗しました。
    pause
    pause
    exit /b %errorlevel%
)

REM 仮想環境をアクティブ化
call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo 仮想環境のアクティブ化に失敗しました。
    pause
    exit /b %errorlevel%
)

REM requirements.txtからライブラリをインストール
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ライブラリのインストールに失敗しました。
    pause
    exit /b %errorlevel%
)

mkdir input_wav
mkdir output_wav

echo 仮想環境の設定が完了しました！
endlocal
pause
