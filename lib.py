import neocript
import configparser
import pyodbc
import pandas as pd
from sqlalchemy import create_engine
import os
import sys

config = configparser.ConfigParser()

# Le o arquivo config.
with open(r"config.ini"):
    config.read(r"config.ini")

# Laço para pegar todas os itens e sessoes no arquivo.
for s in config.sections():
    for i in config[s]:
        config[s][i] = config.get(s, i)

Server              = config["CONEXAO"]["Server"]
Database            = neocript.Descriptografa(config["CONEXAO"]["Database"])
User                = neocript.Descriptografa(config["CONEXAO"]["User"])
Password            = neocript.Descriptografa(config["CONEXAO"]["Password"])

RetornaConfigAPI          = neocript.Descriptografa(config["PROCS"]["RetornaConfigAPI"])
RetornaFila               = neocript.Descriptografa(config["PROCS"]["RetornaFila"])
InsereTranscricaoConversa = neocript.Descriptografa(config["PROCS"]["InsereTranscricaoConversa"])


def retornaNomeSemExtensao(audio_file):
    return os.path.splitext(audio_file)[0]

def insereTranscricao(cConversa,locutor, texto, inicioFala, fimFala):
    conn = pyodbc.connect(
        "DRIVER={SQL Server Native Client 11.0};"
        "Server=" + Server + ";"
        "Database=" + Database + ";"
        "uid=" + User + ";"
        "pwd=" + Password + ""
    )
   
    # falaOperador = '; '.join(falaOperador) # str(falaOperador).replace("'","_")
    # falaCliente  = '; '.join(falaCliente) # str(falaCliente).replace("'","_")

    sql = f"exec {InsereTranscricaoConversa} '{cConversa}','{locutor}','{texto}','{inicioFala}','{fimFala}'"

    # print(sql)

    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    # Fechar a conexão com o banco de dados
    conn.close()

def limpaDiretorio():
    
    caminho_atual = retornaDiretorioLocal()
    novo_caminho = os.path.join(caminho_atual, "temp")
    try:

        if not os.path.exists(novo_caminho):
            os.mkdir(novo_caminho)
        else:
            # verificar se há arquivos na pasta e excluí-los
            for root, dirs, files in os.walk(novo_caminho):
                for arquivo in files:
                    caminho_arquivo = os.path.join(root, arquivo)
                    os.remove(caminho_arquivo)
                    #print(f"O arquivo '{arquivo}' foi excluído de '{novo_caminho}'.")
    except Exception as e:
        pass
        # insereLog('0',"Falha no processo de limpar diretorio: " + str(e))

def retornaDiretorioLocal():
    return str(os.path.dirname(os.path.realpath(sys.argv[0])))

def sqlRetornaConfigAPI():
    # insereLog("Inicia - Retona Config API")
    try:
        conn = pyodbc.connect(
            "DRIVER={SQL Server Native Client 11.0};"
            "Server=" + Server + ";"
            "Database=" + Database + ";"
            "uid=" + User + ";"
            "pwd=" + Password + ""
        )
    
        sql = "exec " + RetornaConfigAPI

        try:
            data = pd.read_sql_query(sql, conn)
        except:
            data = pd.DataFrame()

        conn.close()
    except Exception as e:
        pass
    #     insereLog("Falha no retorno de config API: " + str(e))
    
    # insereLog("Finaliza - Retorna Config API")
    return data

def sqlRetornaFila():
    # insereLog("Inicia - Retona Config API")
    try:
        conn = pyodbc.connect(
            "DRIVER={SQL Server Native Client 11.0};"
            "Server=" + Server + ";"
            "Database=" + Database + ";"
            "uid=" + User + ";"
            "pwd=" + Password + ""
        )
    
        sql = "exec " + RetornaFila

        try:
            data = pd.read_sql_query(sql, conn)
        except:
            data = pd.DataFrame()

        conn.close()
    except Exception as e:
        pass
    #     insereLog("Falha no retorno de config API: " + str(e))
    
    # insereLog("Finaliza - Retorna Config API")
    return data

def juntaFalas(falaCliente, falaOperador):

    # Combinação dos arrays
    array_combinado = falaCliente + falaOperador

    # Ordenar o array pelo tempo de início
    array_combinado.sort(key=lambda x: x[1])

    # Adicionar o tipo de fala a cada linha
    for linha in array_combinado:
        # Verificar se a linha pertence ao array do Cliente ou do Operador
        if linha in falaCliente:
            linha.append('Cliente')
        else:
            linha.append('Operador')

    falasProcessadas = []

    # Imprimir o array resultante
    for linha in array_combinado:
        falasProcessadas.append(linha)
        #print(linha)

    return falasProcessadas