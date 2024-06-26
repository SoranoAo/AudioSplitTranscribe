# 使い方

## Step0
Pythonのインストール

・WindowsのMicrosoft Storeを起動
・画面上部の検索バーからPythonを検索
・検索結果からPython 3.8をインストール
　※ほかのバージョンのPythonでも動作するかもしれませんが、3.8以外では動作確認していません。

ffmpegをインストールする。
ffmpegをダウンロードし、Windowsの場合はpathにffmpegへのパス設定を行ってください


## Step1
このリポジトリ内のソースファイルを任意の場所にclone。

git clone https://github.com/SoranoAo/AudioSplitTranscribe.git
もしくは、GithubページからZIPファイルとしてダウンロード

※ファイルパスがすべて半角英数字の場所に配置したほうがいいかもしれません。
　ファイルパス日本がが含まれると正常に動作しない可能性があります。（未検証）

## Step2
install.bat　を実行
「"complite install!!"」と表示されればOK

## Step3
input_wavのフォルダが作成されるのでそのファイルに処理対象WAVファイルを配置。
複数のWAVファイルを入れても問題ないです。

## Step4
RunAudioSplitRenameMain.bat を実行。
長いWavファイルの場合、処理に時間がかかります。

output_wavフォルダにinput_wavのフォルダに配置されたWavファイル内で無音区間がある部分で区切り、ファイルを分割する。
分割したファイルでの音声内容を文字起こしを実行し、ファイル名を文字起こしした内容の冒頭３０文字でリネーム。


# 設定
## 無音時間とみなす時間の設定
AudioSplitRenameMain.py　をメモ帳などで開き、下記の値を変更することで設定を変更できます。

変更場所
def split_audio_on_silence(audio_path, min_silence_len=3000, silence_thresh=-80, keep_silence=1000):

### 無音時間とみなす時間の設定
min_silence_len=3000　の 3000の部分を変更する

説明: 音声を分割する際に「無音」と見なす最小の無音区間の長さをミリ秒単位で指定します。この値以上の長さの無音区間が見つかった場合に、音声をその位置で分割します。
型: int
デフォルト値: 1000（1秒）

### 無音区間と扱う音量の設定
silence_thresh=-80　の -80の部分を変更する

説明: 無音を検出する際の閾値をデシベル単位で指定します。この値よりも音量が小さい区間を無音と見なします。通常、この値は音声ファイル全体の音量レベルに対して相対的に設定されます。
型: int
デフォルト値: -40（デシベル

WAV音声ファイルのbit数によって最小値が変わるようです。
音声ファイルが16ビットPCMの場合、最小値は-96デシベル（dB）です。これは16ビットオーディオのダイナミックレンジに対応します。
音声ファイルが8ビットPCMの場合、最小値は-48デシベル（dB）です。これは8ビットオーディオのダイナミックレンジに対応します。
通常、silence_threshは音声の平均音量よりも少し低い値に設定します。例えば、音声の平均音量が-20dB程度であれば、無音を検出するための閾値を-30dBから-40dBに設定することが一般的です。

### 出力ファイルに残す無音時間
keep_silence=1000

説明: 無音区間を分割後のチャンクの両端にどれだけ残すかをミリ秒単位で指定します。これにより、チャンクの開始と終了部分に少しの無音を残すことができます。
型: int
デフォルト値: 500（0.5秒）

# ライセンス
下記のオープンソースのソフトウエアを利用させていただいております。

## faster-whisper
https://github.com/SYSTRAN/faster-whisper

ライセンス
MIT License

Copyright (c) 2023 SYSTRAN

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.