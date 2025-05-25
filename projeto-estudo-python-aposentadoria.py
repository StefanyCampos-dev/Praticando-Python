from datetime import datetime  # importa módulo para lidar com datas e horas

def linha(tam=50): #chama linhas e caso não colocado o tamanho, assume 50
    print('-=' * tam)

def calcular_idade(ano_nascimento): # função que calcula a idade atual
    return datetime.now().year - ano_nascimento #retorna a diferença entre o ano atual subtraindo o ano de nascimento

def calcular_tempo_contribuicao(ano_contratacao): # função que calcula o tempo de contribuição 
    return datetime.now().year - ano_contratacao #retorna a diferença entre o anos atual subtraiando o ano de contratação

def calcular_anos_para_aposentar(tempo_contribuicao, sexo): # define o tempo necessário para apos !0 de m e f
    if sexo.lower() == 'f':
        tempo_necessario = 30
    elif sexo.lower() == 'm':
        tempo_necessario = 35
    else:
        raise ValueError("Sexo Invalido. Use 'M' ou 'F'.") #caso o sexo não seja masculino ou feminino, retorna)

    restante = tempo_necessario - tempo_contribuicao  # calcula o tempo restante para atingir o tempo necessário
    return max(restante, 0) #retorna o maior valor entre o restantes e 0, garantindo que não seja senagtivo

def coletar_dados(): #  faz tratamento básico de erros
    dados = {} #coloca os dados em um dicionário 

    dados['nome'] = input("Nome completo: ").strip()  # remove espaços extras
    dados['sexo'] = input("Sexo (M/F): ").strip().lower()  # minusculo

    try: #tratamento de erro
        dados['ano_nascimento'] = int(input("Ano de nascimento: "))
        dados['ano_contratacao'] = int(input("Ano da 1ª contratação: "))
        dados['registro'] = str(input('Esta trabalhando atualmente? (S/N): ')).strip().lower()
    except ValueError: #tratamento de erro 
        print("Entrada inválida. Tente novamente.")
        return None  # sai da função 

    return dados

def mostrar_resultado(dados): # imprime o resultado da simulação com base nos dados coletados
    idade = calcular_idade(dados['ano_nascimento'])
    tempo_contrib = calcular_tempo_contribuicao(dados['ano_contratacao'])
    anos_faltando = calcular_anos_para_aposentar(tempo_contrib, dados['sexo'])

    linha()  
    print("\n🧾 Resultado da simulação:")
    print(f"Nome: {dados['nome'].title()}")
    print(f"Idade atual: {idade} anos")
    print(f"Tempo de contribuição: {tempo_contrib} anos")
    print(f"⏳ Faltam {anos_faltando} anos para aposentadoria.")
    print("\n📌 Observação: O tempo real de contribuição pode variar conforme vínculos anteriores em outras empresas e registros no INSS.")
    linha()  

def main(): # controla o fluxo do programa
    dados_usuario = coletar_dados()  # recebe dados do usuário
    if dados_usuario:
        mostrar_resultado(dados_usuario)

if __name__ == "__main__": # mantem script principal rodando
    main()
