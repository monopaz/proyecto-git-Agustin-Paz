# Sistema de gestión de tareas

def crear_tarea(nombre):

    print(f"✓ Tarea '{nombre}' ha sido agregada al sistema")

if __name__ == "__main__":

    crear_tarea("Tarea de ejemplo")
## Características

### Funcionalidades principales

- Creación de tareas

- Gestión eficiente

- Interfaz intuitiva

### Tecnologías

- Python 3.x

- Git para control de versiones

def listar_tareas():

    print("→ Mostrando todas las tareas registradas...")


def eliminar_tarea(nombre):

    print(f"✗ Tarea '{nombre}' ha sido eliminada del sistema")


if __name__ == "__main__":

    crear_tarea("Tarea de ejemplo")

    listar_tareas()
