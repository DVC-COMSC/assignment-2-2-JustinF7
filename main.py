def main():
    celsius = float(input("Tempature in Celsius - "))
    fahrenheit = 9/5 * celsius + 32
    print(f'Tempature in Fahrenheit - {fahrenheit:.2f}')
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
