import os

from domain.archive import Archive

if __name__ == '__main__':
    arquivo = Archive(path_file=)
    dados = None
    if os.path.exists(path_file):
        dados = arquivo.file_read
    else:
        arquivo.create_archive()

    if dados:
        novo_registro = Transparence