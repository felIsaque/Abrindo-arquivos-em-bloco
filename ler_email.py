import sys
import re
from os import sep

from get_paragraph import GetParagraph

home_path = str(Path.home())
path_file = f"{home_path}{sep}Documents"
path_file_copy = f"C:{sep}Users{sep}leilao{sep}AppData{sep}Roaming{sep}Thunderbird{sep}Profiles{sep}kc68u730.default-release{sep}Mail{sep}pop3.nossoleilao.com-1.br{sep}Sent_copy"
path_inbox = f"C:{sep}Users{sep}leilao{sep}AppData{sep}Roaming{sep}Thunderbird{sep}Profiles{sep}kc68u730.default-release{sep}Mail{sep}pop3.nossoleilao.com-1.br{sep}Inbox"


def get_paragraph_list(file, chunks_size, obj_paragraph):

    paragraph_list = []
    while sys.getsizeof(paragraph_list) < chunks_size:
        paragraph = obj_paragraph.separate_email()

        if not paragraph:
            break

        paragraph_list.append(paragraph)

    if paragraph_list:
        return paragraph_list
    return


diferentes = []


def send_email_to_inbox():

    with open(path_file, "r", encoding="utf8") as file:
        get_paragraph_ins = GetParagraph(file)

        while 1:
            block_paragraph_list = get_paragraph_list(
                file, 27272, get_paragraph_ins
            )
            if not block_paragraph_list:
                break

            file_copy = open(path_file_copy, "r", encoding="utf8")
            get_paragraph_ins_copy = GetParagraph(file_copy)

            while 1:
                block_paragraph_list_copy = get_paragraph_list(
                    file_copy, 27272, get_paragraph_ins_copy
                )

                if not block_paragraph_list_copy:
                    file_copy.close()
                    break

                for item in block_paragraph_list:
                    if item not in block_paragraph_list_copy:
                        diferentes.append(item)

    print(diferentes)
    with open(path_inbox, "a") as file:
        for email in diferentes:
            file.write(email)
