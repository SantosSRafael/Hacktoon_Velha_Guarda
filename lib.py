import os

def retornaNomeSemExtensao(audio_file):
    return os.path.splitext(audio_file)[0]