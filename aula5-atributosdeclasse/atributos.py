class A:
    vc = 123

a1 = A()
a2 = A()
print("Todos os valores atribuídos:")
print(a1.vc)  # instância a1 possui vc = 123
print(a2.vc)  # instância a2 possui vc = 123
print(A.vc)   # classe A possui vc = 123

print()
A.vc = 321  # Alteração do vc dentro da classe
print("A.vc = 321:")
print(a1.vc)  # Como alterei o vc da classe, e não de cada instância, mudou para todos
print(a2.vc)
print(A.vc)

##############################################################
# O que acontece é que o interpretador procura primeiro variáveis dentro das instâncias, e depois dentro da classe.
# Veja na prática que ambos, por mais que estejam com vc = 321...
# ...estão vazios, pois não existem variáveis atribuidas a eles em si, e sim da classe.
print()
print("a.__dict__ de cada um:")
print(a1.__dict__)  # .__dict__ mostra todos os atributos que foram "alocados" em uma instância.
print(a2.__dict__)

print()
# Agora irei mudar a1.vc
a1.vc = 456

print("a.__dict__ após a1.vc = 456:")
print(a1.__dict__)
print(a2.__dict__)

print("\n","#"*40)
################################################################

# Crio uma classe nova
class B:
    vc = 123
    def __init__(self):
        self.vc = 321

b1 = B()
b2 = B()

# Agora somente 'B.vc' foi mantido. Pois qualquer instância criada terá agora valor 321 como padrão.
print(b1.vc)
print(b2.vc)
print(B.vc)
