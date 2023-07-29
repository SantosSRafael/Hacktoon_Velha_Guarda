from azureLib import *
from lib import *



def principal():
    limpaDiretorio()

    cOperador =  '1'
    cCliente  =  '1'
    audio_filename = "TesteEsterio.wav"

    arquivosSeparados = separaAudio(audio_filename)
    
    transcricaoCliente  = transcreveAudio(arquivosSeparados[0])
    transcricaoOperador = transcreveAudio(arquivosSeparados[1])

    insereTranscricao(cOperador,cCliente,transcricaoOperador,transcricaoCliente)
    
principal()