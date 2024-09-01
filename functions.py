simbols = ["+", "-", "*", "/", "^", "%"]

def lastIsSimbol(text: str) -> bool:
    for simbol in simbols:
        if text[-1] == simbol:
            return True
    return False

def existDot(text: str) -> bool:
    i = len(text) - 1
    print(i)
    while True:
        for simbol in simbols:
            if text[i] == simbol:
                print(f"simbol: {simbol}")
                return False
        if text[i] == ".":
            print("Se encontro .")
            return True
        i -= 1
        if i == -1:
            print("Fin del indice")
            return False

def factorial (number: int) -> int:
    i = 0
    result = 1
    while i < number:
        result *= i + 1
        i+=1
    return result

# def dec_bin(num: int) -> str:
#     return bin(num)[2:]

def Dec_Bin(dec: int) -> str:
    bin = ""
    cociente = 0
    residuo = 0
    while dec / 2 > 0:
        cociente = int(dec) / 2
        residuo = int(dec) % 2
        dec = cociente
        bin = str(residuo) + bin
        # print(bin)
    # bin = str(cociente) + bin
    return bin

def Dec_Oct(dec: int) -> str:
    oct = ""
    residuo = 0
    while dec > 0:
        residuo = dec % 8
        oct = str(residuo) + oct
        dec //= 8
    return oct

def Bin_Dec(bin: str) -> str:
    dec = 0
    i = 0
    j = len(bin) - 1
    while j >= 0:
        if bin[j] == "1":
            dec += pow(2, i)
        i+=1
        j-=1
    return str(dec)

def Oct_Dec(oct: int) -> str:
    dec = 0
    potency = 0
    
    while oct != 0:
        digit = oct % 10
        dec += digit * (8 ** potency)
        oct //= 10
        potency += 1
    
    return str(dec)

def Dec_Hex(dec: int) -> str:
    hex_chars = "0123456789ABCDEF"
    hex = ""
    
    while dec > 0:
        residuo = dec % 16
        hex = hex_chars[residuo] + hex
        dec //= 16
        
    return hex

def Hex_Dec(hex: str) -> str:
    hex = hex.upper()
    hex_chars = "0123456789ABCDEF"
    dec = 0
    potency = 0
    
    for digit in reversed(hex):
        value = hex_chars.index(digit)
        dec += value * (16 ** potency)
        potency += 1
    
    return str(dec)