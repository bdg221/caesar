#!/usr/bin/python3

import sys

# ASCII A = 65 and a= 97
# ord gets int representing unicode character
# chr does inverse of ord

def encrypt(orig, s=3):
    result = ""
    for i in range(len(orig)):
        if(orig[i].isspace() == True):
            result += orig[i]
        else:
            result += chr(ord(orig[i])+s)
    return result

def decrypt(code, s=3):
    result = ""
    for i in range(len(code)):
        if(code[i].isspace() == True):
            result+= code[i]
        else:
            result += chr(ord(code[i])-s)
    return result

def main():
    if(len(sys.argv) == 3 or len(sys.argv) == 4):
        if (sys.argv[1] == "encode"):
            if(len(sys.argv) == 4):
                enc = encrypt(sys.argv[2], sys.argv[3])
            else:
                enc = encrypt(sys.argv[2])
            print("Encrypted value: "+ enc)
        elif (sys.argv[1] == "decode"):
            if(len(sys.argv) == 4):
                dec = decrypt(sys.argv[2], int(sys.argv[3]))

            else:
                dec = decrypt(sys.argv[2])
            print("Decrypted value: "+ dec)
        else:
            help()
            defaults()
    else:
        help()
        defaults()

def help():
    print("encode example: caesar.py encode \"{text to encode}\" {shift number}")
    print("decode example: caesar.py decode \"{text to decode}\" {shift number}")
    print("{shift number} is optional and a default value of 3 will be used if not specified.")

def defaults():
    test1 = "Hello World"
    t1e = encrypt(test1)
    t1d = decrypt(t1e)
    t1e5 = encrypt(test1, 5)
    t1d5 = decrypt(t1e5, 5)



    print("caesar.py encode \"" + test1 + "\"")
    print(t1e)
    print("caesar.py decode \"" + t1e + "\"")
    print(t1d)
    print("caesar.py encode \"" + test1 + "\" 5")
    print(t1e5)
    print("caesar.py decode \"" + t1e5 + "\" 5")
    print(t1d5)

def moreExamples():
    test2 = "Get busy living or get busy dying"
    t2e = encrypt(test2)
    t2d = decrypt(t2e)
    t2e5 = encrypt(test2, 5)
    t2d5 = decrypt(t2e5, 5)
    print("\n caesar.py encode \"" + test2 + "\"")
    print(test2)
    print(t2e)
    print(t2d)
    print("\n caesar.py encode \"" + test2 + "\" 5")
    print(t2e5)
    print(t2d5)

main()
