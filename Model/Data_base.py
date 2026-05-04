import mysql.connector

class Data_base:
    def __init__(self):
# configura o acesso ao servidor MYSQL        
        self.__host = 'localhost'
        self.__user = 'root'
        self.__password = 'root'
# Estabelece a ligação com o servidor MYSQL com as cardenciais acima       
        self.__db = mysql.connector.connect(host=self.__host, user=self.__user, password=self.__password)
# O cursor é o que nos permite "escrever" e executar comandos SQL no python        
        self.__cursor = self.__db.cursor()


# Executa o comando SQL para criar a base de dados no servidor
    def criar_bd(self):
        self.__cursor.execute('CREATE DATABASE marketing_publicidade;')

