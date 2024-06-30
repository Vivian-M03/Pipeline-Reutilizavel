import json
import csv

class Dados:                                   ##criação da classe

    def __init__(self, path, tipo_dados):      ##metodos da classe
        self.__path = path
        self.__tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        self.nome_colunas = self.__get_columns()
        self.qtd_linhas = self.__size_data()

    def __leitura_json(self):              
        dados_json = []
        with open(self.__path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

    def __leitura_csv(self):               
        dados_csv = []
        with open(self.__path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)   
        return dados_csv

    def leitura_dados(self):
        dados = []

        if self.__tipo_dados == 'csv':
            dados = self.__leitura_csv()

        elif self.__tipo_dados == 'json':
            dados = self.__leitura_json()

        elif self.__tipo_dados == 'list':
            dados = self.__path
            self.__path = 'lista em memoria'

        return dados
    
    def __get_columns(self):
        return list(self.dados[-1].keys())
    
    def rename_columns(self, key_mapping):
        new_dados = []
        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)
        
        self.dados = new_dados
        self.nome_colunas = self.__get_columns()

    def __size_data(self):                     ##Ver a quantidade de dados // mander afunção mesmo que simples para futuras aplicaçãoes
        return len(self.dados)
    
    def join(dadosA, dadosB):
        combined_lista = []
        combined_lista.extend(dadosA.dados)
        combined_lista.extend(dadosB.dados)
        
        return Dados(combined_lista, 'list')
    
    def __tranformação_dados_tabela (self):      ##Transformação dos dados das tabelas

        dados_combinados_tabela = [self.nome_colunas]
        for row in self.dados:
            linha = []     ##lista vazia
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, 'Indisponivel'))
            dados_combinados_tabela.append(linha) 
        
        return dados_combinados_tabela
    
    def salvando_dados(self, path):         ##Salvamento dos dados
       
        dados_combinados_tabela = self.__tranformação_dados_tabela()
       
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)
                
