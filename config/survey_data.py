dados_pesquisa = {
    pergunta: {"Sim": s, "Não": n}
    for pergunta, s, n in zip(perguntas, sim, nao)
}

print(dados_pesquisa)
