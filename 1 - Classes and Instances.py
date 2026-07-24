"""
    ============================================================================================================
                                        Python Object-Oriented Programming
                                               Classes and Instances
    ============================================================================================================
"""
"""
    Método      = Função que é Associada a uma Classe
    Atributos   = Variável assossiada com uma Classe
    
    Por exemplo: Numa empresa os EMPREGADOS podem ser uma classe, pois todos tem atributos e métodos em comum.
    todo Empregado tem um NOME, EMAIL, PAGAMENTO E AÇÕES QUE PODEM EXERCER.
    
    Uma classe é basicamente "A BLUEPRINT" uma planta para criar várias INSTÂNCIAS daquela classe, ou seja, cada
    empregado criado utilizando a classe EMPLOYEE é uma istância da classe.
"""


class Employee:
    pass


# Se eu chamar
emp_1 = Employee()
emp_2 = Employee()
# Cada uma dessas (emp_1 e emp_2) será uma instância diferente da classe Employee.
print(emp_1)
print(emp_2)
'''
    Note que ambas são objetos e ambos tem valores distintos. (Estão alocadas em localizações distintas na memória)
    Isso é uma distinção importante, pois se fala muito sobre variáveis de instância e variáveis de classe, 
    é importante saber a diferença entre elas, aqui será tratado apenas de variáveis de INSTÂNCIA!
    O valor da variável de Instância tem valor ÚNICO para cada instância distinta da classe.
'''
emp_1.first = 'Flavio'
emp_1.last = 'Alvarenga'
emp_1.email = 'flavio.alvarenga@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

'''
    Ficou claro como funcionam os atributos numa classe, mas ao utilizar classes desta forma vc não está tento nenhum
    benefício de se usar classe. Para isso vamos voltar a definição de classe e usar um método especial e mágico 
    chamado: método __init__
'''


class Employee:

    def __init__(self, first, last, pay):
        """
            Pode-se pensar nesse método como INICIALIZADOR, ou em outras linguagens CONSTRUTOR;
            Ao criamos métodos para uma classe, passamos a INSTÂNCIA como a 1ª variável automaticamente;
            Por convenção a INSTÂNCIA é chamada de 'self', pode chamar dq quiser, mas fica com o self msm;
            Depois de 'self' vc pode colocar outras variáveis que o método aceita ao ser chamado
            Nesse caso 'first', 'last' e 'pay', existe tb o email mas ele será criado utilizando o 'first' e 'last'
            !!!OK!!!
            Agora começaremos a SETAR todas essas variáveis da INSTÂNCIA: self.first = first
        """
        self.first = first.title()
        self.last = last.title()
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + "@company.com"

    # IGNORE esse método antes de chegar no comentário pedindo para lê-lo!!!!!!!
    def fullname(self):  # Só precisamos do self, por todo o resto já É atributo dessa classe!!! =)
        return f'{self.first} {self.last}'  # RETORNA SEUS próprios atributos 'first' e 'last'.


# Agora quando criarmos as intâncias logo abaixo, poderemos passar os valores como variáveis ao chamar a classe
# O self já é passado automaticamente, então só precisamos chamar os nomes e o pagamento
emp_1 = Employee('Flavio', 'Alvarenga', 50000)
emp_2 = Employee('Test', 'User', 66600)


print(emp_1.first, emp_1.last, emp_1.email, emp_1.pay)
print(emp_2.first, emp_2.last, emp_2.email, emp_2.pay)
''' 
    Para Realizar algumas ações devemos adicionar MÉTODOS para a nossa classe.
    Digamos que nos quisessemos poder mostar o NOME COMPLETO do nosso empregado, Isso é algo que provavelmente
    a empresia precisaria fazer muito dentro dessa classe. Para isso iremos dentro da def da classe e adicionaremos
    o método. (no caso ele já está pronto ali em cima mas só agora VC ESTÁ AUTORIZADO A LER. =]
'''
# print(f'{emp_1.first} {emp_1.last}')
# print(emp_1.fullname)
# print(emp_2.fullname)
print(emp_1.fullname())
print(emp_2.fullname())

# Um erro muito recorrente ao se criar um método é esquecer o 'self' como primeiro argumento.
# Ao criar o método sem o self o script vai rodar normalmente, só ocorrendo erro ao chamar o método pois ele se passa
# Como argumento automaticamente.

# Também é possível chamar o método através da classe, o que torna mais claro que o q realmente está acontecendo
Employee.fullname(emp_1)    # ao chamar pela CLASSE temos que colocar a instância MANUALMENTE, nesse caso emp_1
emp_1.fullname()            # faz exatamente a msm coisa da linha de cima, mas chamando sua instância automaticamente

# ou seja, quando chamamos "emp_1.fullname()" ela se transforma em "Employee.fullname(emp_1)", emp_1 como argumento e
# retornando os valores atribuidos.
print(Employee.fullname(emp_1))
