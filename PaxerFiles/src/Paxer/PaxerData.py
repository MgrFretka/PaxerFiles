#importy
import json

class Paxer:

    class Data:

        def dataWrite(text):
            textd = f'data: {text}'
            file = 'data.json'

            try:
                with open(file, 'w') as f:
                    json.dump(textd, f)
            except FileNotFoundError:
                open('data.json')

        def dataRead():
            file = 'data.json'

            with open(file) as f:
                read = json.load(f)
            print(read)

        def dataCreate():
            file = 'data.json'
            try:
                open(file, 'x')
                print(f'utworzono plik {file}')
            except FileExistsError:
                print(f"Plik {file} już istnieje")


#PaxerData.dataWrite("Hello World")
