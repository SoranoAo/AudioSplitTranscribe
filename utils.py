import subprocess
from pathlib import Path

AUDIO_SPLITTER_EXEPATH = "audio_splitter.exe"
TMP_DIRPATH = "./tmp"

def split_audio_on_silence(audio_path, min_silence_len=500, silence_thresh=-40, keep_silence=300):
    # make directory
    Path(TMP_DIRPATH).mkdir(exist_ok=True, parents=True)
    # execute
    cmd = [AUDIO_SPLITTER_EXEPATH,"-i", audio_path,"--min-silence-duration",f'"{min_silence_len}"',f"-t={silence_thresh}", "-o", TMP_DIRPATH]
    p = subprocess.Popen(' '.join(cmd),stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    out, err = p.communicate()
    print(out)
    return

if __name__ == "__main__":
    print(Path(AUDIO_SPLITTER_EXEPATH).resolve())
    split_audio_on_silence("./input_wav/test.wav")