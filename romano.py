from rom import rom_parse


def MakeRomanInt(a):
    #a = input("Escreva um numero romano: ")
    a = rom_parse(a)
    print(a)

MakeRomanInt('VCII')
