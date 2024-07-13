import subprocess
from pathlib import Path
from pathlib import WindowsPath
import os
import time
from collections import deque
from typing import Generator

AUDIO_SPLITTER_EXEPATH = "audio_splitter.exe"
KOTOBA_WHISPER_DIR = "kotoba-whisper"
TMP_DIRPATH = "./tmp"

def split_audio_generator(audio_path:WindowsPath, min_silence_len=500, silence_thresh=-40, keep_silence=300) -> Generator[int, None, None]:
    # make directory
    Path(TMP_DIRPATH).mkdir(exist_ok=True, parents=True)
    # execute
    cmd = [AUDIO_SPLITTER_EXEPATH,"-i", str(audio_path.absolute()),"--min-silence-duration",f'"{min_silence_len}"',f"-t={silence_thresh}", "-o", TMP_DIRPATH]
    
    print("無音区間で分割...")
    p = subprocess.Popen("cmd /c start "+' '.join(cmd),stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    
    time.sleep(1)
    prev_list = []
    queue = deque()
    
    current_list = get_wavfile_path_list("tmp/16kHz")
    while True:
        # リストBの要素をセットに変換して高速に検索できるようにする
        set_prev = set(prev_list)

        # リスト内包表記を使ってリストCを作成
        diff = [item for item in current_list if item not in set_prev]
        if len(diff) != 0:
            queue.extend(diff)
        elif len(queue) == 0:
            break
            
        yield queue.popleft()
        
        prev_list = current_list
        current_list = get_wavfile_path_list("tmp/16kHz")
        
        

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
    chunks = split_audio_generator("./input_wav/test.wav")
    print(chunks)
    