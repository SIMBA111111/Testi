import re


def emails(file_path):
    symbols = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    with open(file_path, 'r') as file:
        for line in file:
            yield re.findall(symbols, line)


mails = []
file = '6th_example.txt'
for email in emails(file):
    mails += email
    print(email)


def copy_mails(output_file):
    with open(output_file, 'w') as output_file:
        for email in mails:
            output_file.write(email + '\n')


output_file = '6th_example2.txt'

copy_mails(output_file)
