def load_input(file_name: str):
    with open(file_name, 'r') as f:
        result = f.readlines()
    return result
