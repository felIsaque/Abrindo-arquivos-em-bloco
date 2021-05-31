import sys


def get_paragraph(file):
    paragraph = ""
    line_in_memory = ""

    while not line_in_memory.isspace():
        try:
            line_in_memory = next(file)
        except StopIteration:
            break

        if not line_in_memory:
            break
        paragraph = paragraph + line_in_memory

    if paragraph:
        return paragraph
    return


def get_paragraph_list(file, chunks_size):

    paragraph_list = []
    while sys.getsizeof(paragraph_list) < chunks_size:
        paragraph = get_paragraph(file)

        if not paragraph:
            break

        paragraph_list.append(paragraph)

    if paragraph_list:
        return paragraph_list
    return


teste = []
paragraphs = []
paragraphs2 = []

with open("sample3.txt", "r") as file:
    while 1:
        paragraph_list = get_paragraph_list(file, 27272)

        if not paragraph_list:
            break
        paragraphs.append(paragraph_list)
