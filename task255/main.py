import sys

from extender import *

# ----------------------------------------------
if __name__ == '__main__':
    if len(sys.argv) == 4:
        input_file_name = sys.argv[1]
        output_file_name_1 = sys.argv[2]
        output_file_name_2 = sys.argv[3]
    elif len(sys.argv) == 3:
        input_file_name = sys.argv[1]
        output_file_name_1 = sys.argv[2]
        output_file_name_2 = "output2.txt"
    elif len(sys.argv) == 2:
        input_file_name = sys.argv[1]
        output_file_name_1 = "output1.txt"
        output_file_name_2 = "output2.txt"
    elif len(sys.argv) == 1:
        print(
            "Incorrect command line! Attention! File path must not contain spaces. "
            "You must write: python_main <inputFileName>_or_number [<outputFileName1>] [<outputFileName2>]")
        exit()

try:
    int(input_file_name)
    cont = []
    container.random_generate(cont, int(input_file_name))
except ValueError:
    try:
        ifile = open(input_file_name)
        str = ifile.read()
        ifile.close()
    except NameError and FileNotFoundError:
        print(
            "Incorrect command line! Attention! File path must not contain spaces. "
            "You must write: python_main <inputFileName>_or_number [<outputFileName1>] [<outputFileName2>]")
        exit()

    # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
    strArray = str.replace("\n", " ").split(" ")

    cont = []
    fig_num = container.read(cont, strArray)

print('==> Start')

ofile = open(output_file_name_1, 'w')
container.write(cont, ofile)
ofile.close()

cont = container.volume_filter(cont)
ofile = open(output_file_name_2, 'w')
container.write(cont, ofile)
ofile.close()

print('==> Finish')
