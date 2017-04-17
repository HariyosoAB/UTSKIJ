import re
import codecs
import sys


def intToBinary(bilangan):
    x = '{0:08b}'.format(bilangan)
    return x

def XOR(binkread, binread):
    hasil = ""
    for x in range(0,len(binkread)):
        if(binkread[x] == binread[x]):
            hasil = hasil + '0'
        else:
            hasil = hasil + '1'
    return hasil
def encrypt(isi,potongKeyR,potongKeyL):

    binread = ""
    if (len(isi) % 4 != 0):
        for i in range(0, 4 - len(isi) % 4):
            isi = isi + " "
    print "plaintext: " + isi
    for c in isi:
        binread = binread + intToBinary(ord(c))
    potong = re.findall('.{1,32}', binread)

    encrypted = ""
    for c in range(0, len(potong)):
        some = XOR(potongKeyL, potong[c])
        someInt = int(some, 2) + int(potongKeyR, 2)
        encrypted = encrypted + "{0:032b}".format(someInt)


    encryptFin = ""
    write = open('encrypted.txt', 'ab+')

    potongEn = re.findall('.{1,8}', encrypted)
    for c in range(0, len(potongEn)):
        ascii = int(potongEn[c], 2)
        # print ascii
        encryptFin = encryptFin + str(chr(ascii))
        write.write(chr(ascii))

    write.close()
    print "Hasil Enkirpsi: " + encryptFin
    return encryptFin

def decrypt(cipher,potongKeyL,potongKeyR):
    binread = ""
    counter = 1
    for i in range(0, len(cipher)):
        binread = binread + intToBinary(ord(cipher[i]))
        # print cipher[i]
        counter += 1
    potong = re.findall('.{1,32}', binread)
    # print potong
    decrypted = ""
    for c in range(0, len(potong)):
        someInt = int(potong[c], 2) - int(potongKeyR, 2)
        ubah = "{0:032b}".format(someInt)
        decrypted = decrypted + XOR(potongKeyL, ubah)

    decryptFin = ""
    potongEn = re.findall('.{1,8}', decrypted)
    for c in range(0, len(potongEn)):
        ascii = int(potongEn[c], 2)
        decryptFin = decryptFin + chr(ascii)

    print "Hasil Dekripsi: " + decryptFin
    writedec = open('decrypted.txt', 'w+')
    writedec.write(decryptFin)
    writedec.close()

def initializeKey():
    key = raw_input('Enter Key: ')
    binkread = ""
    if (len(key) != 8):
        print "key harus 64bit!"
        sys.exit()
    for a in key:
        binkread = binkread + intToBinary(ord(a))
    potongkey = re.findall('.{1,32}', binkread)
    return potongkey

def main():

    potongkey = initializeKey()
    file = open("plain.txt", "r")
    isi = file.read()
    file.close()

    cipher = encrypt(isi,potongkey[1],potongkey[0])
    decrypt(cipher,potongkey[0],potongkey[1])


if __name__ == "__main__":
    main()