"""
    ============================================================================================================
                                        Python Object-Oriented Programming
                                         Inheritance, Creating Subclasses
    ============================================================================================================
"""
"""
    ************************************************ INHERITANCE ***************************************************
    Como o nome diz inheritance (herança) nos deixa herdar atributos e métodos de uma classe Mãe (parent class). 
    Isso é muito útil pq podemos criar uma subclasse, herdar tuda a funcionalidade da nossa classe Mãe e agora 
    podemos sobreescrever ou adicionar uma funcionalidade completamente nova sem afetar a PARENT CLASS de qualquer 
    forma. Vamos oberser no exemplo da classe dos funcionários que viemos trabalhando até aqui, digamos que agora
    eu precise criar dois tipos de funcionários, developers e managers. São bons exemplos de subclasses pois ambos
    terão os atributos básico da classe Employee. Vamos herdar isso tudo de Employee agora: 
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


class Developer(Employee):      # Com esse parantêses dizemos que vamos herdar de Employee
    pass


# pronto! sem nenhum código já herdamos toda a funcionalidade (atributos e métodos) de Employee.
dev_1 = Developer('Flavio', 'Alvarenga', 50000)
dev_2 = Developer('Test', 'Developer', 60000)
print(dev_1.email)
print(dev_2.email)
"""
    Agora quando chamamos a classe Developer para criar o objeto, primeiro ele olha dentro de Developer pra ver se 
    existe o atributo ou método, se não houver ele acessa através da cadeira de herança para encontrar. Essa cadeira
    é chamada de Method Resolution Order, através da função help() fica mais fácil de visualizar. 
"""
print(help(Developer))


class Developer(Employee):      # Com esse parantêses dizemos que vamos herdar de Employee
    raise_amount = 1.10


dev_1 = Developer('Flavio', 'Alvarenga', 50000)
print(dev_1.pay)
dev_1.aumento_sal()
print(dev_1.pay)    # Veja que agora ele pega o aumento de 10% antes de olhar em Employee o valor de 4%
"""
    É importante saber que as alterações feitas em Developer (subclasse) não alteram de forma alguma a classe
    Employee, ela não é afetada por nenhuma modificação e seus objetos continuam funcionando perfeitamente. 
  
"""


class Developer(Employee):      # Com esse parantêses dizemos que vamos herdar de Employee
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # SUPERCLASSE INICIA OS ATRIBUTOS QUE INICIAM NELA
        # Employee.__init__(first, last, pay)   # Também funciona, fica mais simples manter no super
        self.prog_lang = prog_lang


dev_1 = Developer('Flavio', 'Alvarenga', 50000, 'Python')
dev_2 = Developer('Test', 'Developer', 60000, 'Java')

print(dev_1.email)
print(dev_1.prog_lang)
print(dev_2.email)
print(dev_2.prog_lang)


#  Agora vamos criar o MANAGER
class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []  # A lista vazia não foi argumento pq não se faz isso, será explicado depois
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(' --> ', emp.nome_completo())


mgr_1 = Manager('Meu', 'Chefe', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()

print(isinstance(mgr_1, Manager))    # Diz se o objeto é uma INSTANCIA DE UMA CLASSE - mgr_1 é instância de Manager?
print(isinstance(mgr_1, Employee))   # É uma instância de Employee??
print(isinstance(mgr_1, Developer))  # E de Developer? É???

print(issubclass(Developer, Employee))  # issubclass() nos diz se uma CLASSE é uma SUBCLASSE de outra
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
