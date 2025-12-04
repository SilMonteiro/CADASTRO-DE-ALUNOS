import pandas as pd
import numpy as np
import random

df = pd.read_csv('CADASTRO-DE-ALUNOS/codigo-base/alunos.csv', sep=';', on_bad_lines='skip')

def menu_inicial():

    print("Seja Bem Vindo ao sitema de cadastro de alunos (SCA)!\n")
    print("Digite a opção desejada:\n1 - CADASTRAR ALUNO\n2 - PESQUISAR ALUNO\n3 - SAIR DO SISTEMA")


def cadastrar_aluno():

    print("\n-> Para iniciar o cadastro do aluno, por favor preencha os campos abaixo:\n")
    dados_cadastro = {}
    dados_cadastro['nome'] = input("Digite o nome do aluno:")
    dados_cadastro['rua'] = input("Digite a rua do aluno:")
    dados_cadastro['numero'] = input("Digite o numero da casa do aluno:")
    dados_cadastro['bairro'] = input("Digite o bairro do aluno:")
    dados_cadastro['cidade'] = input("Digite a cidade do aluno:")
    dados_cadastro['uf'] = input("Digite a UF do aluno:")
    dados_cadastro['telefone'] = input("Digite o telefone do aluno:")
    dados_cadastro['email'] = input("Digite o email do aluno:")
    dados_cadastro['numero_matricula'] = random.randint(1000, 9999)

    df = pd.DataFrame([dados_cadastro])
    df.to_csv('CADASTRO-DE-ALUNOS/codigo-base/alunos.csv', sep=';', mode='a', header=False, index=False)
    print("\nAluno cadastrado com sucesso!!\n")
    pd.read_csv('CADASTRO-DE-ALUNOS/codigo-base/alunos.csv', sep=';', on_bad_lines='skip')
    print(df)

    
def escolha_opcao():

    menu_inicial()
    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        cadastrar_aluno()
    elif opcao == '2':
        pesquisar_aluno()
    elif opcao == '3':
        sair_sistema()
    else:
        print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    escolha_opcao()

