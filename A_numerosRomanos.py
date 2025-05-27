import re
valores = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}
regex_romano = re.compile(
    r"^M{0,3}"
    r"(CM|CD|D?C{0,3})"
    r"(XC|XL|L?X{0,3})"
    r"(IX|IV|V?I{0,3})$"
)
def romano_a_decimal(romano):
    total = 0
    prev = 0
    for letra in reversed(romano):
        valor = valores[letra]
        if valor < prev:
            total -= valor
        else:
            total += valor
            prev = valor
    return total
def main():
    print("=== Analizador Léxico de Números Romanos ===")
    numero = input("Ingrese un número romano entre I y MMM (1 - 3000): ").upper()

    if regex_romano.fullmatch(numero):
        decimal = romano_a_decimal(numero)
        print(f"Válido. El valor en indoarábigo es: {decimal}")
    else:
        print("Número romano no válido o fuera del rango permitido.")
if __name__ == "__main__":
    main()