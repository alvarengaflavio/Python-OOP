"""
    ============================================================================================================
                                        Python Object-Oriented Programming
                                          Classmethods and Staticmethods
    ============================================================================================================
"""
"""
    ************************************************ CLASS METHODS ***************************************************
    Como visto um Método comum sempre pega a instância da classe como primeiro argumento. 'self'
    Então como mudamos isso pra que ele automaticamente pegue a classe como primeiro argumento do método?
    Para isso vamos utilizar o CLASS METHOD, método de classe.
    Para isso é necessário colocar um decorador no topo chamado @classmethod
    Vamos criar um aqui embaixo na classe que estamos trabalhando.
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

    """
        farei um arquivo apenas para decoradores, mas esse basicamente esse está adicionando a funcionalidade
        para o nosso método de agora poder receber a classe como argumento e não a instância. Por convenção
        no méthodo da instância chamamos a variáveld e 'self', a convenção para a variável de classe é 'cls'
    """

    @classmethod  # decorador que indica que é um método da classe
    def set_aumento_sal(cls, amount):  # primeiro argumento é a própria classe
        cls.raise_amount = amount


emp_1 = Employee('Flavio', 'Alvarenga', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
#  todos valem 1.04, 4%, pois existe na classe a variável 'raise_amount' já originalmente setada pra 4%
# agora vamos tetar aumentar pra 5%

Employee.set_aumento_sal(1.05)  # A classe é passada como argumento AUTOMATICAMENTE, então passamos apenas o amount

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
"""
    Todos valem 5% agora pq vc alteura o valor da variável da classe, que é válida em todas as instâncias
    Employee.set_aumento_sal(1.05) é equivalente a Employee.raise_amount = 1.05 , só que feito através do método
    Podemos rodar o método da classe para a instâncais também, o q alteraria todas as instâncias (porém não se usa)
"""
emp_1.set_aumento_sal(1.06)  # também funciona para todos mas NÃO se usa

"""
    Pode-se usar métodos de classe como construtores alternativos para a classe. Ou seja, podem fornecer múltiplas
    formas de criar os objetos da classe. Por exemplo, se alguém tiver que usar nossa classe Employee e tem a 
    necessidade de tratar a informação dos funcionários vem em forma de string separados por hífens, precisa ser 
    quebrada e tratada antes de criar, OU SEJA, uma forma de receber essa string e criar um funcionário a partir dela
    retirando as informações dessa única variável.    
"""
emp_str_1 = 'Fausto-Silva-70000'        # criar o novo funcionário a partir disso
emp_str_2 = 'Felipe-Smith-30000'
emp_str_3 = 'Selena-Gomez-90000'


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

    @classmethod  # decorador que indica que é um método da classe
    def set_aumento_sal(cls, amount):  # primeiro argumento é a própria classe
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):  # from_ no começo de construtores de classmethos tb é convenção
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)    # retorna pra poder criar o objeto, chama por cls que é o mesmo que Employee2


new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)
"""
    ************************************************ STATIC METHODS ***************************************************
    Os Métodos Regulares (de instância) passam a instância como argumento 'self', os Métodos de Classe passam a classe 
    como argumento 'cls' e os Métodos Estátidos NÃO PASSAM NADA automaticamente, eles funcionam basicamente como uma
    função comum, exceto que está incluso e uma classe por ter alguma conexão lógica com a classe. 
    
    Para criar basta usar um decorador, de forma semelhante ao do método de classe, chamado @staticmethod
"""
import datetime


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

    @classmethod
    def set_aumento_sal(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)    # Por exemplo aqui utilizamos a variável cls AQUI, não poderia ser Estática

    @staticmethod
    def dia_util(day):  # não passa nada automaticamente. Python tem métodos que segunda = 0 até domingo = 6
        if day.weekday() == 5 or day.weekday() == 6:    # se for Sábado ou Domingo
            return False
        return True
    # Uma DICA para saber se um MÉTODO deve ser ESTÁTICO é ver se ele precisa acessar alguma info da instância ou da
    # classe. Se não precisar de nenhum dessas informações em nenhum lugar da função ele deveria ser um MÉTODO ESTÁTICO.


my_date = datetime.date(2020, 9, 22)
print(Employee.dia_util(my_date))  # True pois hoje é uma terça-feira =D
