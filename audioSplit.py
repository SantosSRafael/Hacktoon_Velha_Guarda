from pydub import AudioSegment
import os
from lib import *

def separaAudio(audio_file):

    # Carrega o arquivo de áudio estéreo
    audio = AudioSegment.from_wav(audio_file)

    # Divide o áudio em canais esquerdo e direito
    left_channel = audio.split_to_mono()[0]
    right_channel = audio.split_to_mono()[1]

    # Extrai o nome do arquivo sem a extensão
    nome_arquivo = retornaNomeSemExtensao(audio_file)

    nomeArquivoCliente  = "temp/" + nome_arquivo + "_Cliente.wav"
    nomeArquivoOperador = "temp/" + nome_arquivo + "_Operador.wav"

    # Salva os canais esquerdo e direito como arquivos de áudio mono separados
    left_channel.export(nomeArquivoCliente,  format="wav")
    right_channel.export(nomeArquivoOperador, format="wav")

    retorno = [nomeArquivoCliente,nomeArquivoOperador]

    return retorno