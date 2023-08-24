from azureLib import *
from lib import *
import warnings
warnings.filterwarnings("ignore")

def principal():
    while True:
        
        retornaFila  = sqlRetornaFila()

        if len(retornaFila) > 0:
            print('Inicia Fila de Processamento')
            cConversa  =  retornaFila["cConversa"].values[0]
            audioUrl  =  retornaFila["audioUrl"].values[0]

            limpaDiretorio()

            arquivosSeparados = separaAudio(audioUrl)
            
            print('Inicia Transcrição Cliente')
            transcricaoCliente  = transcreveAudio(arquivosSeparados[0])
            print('Finaliza Transcrição Chamada Cliente')

            print('Inicia Transcrição Chamada Operador')
            transcricaoOperador = transcreveAudio(arquivosSeparados[1])
            print('Finaliza Transcrição Chamada Operador')

            print('Junta Falas')
            falaUnidas = juntaFalas(transcricaoCliente,transcricaoOperador)


            print('Insere Trancrição Banco')
            for fala in falaUnidas:
                locutor     = fala[3]
                texto       = fala[0]
                inicioFala  = fala[1]
                fimFala     = fala[2]

                
                insereTranscricao(cConversa,locutor,texto,inicioFala,fimFala)
                
            print('Verifica Chamada API')
            verificaChamada(cChamada=cConversa)
                        
        else:
            print('Sem Arquivos Para Processar')

            retornaFilaAnalise  = sqlRetornaFilaAnalise()
            
            if len(retornaFilaAnalise) > 0:
                print('Analisando Falas')
                cConversaAnalise  =  retornaFilaAnalise["cChamada"].values[0]
                verificaChamada(cChamada=cConversaAnalise)
            else:
                print('Sem Fala a Serem Analisadas')
            
            pass

        time.sleep(15)

principal()