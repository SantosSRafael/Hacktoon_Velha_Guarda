from azureLib import *


speech_key      = "6424fc8703a443ab9b8bf97b97d3d73c"
service_region  = "brazilsouth"
language        = "pt-br"

audio_filename = "TesteEsterio.wav"

def principal():
    separaAudio(audio_filename)
    
    nomeArquivoCliente  = "temp/" + retornaNomeSemExtensao(audio_filename) + "_Cliente.wav"
    nomeArquivoOperador = "temp/" + retornaNomeSemExtensao(audio_filename) + "_Operador.wav"

    transcricaoCliente = transcreveAudio(speech_key,service_region,language,nomeArquivoCliente)

    transcricaoOperador = transcreveAudio(speech_key,service_region,language,nomeArquivoOperador)

    print("Cliente: ")
    print(transcricaoCliente)
    print("Operador: ")
    print(transcricaoOperador)

principal()