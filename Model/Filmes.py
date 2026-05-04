# Classe Filmes: Define a estrutura e os atributos para a gestao de filmes
class Filmes:
# Metodo Construtor: Inicializa a "memoria" do objeto filme com os seus dados base    
    def __init__(self,id, titulo, genero, ano, realizador):
# Encapsulamento: Atributos privados para garantir a integridade da informacao
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__ano = ano
        self.__realizador = realizador


# Getters: Metodos para visualizar/aceder aos dados sem permitir alteracao direta
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
    
    
        


