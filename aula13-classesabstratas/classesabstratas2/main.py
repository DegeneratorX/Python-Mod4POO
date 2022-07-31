"""
Simulação simples de um banco que possui uma Conta como padrão, e nesse banco possui opção de corrente e poupança.
"""

from classes.conta_poup import ContaPoupanca
from classes.conta_corr import ContaCorrente

cp = ContaPoupanca(1111, 2222, 0)  # Agência, conta e saldo do cliente

cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(1)

print("######################################")

cc = ContaCorrente(agencia=1111,conta=3333,saldo=0,limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)
