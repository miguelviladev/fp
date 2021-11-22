preco_fabrico = 20
preco_venda = 24.95
imposto = 1.23
spa_tax = 0.20

lucro_unitario = (preco_venda - imposto*preco_fabrico - spa_tax) / imposto

print("Para 500 exeplares a livraria lucrou {:.2f} euros, foi coletado {:.2f} euros em impostos e foram reunidos {:.2f} euros em taxas.".format(lucro_unitario*500, 500*(preco_venda*(imposto-1)), 500*spa_tax))