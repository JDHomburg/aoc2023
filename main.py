from datetime import datetime
import importlib

if __name__ == '__main__':
    day = datetime.today().strftime('%d')
    module = importlib.import_module(f'day{day}.solution')
    for f in dir(module):
        if (f.startswith('task')):
            print(f'Task {f}: {getattr(module, f)()}')
