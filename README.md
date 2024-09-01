# Checkpointing
Generar un programa que sea capaz de restaurar el estado de ejecución

## Pickle
Se trata de una libreria para python que nos permite guardar de manera binaria utilizando serialización casi cualquier tipo de dato en python. La ventaja de que se guarde de manera binaria es que un humano no puede leer la información almacenada y es posible enviar esta información a otro sistema evitando en gran medida la perdida de información.

## Función para guardar datos en un documento
La función `dump()` nos permite serializar un objeto y guardarlo en un archivo, en este caso se trata de la cadena que se muestra en el display de la calculadora
```
def save() -> None:
    # 'wb' Abrir el archivo en modo escritura binaria
    with open(filename, 'wb') as file:
        pickle.dump(display.get(), file)
```

## Función para guardar datos en un documento
La función `load()` nos permite deserializar un archivo y almacenarlo en una variable
```
def load_file() -> None:
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
    # 'rb' Abrir el archivo en modo lectura binaria
        with open(filename, 'rb') as file:
            loaded_data = pickle.load(file)
        
        print(loaded_data)
        cleanZero()
        display.insert(0, loaded_data)
        try:
            updateConversor(int(loaded_data))
        except:
            print("[-] Error al restaurar la ultima conversión")
```
## Funcionamiento

>
![Función]("")
