import os

from domain.archive import Archive
from model.transparance import Transparence

if __name__ == '__main__':
    file_name = "transparencia.csv"
    arquivo = Archive(file_name)
    if os.path.exists(file_name):
        print(arquivo.file_read())
        dados = arquivo.file_read()

        if dados:
            novo_registro = Transparence(
                "123456",
                "Novo nome órgão superior",
                "1234",
                "Novo nome órgão",
                "5678",
                "Nova nome unidade gestora",
                "Nova categoria econômica",
                "Nova origem receita",
                "Nova espécie receita",
                "Novo detalhamento",
                "1000.00",
                "900.00",
                "800.00",
                "80.00",
                "2023-03-10",
                "2024",
            )

        arquivo.edit_file(dados, 1200, novo_registro)

    else:
        arquivo.create_archive()


    # Exclui o terceiro registro
    arquivo.delet_file(dados, 2)

    # Grava os dados atualizados
    arquivo.edit_file(dados)
