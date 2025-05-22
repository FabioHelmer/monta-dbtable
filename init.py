from executa_transformacao import executa_transformacao

with open("input.txt", "r", encoding="utf-8") as file:
    conteudo = file.read()
    print(conteudo)
    dbtable = executa_transformacao(conteudo)
    print(dbtable)

    with open("output.txt", "w", encoding="utf-8") as file_out:
        file_out.write(dbtable)
    