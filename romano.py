import rom
import rom.rom


def MakeRomanInt(a):
    #a = input("Escreva um numero romano: ")
    a = rom.rom_parse(a)
    print(a)
