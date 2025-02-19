import os

def main():
    nombre = os.getenv("USERNAME")
    
    print(f"¡Hola, {nombre}! Veo que tu lenguaje favorito es JavaScript.")

if __name__ == "__main__":
    main()
