from first_task import salary_calculations
from second_task import cats_handler
from pathlib import Path
from directory import output_directory_insides


def main():
    cats_file = 'cats.txt'
    cats = cats_handler.get_cats_info(cats_file)
    print(f'Data from file {cats_file}:')
    for cat in cats:
        print(cat)
    salary_file = 'salary.txt'
    total_salary, average_salary = salary_calculations.total_salary(salary_file)
    print(f'Data from file {salary_file}:\n'
          f'Total salary: {total_salary}\n'
          f'Average salary: {average_salary}')


if __name__ == '__main__':
    print(output_directory_insides())
