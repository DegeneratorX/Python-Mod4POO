
class A:
    def __new__(cls, *args, **kwargs):  # Real construtor de uma classe. Sobrepõe o __init__.
        pass  # Com ele inicializado, o __init__ não executa, portanto não irá printar o que estiver em __init__.


    def __init__(self):  # "Construtor". Não é executado por conta do __new__
        print('Estou no INIT')


a = A()

#########################################################
print()
print("#"*20)
print()

# Para executar tudo que estiver dentro do __new__ e o __init__, é necessário retornar o construtor da classe mãe suprema built-in, a 'class object'

class B:
    def __new__(cls, *args, **kwargs):
        print("Estou no NEW")
        return super().__new__(cls)  # Isso é igual a 'object.__new__(cls)'
        # Ao retornar isso, ele agora permite a execução tanto de __new__ quanto de __init__.


    def __init__(self):
        print('Eu sou o INIT')

b = B()  # Agora sim executa ambos os métodos.

#########################################################
print()
print("#"*20)
print()

# Para usar o __new__ de forma que todo objeto seja instanciado apenas UMA VEZ para uma classe, usa-se esse "template" abaixo.

class C:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_atributo_generico'):
            cls._atributo_generico = object.__new__(cls)
        return cls._atributo_generico

    
    def __init__(self):
        print('Estou no INIT')

c1 = C()
c2 = C()
c3 = C()

print(c1 == c2 == c3)  # Todas as outras instâncias serão cópias da primeira.
print(id(c1), id(c2), id(c3))  # Endereços iguais. Cria cópias.
