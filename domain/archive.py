import csv


class Archive:
    def __init__(self, path_file):
        self.path_file = path_file

    def create_archive(self):
        with open(self.path_file, "w", encoding="utf-8") as file:
            csv.writer(file, delimiter=";")

    def file_read(self):
        """Ler dados do arquivo csv.

        :returns dados: dados do arquivo csv
        """
        with open(self.path_file, "r", encoding="latin-1") as arquivo:
            leitor = csv.reader(arquivo, delimiter=";")

            # Ignora cabeçalho
            next(leitor, None)

            dados = []
            for linha in leitor:
                # Cria um objeto Registro com os campos da linha
                registro = Archive(
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

                dados.append(registro)

        return dados
    @staticmethod
    def edit_file(dados, position, new_register):
        dados[position] = new_register

