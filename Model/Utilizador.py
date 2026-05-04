# Classe Utilizador: Define a estrutura de dados para os utilizadores do sistema
class Utilizador:
# Metodo Construtor: O parametro id_utilizador=None permite criar um utilizador 
# que ainda nao existe na base de dados (o ID sera gerado pelo MySQL depois)    
    def __init__(self, nome, email, password, id_utilizador=None):
# Atributos com "__" sao privados (Encapsulamento), protegendo os dados de acessos diretos        
        self.__nome = nome
        self.__email = email
        self.__password = password
        self.__id_utilizador = id_utilizador

# @property (Getter): Permite ler o valor do atributo privado de forma segura
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

# @password.setter (Setter): Permite modificar o valor do atributo privado com seguranca
    @password.setter
    def password(self, nova_password):
        self.__password = nova_password