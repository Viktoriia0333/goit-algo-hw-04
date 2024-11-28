from pathlib import Path


def get_cats_info(path: str) -> list:
    file = Path(__file__).parent / path
    print(file)
    try:
        with open(file, 'r', encoding='utf-8') as f:
            cats = f.readlines()
            result = []

            for cat in cats:
                attributes = cat.split(',')

                if len(attributes) == 3 and isinstance(attributes[1], str) and attributes[2].strip().isdigit():
                    result.append({'id': attributes[0], 'name': attributes[1],
                                           'age': attributes[2].strip()})

            if not result:
                print('There are no correct information in the file')

        return result

    except FileNotFoundError:
        print('File is not found')
