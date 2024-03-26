import csv

from model.transparance import Transparence


class Archive:
    def __init__(self, path_file):
        self.path_file = path_file

    def create_archive(self):
        with open(self.path_file, "w", encoding="utf-8") as file:
            csv.writer(file, delimiter=";")

    def file_read(self):
        with open(self.path_file, "r", encoding="utf-8") as file:
            leitor = csv.reader(file, delimiter=";")

            next(leitor, None)
            dados = []
            for linha in leitor:
                transparencia = Transparence(
                    linha[0],
                    linha[1],
                    linha[2],
                    linha[3],
                    linha[4],
                    linha[5],
                    linha[6],
                    linha[7],
                    linha[8],
                    linha[9],
                    linha[10],
                    linha[11],
                    linha[12],
                    linha[13],
                    linha[14],
                    linha[15],
                )

                dados.append(transparencia)

            return dados

    def file_write(self, dados):
        with open(self.path_file, "w", encoding="latin-1") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")

            # Escreve cabeçalho
            escritor.writerow([
                "CODIGO_ORGAO_SUPERIOR",
                "NOME_ORGAO_SUPERIOR",
                "CODIGO_ORGAO",
                "NOME_ORGAO",
                "CODIGO_UNIDADE_GESTORA",
                "NOME_UNIDADE_GESTORA",
                "CATEGORIA_ECONOMICA",
                "ORIGEM_RECEITA",
                "ESPECIE_RECEITA",
                "DETALHAMENTO",
                "VALOR_PREVISTO_ATUALIZADO",
                "VALOR_LANCADO",
                "VALOR_REALIZADO",
                "PERCENTUAL_REALIZADO",
                "DATA_LANCAMENTO",
                "ANO_EXERCICIO",
            ])

            # Escreve os dados
            for registro in dados:
                escritor.writerow([
                    registro.codigo_orgao_superior,
                    registro.nome_orgao_superior,
                    registro.codigo_orgao,
                    registro.nome_orgao,
                    registro.codigo_unidade_gestora,
                    registro.nome_unidade_gestora,
                    registro.categoria_economica,
                    registro.origem_receita,
                    registro.especie_receita,
                    registro.detalhamento,
                    registro.valor_previsto_atualizado,
                    registro.valor_lancado,
                    registro.valor_realizado,
                    registro.percentual_realizado,
                    registro.data_lancamento,
                    registro.ano_exercicio,
                ])

    @staticmethod
    def edit_file(dados, position, new_register):
        dados[position] = new_register

    @staticmethod
    def delet_file(dados, indice):
        del dados[indice]
