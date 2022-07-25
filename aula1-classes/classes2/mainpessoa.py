from pessoa import Pessoa

p1 = Pessoa('Victor', 25)  # Forçamento para que nossas instâncias tenham parâmetros padrão.
p1.nome = 'Luiz'  # Mudo o nome.
p1.outro_metodo()

p1.comer('maçã')  # Estou mandando a pessoa comer.
p1.comer('maçã')  # A pessoa já está comendo. Se esse método for chamado de novo, o "if" detectará.
p1.parar_comer()
p1.parar_comer()
p1.falar('POO')
p1.comer('alimento')
p1.parar_comer()
p1.parar_falar()
p1.falar('um assunto qualquer')

#################################
print()

p2 = Pessoa('João', 32)

p1.falar('POO')
p2.falar('Filmes')
p2.comer('Churrasco')
p1.comer('Ovo')  # Provando que objetos são independentes.
