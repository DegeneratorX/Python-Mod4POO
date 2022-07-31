class A:
    def falar(self):
        print("Falando... Estou em A.")


class B(A):
    def falar(self):
        print("Falando... Estou em B.")


class C(A):
    def falar(self):
        print("Falando... Estou em C.")


class D(B, C):  # Herança múltipla: quando herdo de duas classes ou mais.
    # Aproveitando o exemplo, esse é um caso clássico do problema do diamante, onde o interpretador não sabe qual método pegar.
    pass