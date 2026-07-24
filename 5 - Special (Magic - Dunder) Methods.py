"""
    ============================================================================================================
                                        Python Object-Oriented Programming
                                           Special Magic/Dunder Methods
    ============================================================================================================
"""
"""
    Ao defenir nossos métodos especiais nós podemos alterar alguns dos comportamentos indejados de nossas variáveis
    , atributos ou objetos. Por exemplo o comportamento ao somar strings ser diferente ao de somar ints. O de imprimir
    um objeto e receber apenas uma mensagem dizendo que é um objeto e seu endereçod e memória. Podemos fazer a 
    impressão ser algo mais userfriendly. Esses MÉTODOS ESPECIAIS são sempre cercados por '__', muitas pessoas chamam 
    esse duplo _ de dunder (double underscore), ou seja, se ouvir alguém dizer dunder init ele se refere a __init__.
    Já vimos o __init__ ao estudar classe e módolos em Pyhton, ele é um dunder que já estamos acostumados é um dos 
    métodos especiais mais comuns ao se trabalhar com classes.  Ele é um método especial que é implicitamente chamado
    quando chamamos uma classe para iniciá-la e setar todos os atributos.
    Agoa vamos nos familiarizar com outros métodos especiais. Aqui estão dois que precisamos implementar praticamente
    sempre, elas são implicitamente chamadas sempre que usamos repre(emp_1) ou str(emp_1) no nosso objeto.
    __repr__  : Deve ser uma representação não ambígua do nosso objeto, deve ser usado para debuggar, lobbing e coisas
                desta netureza. Feita para ser vista por outros desenvolvedores. 
    
    __str__   : Está mais para uma representação legível de um objeto e tende a ser uma representação visual do objeto
                para ser mostrada ao usuário.  
    
    Vamos implementar na classe Employee e obervar a diferença. 
    Primeiro implemente __repr__ primeiro, ou no mínimo ele, pois o __str__ usa o __repr__ como callback.
"""


class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first.title()
        self.last = last.title()
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + "@company.com"

        Employee.num_of_emps += 1

    def nome_completo(self):
        return f'{self.first} {self.last}'

    def aumento_sal(self):  # primeiro argumento é a própria classe
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):
        return f"{self.nome_completo()} - {self.email}"

    # Ver após de __add__
    def __add__(self, other):
        return self.pay + other.pay

    # Ver após __len__
    def __len__(self):
        return len(self.nome_completo())


emp_1 = Employee('Flavio', 'Alvarenga', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1)  # Lembre que antes de implementar __repre_ a print imprimia <__main__.Employee object at (endereço)>
# Antes de definir __str__ print escrevia __repr__, mas o __str__ sobreescreve. Chamar da seguinte forma permite ambas
print(repr(emp_1))  # = print(emp_1.__repr__())
print(str(emp_1))   # = print(emp_1.__str__())

"""
    __init__, __repr__, __str__ são os métodos que provavelmente usaremos mais, mas vamos dar uma olhada em mais alguns
    para saber como funcionam.
    __add__ : print(1+2) chama um método dunder no background chamado __add__ : print(int.__add__(1,2)) >>> 3
    strings tem seu próprio __add__ que seria str.__add__('a', 'b')) >>> ab
    
    Podemos customizar como adicionamos em um objeto ao criar o __add__ método nele.
    Diagampos que por exemplo queremos saber o total de salário ao somar Funcionários da classe Empolyee. 
    (Por mais que no mundo real ao fazer isso seja melhor fazê-lo de forma explícita, mas fazer assim pelo bem do
    exemplo)
    
"""
print(1 + 2)
print('a' + 'b')

print(int.__add__(1, 2))
print(str.__add__('a', 'b'))

print(emp_1 + emp_2)
#  Veja que ao realizar a soma de dois objetos de Employee __add__ foi chamada e realizou a soma dos atributos pay.
"""
    print(len('teste')) Também é um método especial, usamos quando queremos saber o tamanho de algo. 
    print('teste'.__len__()) é o comando por detrás 
"""
print(len(emp_1))
print(len(emp_2))
