import cript.neocript as neocript
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

class Conexao_BD:
    def __init__(self):
        self.conn = pyodbc.connect(
            "DRIVER={SQL Server Native Client 11.0};"
            "Server=" + Server + ";"
            "Database=" + Database + ";"
            "uid=" + User + ";"
            "pwd=" + Password + ""
        )

    def execute_proc(self, procedure):  
        try:
            sql = f"exec {procedure}"

            # print(sql)

            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()

            # Fechar a conexão com o banco de dados
            self.conn.close()
        except Exception as e:
            self.conn.close()
            pass
        
        
    
       