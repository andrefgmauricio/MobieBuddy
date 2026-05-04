import mysql.connector

class Data_base:
    def __init__(self):
        self.__host = 'localhost'
        self.__user = 'root'
        self.__password = 'root'
        self.__db = mysql.connector.connect(host=self.__host, user=self.__user, password=self.__password)
        self.__cursor = self.__db.cursor()

    def criar_bd(self):
        self.__cursor.execute('CREATE DATABASE marketing_publicidade;')

        