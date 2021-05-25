import sys


def get_paragraph(file):
    paragraph = ''
    line_in_memory = ''

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

with open('sample3.txt', 'r') as file:
    file2 = open('sample1.txt', 'r')

    while 1:
        paragraph_list = get_paragraph_list(file, 13636)

        while 1:
            paragraph_list2 = get_paragraph_list(file2, 13636)
            # import ipdb; ipdb.set_trace()
            if not paragraph_list2:
                file2.close()
                file2 = open('sample1.txt', 'r')
                break
            paragraphs2.append(paragraph_list2)

            if paragraph_list[-1] in paragraph_list2[-1]:
                teste.append()

        # if not paragraph_list:
        #     file2.close()
        #     break
        # paragraphs.append(paragraph_list)
