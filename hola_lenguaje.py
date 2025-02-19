import os

def main():
    nombre = os.getenv('USERNAME', 'Usuario')
    lenguaje = os.getenv('LANGUAGE', 'Python')
    
    print(f"¡Hola, {nombre}! Veo que tu lenguaje favorito es {lenguaje}.")

if __name__ == "__main__":
    main()
