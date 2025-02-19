import os

def evaluar_expresiones():
    repo_name = os.getenv('REPO_NAME', 'Desconocido')
    es_principal = os.getenv('ES_PRINCIPAL', 'false').lower() == 'true'
    mensaje = os.getenv('MENSAJE', 'Sin mensaje')
    
    print(f"Repositorio: {repo_name}")
    print(f"¿Es la rama principal? {'Sí' if es_principal else 'No'}")
    print(f"Mensaje: {mensaje}")

if __name__ == "__main__":
    evaluar_expresiones()
