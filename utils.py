import subprocess
from pathlib import Path
from pathlib import WindowsPath
import wave
import numpy as np
import os
import urllib.request
from tqdm import tqdm

AUDIO_SPLITTER_EXEPATH = "audio_splitter.exe"
KOTOBA_WHISPER_DIR = "kotoba-whisper"
TMP_DIRPATH = "./tmp"

def split_audio_on_silence(audio_path:WindowsPath, min_silence_len=500, silence_thresh=-40, keep_silence=300):
    # make directory
    Path(TMP_DIRPATH).mkdir(exist_ok=True, parents=True)
    # execute
    cmd = [AUDIO_SPLITTER_EXEPATH,"-i", str(audio_path.absolute()),"--min-silence-duration",f'"{min_silence_len}"',f"-t={silence_thresh}", "-o", TMP_DIRPATH]
    p = subprocess.Popen(' '.join(cmd),stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    out, err = p.communicate()
    print(out)
    
    wavfile_path_list = get_wavfile_path_list("tmp/16kHz")
    
    return wavfile_path_list

def get_wavfile_path_list(directory) -> WindowsPath:
    # 指定されたディレクトリ内の全ファイルとディレクトリのリストを取得
    files = os.listdir(directory)
    # .wavファイルのみをフィルタリング
    wav_files = [(Path(directory) / Path(file)) for file in files if file.endswith('.wav')]
    # ファイル名でソート
    wav_files.sort()
    
    return wav_files

if __name__ == "__main__":
    print(Path(AUDIO_SPLITTER_EXEPATH).resolve())
    chunks = split_audio_on_silence("./input_wav/test.wav")
    print(chunks)
    