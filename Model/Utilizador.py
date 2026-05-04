#class utilizador e o que precisa para a sua memoria
class Utilizador:
    def __init__(self, nome, email, password, id_utilizador=None):
        self.__nome = nome
        self.__email = email
        self.__password = password
        self.__id_utilizador = id_utilizador

#GET como é encapsulamento o get serve para devolver os valores quando forem chamados noutro lado
    @property
    def nome(self):
        return self.__nome
    @property
    def email(self):
        return self.__email
    @property
    def password(self):
        return self.__password
    @property
    def id_utilizador(self):
        return self.__id_utilizador

#SET é o unico atributo que tenha autorizaçao para serem feitas alterações no caso da necessidade de nova password    
    @password.setter
    def password(self, nova_password):
        self.__password = nova_password