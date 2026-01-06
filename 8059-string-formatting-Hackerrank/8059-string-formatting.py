def print_formatted(number):
    width=len(bin(n)[2:])
    for i in range(1,n+1):
        stri = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        print(stri,octal ,hexa ,binary) 
    # your code goes here

