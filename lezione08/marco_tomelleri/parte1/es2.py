'''Stampare il risultato della moltiplicazione dei numeri da 1 a 100'''

def main():
    result = 1
    for i in range(1, 101):
        result *= i
    print(result)

if __name__ == "__main__":
    main()
    