from isort import SortImports

with open('some_file.txt', 'r') as handler:
    SortImports(handler, quiet=True)
