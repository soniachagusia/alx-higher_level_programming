#!/usr/bin/python3

if __name__ == "__main__":
    import importlib.util
    import sys

    module_name = 'hidden_4'
    module_path = './hidden_4.pyc'  # Provide the path to the hidden_4.pyc file
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    names = dir(module)

    names = [name for name in names if not name.startswith('__')]

    names.sort()

    for name in names:
        print(name)
