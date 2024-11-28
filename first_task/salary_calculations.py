from pathlib import Path


def total_salary(path) -> tuple:
    file = Path(__file__).parent / path

    try:

        with open(file, 'r', encoding='utf-8') as f:
            workers_list = f.readlines()
            salary_list = []

            for worker in workers_list:
                salary = worker.split(',')

                if len(salary) == 2 and salary[1].strip().isdigit():
                    salary_list.append(int(salary[1].strip()))

            if not salary_list:
                print('There are no available salary in the file')
                return 0, 0

        salary_sum = sum(salary_list)
        average_salary = (salary_sum/len(salary_list)).__round__(2)
        result = [salary_sum, average_salary]

        return tuple(result)

    except FileNotFoundError:
        print('Sorry, file was not found')
