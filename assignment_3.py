def prime(number):
    if number <2:
        return False
    for i in range(2,number):
        if number%i == 0:
            return False
    return True

def main():
    for num in range(2,501):
        if prime(num):
            print(num, end=" ")

main()