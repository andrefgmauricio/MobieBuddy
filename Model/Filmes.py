class Filmes:
    def __init__(self,id, titulo, genero, ano, realizador):
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__ano = ano
        self.__realizador = realizador


    @property
    def id(self):
        return self.__id
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def genero (self):
        return self.__genero
    
    @property
    def ano (self):
        return self.__ano
    
    @property
    def realizador (self):
        return self.__realizador
    
    
        


