"""
    ============================================================================================================
                                        Python Object-Oriented Programming
                                                 Class Variebles
    ============================================================================================================
"""
"""
    Vimos sobre classes e como criar instâncias dessa classe. Aprendemos sobre variáveis da instância que é uma
    informação é que única para cada instância, então variáveis de instâncias são essas como no código abaixo que são
    settadas com o argumento 'self'.
    Então por exemplo na classe Employee nos setamos as variáveis first, last, e-mail e pay que servem para todas as 
    instâncias que de Employees que serão criadas.
    ********************************************[ VARIÁEIS DE CLASSE ]**************************************************    
    Variáveis de classe, são variáveis que são compartilhadas com TODAS AS INSTÂNCIAS da classe. 
    Então enquanto as variáveis de instância são únicas para cada instância da classe que for criada, a 
    VARIÁVEL DE CLASSE devem ser a mesma independente da instância.
    
    Na classe Empolyee utilizada na aula 1 (que foi copiada pra cá e está logo ali abaixo), vamos colocar uma variável
    de classe. Digamos que essa empresa dê aumentos anuais para seus funcionários. Por mais que a quantidade varie de 
    ano pra ano, o que for acertado para o aumento daquele ano vai ser aplicado igualmente para todos os funcionários.
     
     Antes de implementarmos a variável de classe, primeiros vamos colocar o aumento HARDCODED na classe como a classe
     definida como apply_raise.
"""


class Employee:

    def __init__(self, first, last, pay):

        self.first = first.title()
        self.last = last.title()
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + "@company.com"

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)


emp_1 = Employee('Flavio', 'Alvarenga', 50000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

"""
    Funciona mas não é uma boa forma de implementar. O melor seria poder chamar emp_1.raise_amount ou ainda melhor
    poder chamar a classe com um Employee.raise_amount. Mas raise_amount não existe ainda, podemos apenasr aumentar em 
    4% que está com valor fixo no código. E nem podemos aplicar os 4% de uma forma fácil para todos os empregados. 
    PARA criar a variável raise_amount, basta ir para o topo da classe e declará-la desta forma:
"""


class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):

        self.first = first.title()
        self.last = last.title()
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + "@company.com"

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # OU Employee.raise_amount
        # Aqui raise_amount pode ser colocada com o self ou a classe como prefixo. self.raise_ ou Employee.raise_


emp_1 = Employee('Flavio', 'Alvarenga', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
"""
Podemos ver que essa variável é acessível tanto pela própria classe, quanto por QUALQUER instância dessa classe.
Quanto tentamos acessar um atributo que está numa instância ele primeiro vai checar se aquela instância contém aquele
atributo, e se não tiver ele vai ver se a classe ou alguma classe que ele herda contém aquele atributo.
Aqui no caso as instâncias não contém a variável, mas elas acessam a variável que pertence a classe. 
"""
print(emp_1.__dict__)   # método mágico que retorna um dicionário com todas as informaçãoes da instância
# NOTE que NÃO existe a variável raise_amount dentro de emp_1
print(Employee.__dict__)
# Apesar de imprimir um monte de coisas que a gente não entende ou não se importa ele tb mostra que raise_amount
# é SIM uma variável que está contida em Employee. Com valor de 1.04 =)
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# VEJA que chamando raise_amount pela classe atribuindo novo valor ele altera o valor na classe e em todas instâncias
emp_1.raise_amount = 1.06
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# AGORA chamando pela INSTÂNCIA, ele altera somente o valor de emp_1, o que é uma surpresa já que ele n existe lá. COMO?
# Quando chamamos por emp_1, na verdade ele CRIA um atributo dentro da instância pra poder alterar o valor apenas nela
# Coisas mágicas do Python.
print(emp_1.__dict__)   # como explicado acima, confira que agora tem o atributo aqui dentro com valor exclusivo.

"""
    Vamos dar uma olhada em outra variável de classe que talvez não faça muito sentido pra gente agora.
    Digamos que queremos ter guardado o número de funcionários. 
    Se eu criar uma variável chamada num_of_emps = 0
    Todas vez que criarmos um novo funcionário vamos incrementar seu valor, pode fazer isso dentro do método __init__
    pois ele é chamado sempre que a classe é criada. 
"""


class Employee2:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):

        self.first = first.title()
        self.last = last.title()
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + "@company.com"

        Employee2.num_of_emps += 1   # aqui nos increm. o contador e deixamos atribuídos a classe.


print(Employee2.num_of_emps)                    # nenhuma instância criada, valerá zero
emp2_1 = Employee2('Flavio', 'Alvarenga', 50000)    # um incrimento
emp2_2 = Employee2('Test', 'User', 60000)        # dois incrementos
print(Employee2.num_of_emps)
# https://repl.it/languages/python3
