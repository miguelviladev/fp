# Um livro custa 20€ a fabricar (PF). Suponha que o preço de capa de um livro é 24,95€
# (PC) e que o mesmo paga uma taxa de IVA de 23% (IMP). Acresce sobre o valor do
# livro uma taxa para compensar os autores pelas cópias de 0,20€ fixos (SPA).
# PC = (PF + Lucro) * (100% + IMP) + SPA
# Para uma tiragem de 500 exemplares: qual o lucro da livraria? Quanto foi coletado em
# impostos? Que quantia de taxas é que foi reunida?

preco_fabrico = 20
preco_venda = 24.95
imposto = 1.23
spa_tax = 0.20

lucro_unitario = (preco_venda - imposto*preco_fabrico - spa_tax) / imposto

print("Para 500 exeplares a livraria lucrou {:.2f} euros, foi coletado {:.2f} euros em impostos e foram reunidos {:.2f} euros em taxas.".format(lucro_unitario*500, 500*(preco_venda*(imposto-1)), 500*spa_tax))