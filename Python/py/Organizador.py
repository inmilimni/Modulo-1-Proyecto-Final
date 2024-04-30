import os
import shutil

def clasificar_archivos(directorio):
    # Inicializar un conjunto para almacenar los tipos de archivo
    tipos_de_archivo = set()

    # Inicializar un contador para los archivos movidos
    archivos_movidos = 0

    # Iterar sobre todos los archivos en el directorio
    for nombre_archivo in os.listdir(directorio):
        # Obtener la extensión del archivo
        tipo_de_archivo = os.path.splitext(nombre_archivo)[1]

        # Si el archivo tiene una extensión
        if tipo_de_archivo:
            # Añadir el tipo de archivo al conjunto
            tipos_de_archivo.add(tipo_de_archivo)

            # Crear un nuevo directorio para este tipo de archivo si no existe
            nuevo_directorio = os.path.join(directorio, tipo_de_archivo[1:])
            if os.path.isfile(nuevo_directorio):
                os.rename(nuevo_directorio, nuevo_directorio + '_archivo')
            os.makedirs(nuevo_directorio, exist_ok=True)

            # Mover el archivo al nuevo directorio
            shutil.move(os.path.join(directorio, nombre_archivo), os.path.join(nuevo_directorio, nombre_archivo))

            # Incrementar el contador de archivos movidos
            archivos_movidos += 1

    # Imprimir el número de diferentes tipos de archivos y el número de archivos movidos
    print(f"Se encontraron {len(tipos_de_archivo)} tipos de archivos distintos.")
    print(f"Se movieron {archivos_movidos} archivos.")

# Llamar a la función en el directorio actual
clasificar_archivos(".")


