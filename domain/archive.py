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

 @staticmethod
    def edit_file(dados, position, new_register):
        dados[position] = new_register



