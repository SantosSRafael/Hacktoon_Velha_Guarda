from azureLib import *
from lib import *

def principal():
    while True:
        retornaFila  = sqlRetornaFila()

        if len(retornaFila) > 0:
            cConversa  =  retornaFila["cConversa"].values[0]
            audioUrl  =  retornaFila["audioUrl"].values[0]

            limpaDiretorio()

            arquivosSeparados = separaAudio(audioUrl)
            
            transcricaoCliente  = transcreveAudio(arquivosSeparados[0])
            transcricaoOperador = transcreveAudio(arquivosSeparados[1])

            falaUnidas = juntaFalas(transcricaoCliente,transcricaoOperador)

            for fala in falaUnidas:
                locutor     = fala[3]
                texto       = fala[0]
                inicioFala  = fala[1]
                fimFala     = fala[2]

                insereTranscricao(cConversa,locutor,texto,inicioFala,fimFala)
        else:
            pass

        time.sleep(60)

principal()