from clases.areas import area_triangulo, area_rectangulo

def main():
    print("Cálculo de Áreas\n")

    base_t = 10
    altura_t = 5
    print(f"Área del triángulo ({base_t}x{altura_t}) = {area_triangulo(base_t, altura_t)}")

    base_r = 8
    altura_r = 6
    print(f"Área del rectángulo ({base_r}x{altura_r}) = {area_rectangulo(base_r, altura_r)}")

if __name__ == "__main__":
    main()
