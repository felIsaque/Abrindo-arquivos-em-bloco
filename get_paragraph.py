import re


class GetParagraph(object):
    def __init__(self, file):
        self.file = file
        self.previous_header = ""
        self.regex_header = r"From - ([\D]{3}) ([\D]{3}) [0-3][0-9] ([0-2][0-9]:[0-9]{2}:[0-9]{2}) ([0-9]{4})"

    def separate_email(self):
        paragraph = ""
        line_in_memory = ""
        header = 0

        while header < 2:
            try:
                line_in_memory = next(self.file)
            except StopIteration:
                break

            if (
                re.search(self.regex_header, line_in_memory)
                or self.previous_header
            ):
                header += 1

            if self.previous_header:
                paragraph = paragraph + self.previous_header
                self.previous_header = ""

            if header < 2:
                paragraph = paragraph + line_in_memory
            else:
                self.previous_header = line_in_memory

        if paragraph:
            return paragraph
        return
