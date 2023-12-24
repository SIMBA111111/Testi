import time
from faker import Faker
import random

from sixmy import emails

fake = Faker()


# Декоратор timeit
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        result = end_time - start_time

        print(f"Время выполнения: {result} секунд")

    return wrapper


def generate_random_emails_and_save_to_file(num_emails, output_file_path):
    with open(output_file_path, 'w') as output_file:
        for i in range(num_emails):
            email = fake.email()
            output_file.write(email + '\n')


input_file = '7th_input_example'
num_emails_to_generate = 100000

generate_random_emails_and_save_to_file(num_emails_to_generate, input_file)

output_file = "7th_output_example"


@timeit()
def copy_mails(input_file, output_file):
    with open(output_file, 'w') as output_file:
        for email in mails:
            output_file.write(email + '\n')
