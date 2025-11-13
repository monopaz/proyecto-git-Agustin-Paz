# Sistema de gestión de tareas

def crear_tarea(nombre):

    print(f"Tarea '{nombre}' creada exitosamente")

if __name__ == "__main__":

    crear_tarea("Tarea de ejemplo")

def listar_tareas():

    print("Listando todas las tareas...")

def eliminar_tarea(nombre):

    print(f"Tarea '{nombre}' eliminada")

if __name__ == "__main__":

    crear_tarea("Tarea de ejemplo")

    listar_tareas()
