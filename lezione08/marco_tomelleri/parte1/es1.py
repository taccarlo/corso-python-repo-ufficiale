'''Stampare i numeri pari da 1 a 100, poi stampare i numeri dispari da 1 a 40
(non utilizzare cicli per farlo)'''

def main():
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)
    for i in range(1, 41):
        if i % 2 != 0:
            print(i)

if __name__ == "__main__":
    main()
