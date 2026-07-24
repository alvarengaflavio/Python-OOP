"""
    ============================================================================================================
                                        Python Object-Oriented Programming
                                Property Decorators - Getters, Setters, and Deleters
    ============================================================================================================
"""
"""
    Se na nossa classe Employee nós criarmos o Objeto emp_1 = Employee('Usuário', 'Teste') e em seguida
    alterarmos o valor do atributo emp_1.first = 'Jim', seu atributo será devidamente alterado porém o email
    que é um atributo criado pelo método __init__ matém-se com o valor inicial 'Usuário', ou seja 
    print(emp_1.first) >>> Jim
    print(emp_1.email) >>>  usuário.teste@email.com (não tem Jim aqui).
    Já o Método nome_completo() retorna o valor atualizado pois busca o valor atual do atributo na instância quando 
    é acionado. 
    
    Por mais que o primeiro pensamento seja "Opa! Então é só criar um método que gera o e-mail e pronto. Toda vez que o 
    e-mail for chamado e estará atualizdo", mas o problema com essa implementação é que ela quebraria o código com todos
    os outros objetos que já utilizam essa classe. E é aqui que os usuários de outras linguagens (Java) trariam 
    à tona os benefícios dos métodos getters e setters, porém nós temos a habilidade de fazer isso em Python
    utilizando Property Decorator. 
    
    ************************************************** Property Decorator **********************************************
    Ele nos permite definir um método para que possamos acessar coisas como um atributo por exemplo. 
    Continuando na classe Employee, vamos alterar o atributo email e transformar num método que criar a retorna a string
    com o e-mail do funcionário quando é chamada, isso supostamente quebraria o código para os funcionários já criados
    antes dessa implementação, para para contornar esse problema basta marcar o método e-mail com um @property
    na linha anterior à sua implementação. Com essa simples mudança o método e-mail pode ser acessado como se fosse um 
    atributo da classe Employee. 
    
    Property == getter
"""


class Employee:

    def __init__(self, first, last):
        self.first = first.title()
        self.last = last.title()

    def nome_completo(self):
        return f'{self.first} {self.last}'

    @property
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@email.com'


emp_1 = Employee('Usuário', 'Teste')

emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.nome_completo())

"""
    ************************************************** SETTERS ********************************************************
    Digamos que queremos poder alterar o nome completo de um funcionário  chamando emp_1.nome_completo = 'Flavio Alvarenga'
    E ao settar esse nome_completo os atributos first and last, consequentemente o email também devem ser alterados. 
     
    Com setter nós podemos fazer isso. Primeiro marcamos o método nome_completo com @property, em seguida marcamos
    um decorador com o nome da função complementado por .setter, ou seja, @fullname.setter, abaixo desse decorador nós
    iremos definir outro método com o mesmo nome. Esse método irá settar o novo nome para o objeto através do mesmo 
    valor de atributo da função que imprime o nome completo. Exemplo:  
    
    Recebendo: emp_1.nome_completo = 'Flavio Alvarenga', o método altera usuário teste para Flavio Alvarenga em todo o objeto. 
"""


class Employee:

    def __init__(self, first, last):
        self.first = first.title()
        self.last = last.title()

    @property
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@email.com'

    @property
    def nome_completo(self):
        return f'{self.first} {self.last}'

    @nome_completo.setter
    def nome_completo(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


emp_1 = Employee('Usuário', 'Teste')

emp_1.nome_completo = 'Flavio Alvarenga'

print(emp_1.first)
print(emp_1.email)
print(emp_1.nome_completo)


"""
    ************************************************** DELETER ********************************************************
    Digamos que queremos deletar o nome completo pra poder ter um código limpo. 
    No caso da classe que estamos usando como exemplo, vamos copiar o método nome_completo e colocar o decorador
    >>>   @nome_completo.deleter   <<< Que não aceitará nenhum outro valor além de si e removerá os valores dos 
    atributos first e last.
    Vamos criar o deleter aqui abaixo. 
"""


class Employee:

    def __init__(self, first, last):
        self.first = first.title()
        self.last = last.title()

    @property
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@email.com'

    @property
    def nome_completo(self):
        return f'{self.first} {self.last}'

    @nome_completo.deleter
    def nome_completo(self):
        print('Nome Deletado!')
        self.first = None
        self.last = None

    @nome_completo.setter
    def nome_completo(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


emp_1 = Employee('Usuário', 'Teste')
print(emp_1.nome_completo)

del emp_1.nome_completo
print(emp_1.nome_completo)
