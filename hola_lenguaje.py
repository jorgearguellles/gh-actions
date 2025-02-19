import os

def main():
    nombre = os.getenv("USERNAME")
    lenguaje_favorito = "JavaScript"
    
    print(f"¡Hola, {nombre}! Veo que tu lenguaje favorito es {lenguaje_favorito}.")

if __name__ == "__main__":
    main()
