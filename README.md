# Python-Mod4POO
Módulo 4 Python - Programação Orientada a Objetos do curso de python do Luiz Otávio Miranda (udemy).

Resumo do módulo.

- Classes:
    - Tipo structures do C. São basicamente moldes de um objeto. Espécies. Tipos. Família. Categorias.
- Instância:
    - Criação de um objeto usando uma classe.
- Construtores de Classe:
    - __init__(self, ...) é o método inicial de uma classe padrão. Onde são criados atributos de um objeto.
- Atributos de Classe:
    - São atributos criados dentro da classe, mas fora de qualquer método. Podem ser usados globalmente dentro da classe, mas podem ser sobrepostos por métodos ou pela instânciação.

#######################################################################################

- Métodos de Instância:
    - Trabalha apenas com instância. São os métodos tradicionais no geral. No geral recebe 'self' como parâmetro.
- Métodos de Classe:
    - Trabalha com classes. Recebe como parâmetro 'cls' ao invés de 'self', e usa o decorador @classmethod para diferenciar.
- Métodos Estáticos:
    - Não recebem parâmetros 'cls' nem 'self'. Funcionam como métodos pois a característica é atribuida à classe.

#######################################################################################

- Método Get:
    - Usa-se normalmente o decorador @property pra diferenciar um método get. Lê atributos de um objeto, normalmente privado. O nome do método precisa ser o mesmo nome do atributo que se deseja ler.
- Método Set:
    - Usa-se normalmente o decorador @atributo.setter para diferenciar um método set. Configura atributos de um objeto, normalmente privado, e sem precisar alterar o código original das classes. O nome do decorador 'atributo' e do método precisa ser o mesmo nome do atributo que se deseja configurar.

#######################################################################################

- Encapsulamento Public:
    - Por padrão, todos os atributos criados são publicos e podem ser acessados pelo editor de texto ou IDE.
- Encapsulamento Protected:
    - O mais utilizado pela comunidade python. Por convenção, se utiliza _ antes de qualquer atributo criado. As IDEs e editores já entnedem que não é um valor que deve ser acessado ou configurado diretamente, e por isso lista por último ao tentar acessar.
- Encapsulamento Private:
    - O menos utilizado. Se utiliza __ antes de qualquer atributo criado. As IDES e editores proibem o acesso normal desse atributo, e pra acessar é preciso fazer gambiarra. Não se recomenda de forma alguma o acesso e configuração desses valores.

#######################################################################################

- Associação (de classes):
    - Uma classe utiliza outra classe, e uma pode viver/funcionar sem a outra. Exemplo: Classe Escritor pode usar uma Classe Caneta, Lápis ou Keyboard, mas ele pode não usar nenhuma das 3. Continuará sendo um escritor.
- Agregação (de classes):
    - Uma classe utiliza outra classe, e uma depende da outra de forma fraca. Exemplo: Carrinho de Compras precisa de Produtos, mas não o inverso. Ou um Carro precisa de Rodas pra andar, mas não o contrário. Eles isolados funcionam, mas serão inúteis.
- Composição (de classes):
    - Uma classe utiliza outra classe, e uma depende da outra de forma forte. Se uma instância for deletada, todos os atributos da classe associada à classe instanciada serão deletados juntos. Exemplo: Cliente preicsa de Endereço, e vice-versa. Corpo Humano precisa do Cérebro, e vice-versa.

#######################################################################################

- Herança Simples:
    - Uma classe herda todos os atributos e métodos de outra classe, mas não ocorre o contrário.
- Herança Múltipla:
    - Uma classe herda todos os atributos e métodos de duas ou mais classes, mas não ocorre o contrário.
- Sobreposição (de métodos):
    - Quando se cria um método dentro de uma classe filha herdada que sobrepõe o método da classe mãe com o mesmo nome. Pra resolver possíveis incompatibilidades, usa-se 'super().métodosobreposto' dentro do método conflituoso criado, e assim recebe todos os atributos da classe mãe e ainda acrescenta mais atributos exclusivos à classe filha.
- Problema do Diamante:
    - Quando uma classe D herda multiplamente de C e B, e C e B herdam de A. O interpretador do python não sabe como escolher as heranças.

#######################################################################################

- Classes Abstratas:
    - Classes que não tem necessidade de serem instanciadas, pois as subclasses já fazem o trabalho de categorizar.
    - Exemplo: Classe Conta, Classe Conta Corrente e Classe Conta Poupança. Não há necessidade de instanciar 'Conta', pois só existe dois tipos de conta: Corrente e Poupança.

    - Métodos Abstratos:
        - Métodos que não tem corpo, não escreve código nele, para que as outras classes filhas herdem este método e sejam OBRIGADAS a criar esse métodos nessas classes filhas. Geralmente métodos que devem ser e serão usados por todas as classes filhas, mas que vão agir de forma diferente pra cada classe. @abstractmethod é usado pra diferenciar.
        - Exemplo: Toda conta deposita e faz saque de forma igual, mas conta corrente e poupança possuem regras diferentes para saque, e precisam ser mudadas dentro dessas subclasses.

    - Métodos Concretos:
        - Métodos tradicionais que se usa normalmente, é herdado pela hierarquia e não são obrigatórios definir em cada subclasse, pois agem de forma igual para todas elas.
        - Exemplo: depósito de uma conta. Tanto Conta Corrente quanto Poupança funcionam de forma igual. Não há necessidade de definir métodos 'depósitos' nessas subclasses. Do jeito que elas irão herdar, vão funcionar perfeitamente.

- Polimorfismo:
    - É o princípio que permite que classes derivadas de uma mesma superclasse tenham métodos iguais (de mesma assinatura), mas comportamentos diferentes. Basicamente tudo que for implementado com métodos abstratos, gera polimorfismo.

#######################################################################################

- Métodos Mágicos (especiais):
    - Métodos que literalmente transformam o comportamento de uma classe. Usa-se 'def __método__()', sempre dois underscore antes e depois do nome principal. São built-in, e fazem todo o trabalho por nós por trás dos panos.