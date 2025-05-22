import json

def executa_transformacao(dll):
    file = dll.split("\n")
    for linha in file:
        if 'CREATE TABLE' in linha:
            print(file)
            out = inicia_leitura_colunas(file)
            return out
        
def inicia_leitura_colunas(file):
    out = ""
    for linha in file:
        if 'CONSTRAINT' in linha.upper():
            break
        
        if 'CREATE TABLE' in linha.upper():
            out+=get_cabecalho(linha)
        
        if 'CREATE TABLE' not in linha.upper():
            if(';' not in linha):
                novalinha = interpreta_linha(linha)
                out+=novalinha+"\n\n"
    return out+"\n}"    


def get_cabecalho(linha):
    
    imports = 'package\n\nimport entidade.persistenciaEL.BaseEntidadePersistirEsocial;\nimport entidade.persistenciaEL.DBFieldELEsocial;\nimport entidade.persistenciaEL.DBTableELEsocial;\nimport java.sql.Timestamp;\nimport java.sql.Date;\nimport java.math.BigDecimal;\n\n'
    
    linha = linha.upper().replace('CREATE TABLE ','').replace('(','').lower()
    schema_table = linha.split(".")
    schema = schema_table[0]
    table= schema_table[1]
    
    nome_classe = corrigi_nome(table)
    nome_classe = f'{capitalize_preserving_format(nome_classe)}DBTableEL'.replace(" ","")
    annotation = f'@DBTableELEsocial(schema="{schema}" , table="{table}")\n'
    java = f'public class {nome_classe} extends BaseEntidadePersistirEsocial '+'{\n\n'

    return imports+annotation+java


def interpreta_linha(linha):
    
    try:
        file = open("config.json",encoding='UTF-8')
        tipos = json.load(file)   
    except:
        tipos = salva_config_incial()
    
    linha = linha.strip()
    nome = ""
    tipo = "String"
    requerid = "false"
    componentes = linha.split()
    if 'not null' in linha.lower():
        requerid = "true"
    
    nome_original = componentes[0]
    nome = corrigi_nome(nome_original)
    
    if "(" in componentes[1]:
        tipo = componentes[1].split("(")[0]
    else:
        tipo = componentes[1]
    tipo = tipos[tipo.replace(",","").upper()]
    
    valor = 'null'
    if tipo == "String":
        valor = '""'
    
    return f'@DBFieldELEsocial(colummn = "{nome_original}", requerid = {requerid}, persist = true, index = 0)\npublic {tipo} {nome} = {valor};'
    
    
def corrigi_nome(nome):
    
    if '_' not in nome: return nome
    
    componentes = nome.split("_")
    nome = ""
    primeira = True
    for item in componentes:
        if not primeira:
            nome+=item.capitalize()
        else: 
            nome+=item
            primeira = False
            
    return nome
    
    
    
def capitalize_preserving_format(string):
    # Converte o primeiro caractere em maiúscula
    capitalized_string = string[0].upper()

    # Mantém a formatação das outras letras
    for char in string[1:]:
        if char.isupper():
            capitalized_string += char
        else:
            capitalized_string += char.lower()

    return capitalized_string


def salva_config_incial():
    tipos = {
        "VARCHAR":"String",
        "INTEGER":"Integer",
        "NUMERIC":"BigDecimal",
        "DATE":"Date",
        "TIMESTAMP":"Timestamp"
    }
        
    file = open("config.json", 'w' ,encoding='UTF-8')
    file.write(json.dumps(tipos, indent = 4) )
    file.close()
    
    return tipos
        