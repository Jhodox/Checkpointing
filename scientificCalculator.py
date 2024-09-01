import tkinter as tk
from tkinter import END
import math
import re
import pickle
import os

from functions import *

filename = "display.pkl"

number1 = 0
result = 0

#region screen
def save() -> None:
    # 'wb' Abrir el archivo en modo escritura binaria
    with open(filename, 'wb') as file:
        pickle.dump(display.get(), file)

def load_file() -> None:
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
    # 'rb' Abrir el archivo en modo lectura binaria
        with open(filename, 'rb') as file:
            loaded_data = pickle.load(file)
        
        print(loaded_data)
        if loaded_data != "0":
            cleanZero()
            display.insert(0, loaded_data)
            try:
                updateConversor(int(loaded_data))
            except:
                print("[-] Error al restaurar la ultima conversión")
    
def addToDisplay(event) -> None:
    cleanZero()
    display.insert(END, event.widget['text'])
    save()

def add(number: int) -> None: 
    cleanZero()
    display.insert(END, number)

# FIXME: agregar en cualquier momento -
def addSimbol(simbol: str) -> None:
    text = display.get()
    
    if text == "0":
        if simbol != "-":
            return
    
    if lastIsSimbol(text): return
    
    cleanZero()
    display.insert(END, simbol)

def updateConversor(dec :int) -> None:
    bin = Dec_Bin(dec)
    lblHex.config(text=Dec_Hex(dec))
    lblDec.config(text=Bin_Dec(bin))
    lblOct.config(text=Dec_Oct(dec))
    lblBin.config(text=bin)

def validateZero(event) -> None:
    if display.get() == "0": return
    addToDisplay(event)

def validateZeroWithText() -> None:
    if display.get() == "0": return
    add(0)

def cleanZero() -> None:
    text = display.get()
    if text == "0": 
        display.delete(0, END)

def addSimbol(simbol: str) -> None:
    text = display.get()
    
    if text == "0":
        if simbol != "-":
            return
    
    if lastIsSimbol(text): return
    
    cleanZero()
    display.insert(END, simbol)
    save()

def addFactorial() -> None:
    text = display.get()
    
    if lastIsSimbol(text): return
    
    # Permite el factorial de 0
    if text != "0":
        cleanZero()
    
    display.insert(END, "!")
    save()
    
def delete(event) -> None:
    if display.get() == "0": return
    
    position = len(display.get())
    display.delete(position-1, position)
    
    if len(display.get()) == 0:
        display.insert(END, "0")
    
    save()
    
def deleteAll(event) -> None:
    display.delete(0, END)
    display.insert(END, "0")
    save()

def addDot() -> None:
    text = display.get()

    # La cadena esta vacia
    if text == "":
        display.insert(0, "0")
    
    if existDot(text): return

    # EL ultimo valor es un simbolo
    for simbol in simbols:
        if simbol == text[-1]:
            display.insert(END, "0")
    
    display.insert(END, ".")
    save()

def addSqrt() -> None:
    text = display.get()

    # La cadena esta vacia
    cleanZero()
    
    if not lastIsSimbol(text) and text != "0": return
    
    display.insert(END, "√")
    
    save()

#region change keyboard
def change_keyboard():
    # print("Conversión: ", converterValue.get())
    if converterValue.get() == "hex":
        btnA["state"] = tk.NORMAL
        btnB["state"] = tk.NORMAL
        btnC["state"] = tk.NORMAL
        btnD["state"] = tk.NORMAL
        btnE["state"] = tk.NORMAL
        btnF["state"] = tk.NORMAL
        
        btnTwo["state"] = tk.NORMAL
        btnThree["state"] = tk.NORMAL
        btnFour["state"] = tk.NORMAL
        btnFive["state"] = tk.NORMAL
        btnSix["state"] = tk.NORMAL
        btnSeven["state"] = tk.NORMAL
        btnEight["state"] = tk.NORMAL
        btnNine["state"] = tk.NORMAL
        
        btnLog["state"] = tk.DISABLED
        btnSquareRoot["state"] = tk.DISABLED
        
        btnPotency["state"] = tk.DISABLED
        btnmodule["state"] = tk.DISABLED
        btnFactorial["state"] = tk.DISABLED
        btnDivision["state"] = tk.DISABLED
        
        btnMultiplication["state"] = tk.DISABLED
        
        btnSubtraction["state"] = tk.DISABLED
        
        btnSum["state"] = tk.DISABLED
        
        btnAbs["state"] = tk.DISABLED
        btnDot["state"] = tk.DISABLED

    if converterValue.get() == "oct":
        btnA["state"] = tk.DISABLED
        btnB["state"] = tk.DISABLED
        btnC["state"] = tk.DISABLED
        btnD["state"] = tk.DISABLED
        btnE["state"] = tk.DISABLED
        btnF["state"] = tk.DISABLED
        
        btnTwo["state"] = tk.NORMAL
        btnThree["state"] = tk.NORMAL
        btnFour["state"] = tk.NORMAL
        btnFive["state"] = tk.NORMAL
        btnSix["state"] = tk.NORMAL
        btnSeven["state"] = tk.NORMAL
        btnEight["state"] = tk.DISABLED
        btnNine["state"] = tk.DISABLED
        
        btnLog["state"] = tk.DISABLED
        btnSquareRoot["state"] = tk.DISABLED
        
        btnPotency["state"] = tk.DISABLED
        btnmodule["state"] = tk.DISABLED
        btnFactorial["state"] = tk.DISABLED
        btnDivision["state"] = tk.DISABLED
        
        btnMultiplication["state"] = tk.DISABLED
        
        btnSubtraction["state"] = tk.DISABLED
        
        btnSum["state"] = tk.DISABLED
        
        btnAbs["state"] = tk.DISABLED
        btnDot["state"] = tk.DISABLED

    if converterValue.get() == "bin":
        btnA["state"] = tk.DISABLED
        btnB["state"] = tk.DISABLED
        btnC["state"] = tk.DISABLED
        btnD["state"] = tk.DISABLED
        btnE["state"] = tk.DISABLED
        btnF["state"] = tk.DISABLED
        
        btnTwo["state"] = tk.DISABLED
        btnThree["state"] = tk.DISABLED
        btnFour["state"] = tk.DISABLED
        btnFive["state"] = tk.DISABLED
        btnSix["state"] = tk.DISABLED
        btnSeven["state"] = tk.DISABLED
        btnEight["state"] = tk.DISABLED
        btnNine["state"] = tk.DISABLED
        
        btnLog["state"] = tk.DISABLED
        btnSquareRoot["state"] = tk.DISABLED
        
        btnPotency["state"] = tk.DISABLED
        btnmodule["state"] = tk.DISABLED
        btnFactorial["state"] = tk.DISABLED
        btnDivision["state"] = tk.DISABLED
        
        btnMultiplication["state"] = tk.DISABLED
        
        btnSubtraction["state"] = tk.DISABLED
        
        btnSum["state"] = tk.DISABLED
        
        btnAbs["state"] = tk.DISABLED
        btnDot["state"] = tk.DISABLED

    if converterValue.get() == "dec":
        btnA["state"] = tk.NORMAL
        btnB["state"] = tk.NORMAL
        btnC["state"] = tk.NORMAL
        btnD["state"] = tk.NORMAL
        btnE["state"] = tk.NORMAL
        btnF["state"] = tk.NORMAL
        
        btnTwo["state"] = tk.NORMAL
        btnThree["state"] = tk.NORMAL
        btnFour["state"] = tk.NORMAL
        btnFive["state"] = tk.NORMAL
        btnSix["state"] = tk.NORMAL
        btnSeven["state"] = tk.NORMAL
        btnEight["state"] = tk.NORMAL
        btnNine["state"] = tk.NORMAL
        
        btnLog["state"] = tk.NORMAL
        btnSquareRoot["state"] = tk.NORMAL
        
        btnPotency["state"] = tk.NORMAL
        btnmodule["state"] = tk.NORMAL
        btnFactorial["state"] = tk.NORMAL
        btnDivision["state"] = tk.NORMAL
        
        btnMultiplication["state"] = tk.NORMAL
        
        btnSubtraction["state"] = tk.NORMAL
        
        btnSum["state"] = tk.NORMAL
        
        btnAbs["state"] = tk.NORMAL
        btnDot["state"] = tk.NORMAL

#region resultado
def obtainResult() -> None:
    global number1
    global result
    
    text = display.get()

    if display.get() == "": return
    
    if converterValue.get() != "dec":
        conversion(text)
        return
    
    # Calcular factorial
    while text.find("!") != -1:
        text = calculateFactorial(text)
        
    while text.find("%") != -1:
        text = calculatePorcentaje(text)
    
    # Reemplazar caracter ^
    text = text.replace("^", "**")
    
    try:
        # Reemplaza la raiz cuadrada √
        result = eval(re.sub(r'√(\d+)', r'math.sqrt(\1)', text))
        print(f"Resultado: {result}")
        display.delete(0, END)
        display.insert(0, result)
        save()
    except ZeroDivisionError:
        print("[-] Trataste de dividir entre zero")
        return
    except:
        print("[-] No fue posible evaluar la expresión")
        return
    
    updateConversor(int(result) if int(result) >= 0 else 0)

#region extra operation
def potency() -> None:
    text = display.get()
    if text == "": return
    
    global number1
    global number2
    global result
    
    result = int(number1) ** int(number2)
    display.delete(0, END)
    display.insert(END, result)

def calculateFactorial(text: str) -> str:
    end = text.find("!")
    start = end - 1
    band = True
    
    # band como condición para evitar que se rompa en caso de que el metodo isdigit falle
    # NO se a comprobado que pueda fallar, puede ser inecesario
    while band:
        try:
            # El numero empieza desde la posición 0
            if text[start] == "-":
                return
            if text[start].isdigit():
                start -= 1
                if start == -1:
                  band = False
            else:
                band = False
        except:
            print("[-] No fue posible validar si era un digito")
            return
    
    start += 1
    tempText = text[start:end:1]
    numberResult = factorial(int(tempText))
    return text[:start] + str(numberResult) + text[end+1:]

def calculatePorcentaje(text: str) -> str:
    simbol = text.find("%")
    print(f"Index: {simbol}")
    
    #Segundo numero
    start = simbol - 1
    while text[start].isdecimal() and start > 0:
        start -= 1
    print(f"Index inicio: {start}")
    
    #Primer numero
    end = simbol + 1
    while text[end].isdecimal() and end < len(text) - 1:
        end += 1
    print(f"Index final: {end}")

    band = True
    
    secondNumber = float(text[start:simbol:1])
    if end == len(text) - 1:
        fistNumber = float(text[simbol+1:end+1:1])
    else:
        fistNumber = float(text[simbol+1:end:1])
    print(f"1: {fistNumber}")
    print(f"2: {secondNumber}")
    
    secondNumber = secondNumber / 100
    restemp = fistNumber * secondNumber
    if  end == len(text) - 1:
        res = text[:start] + str(restemp) + text[end:]
    else:
        res = text[:start+1] + str(restemp) + text[end:]
    print("Res: ", res)
    return str(res)

# No usado
def module() -> None:
    text = display.get()
    if text == "": return

    global number1
    global number2
    global result
    result = int(number1) % int(number2)
    display.delete(0, END)
    display.insert(END, result)
    
def absoluteNumber() -> None:
    text = display.get()
    
    if text == "0" or text == "": return
    if text[0] != "-": return
    
    #Metodo facil
    # display.delete(0, 1)
    # return
    
    try:
        # Se espera validar que el resto del display sea un entero o flotante
        for i in range(1, len(text)):
            if not (text[i].isdigit() or text[i] == "."): return
        display.delete(0, 1)
        save()
    except:
        print("[-] absoluteNumber no pudo evaluar")
        return

def conversion(num: str) -> None:
    if converterValue.get() == "hex":
        dec = Hex_Dec(num)
        # display.delete(0, END)
        # display.insert(0, dec)
        updateConversor(int(dec))
    elif converterValue.get() == "oct":
        dec = Oct_Dec(int(num))
        # display.delete(0, END)
        # display.insert(0, dec)
        updateConversor(int(dec))
    elif converterValue.get() == "bin":
        dec = Bin_Dec(num)
        # display.delete(0, END)
        # display.insert(0, dec)
        updateConversor(int(dec))
    # converterValue.set("dec")
    # change_keyboard()
    return

#region Main windows config
root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)
# root.geometry("400x600")

#Frames
converter = tk.Frame(root)
converter.grid(row=1, column=0)

#Display
display = tk.Entry(root, background="lightgray", font=("Arial", 16), justify="right", bd=3)
display.insert(0, "0")
display.grid(row=0, column=0, columnspan=5)

# Frame
converterFrame = tk.Frame(root)
converterFrame.grid(row=1, column=1, columnspan=4)

converterValue = tk.StringVar()
converterValue.set("dec")

optHex = tk.Radiobutton(converter, text="HEX", font=("Arial", 10), variable=converterValue, value="hex", command=change_keyboard, indicatoron=0)
optDec = tk.Radiobutton(converter, text="DEC", font=("Arial", 10), variable=converterValue, value="dec", command=change_keyboard, indicatoron=0)
optOct = tk.Radiobutton(converter, text="OCT", font=("Arial", 10), variable=converterValue, value="oct", command=change_keyboard, indicatoron=0)
optBin = tk.Radiobutton(converter, text="BIN ", font=("Arial", 10), variable=converterValue, value="bin", command=change_keyboard, indicatoron=0)
optHex.pack()
optDec.pack()
optOct.pack()
optBin.pack()

#region Converter
lblHex = tk.Label(converterFrame, text="0", justify="left")
lblHex.grid(row=0, column=0, sticky="w", padx=5)
lblDec = tk.Label(converterFrame, text="0", justify="left")
lblDec.grid(row=1, column=0, sticky="w", padx=5)
lblOct = tk.Label(converterFrame, text="0", justify="left")
lblOct.grid(row=2, column=0, sticky="w", padx=5)
lblBin = tk.Label(converterFrame, text="0", justify="left")
lblBin.grid(row=3, column=0, sticky="w", padx=5)

root.grid_columnconfigure(0, minsize=10)  # Ajusta el valor según sea necesario
root.grid_columnconfigure(1, minsize=10)

#region Keyboard
paddingX=2
paddingY=2
sizeX=5
sizeY=2

#region Row 1
btnA = tk.Button(root, text="A", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY)
btnA.grid(row=0+2, column=0)
btnA.bind("<Button-1>", addToDisplay)

btnLog = tk.Button(root, text="Log", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY)
btnLog.grid(row=0+2, column=1)

btnSquareRoot = tk.Button(root, text="√", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY, command=addSqrt)
btnSquareRoot.grid(row=0+2, column=2)

btnCE = tk.Button(root, text="CE", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY)
btnCE.grid(row=0+2, column=3)
btnCE.bind("<Button-1>", deleteAll)

btnDelete = tk.Button(root, text="<-", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY)
btnDelete.grid(row=0+2, column=4)
btnDelete.bind("<Button-1>", delete)

#region Row 2
btnB = tk.Button(root, text="B", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY)
btnB.grid(row=1+2, column=0)
btnB.bind("<Button-1>", addToDisplay)

btnPotency = tk.Button(root, text="^", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY, command=lambda: addSimbol("^"))
btnPotency.grid(row=1+2, column=1)

btnmodule = tk.Button(root, text="%", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY, command=lambda: addSimbol("%"))
btnmodule.grid(row=1+2, column=2)

btnFactorial = tk.Button(root, text="n!", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY, command=addFactorial)
btnFactorial.grid(row=1+2, column=3)

btnDivision = tk.Button(root, text="/", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY, command=lambda: addSimbol("/"))
btnDivision.grid(row=1+2, column=4)

#region Row 3
btnC = tk.Button(root, text="C", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY)
btnC.grid(row=2+2, column=0)
btnC.bind("<Button-1>", addToDisplay)

btnSeven = tk.Button(root, text="7", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY)
btnSeven.grid(row=2+2, column=1)
btnSeven.bind("<Button-1>", addToDisplay)

btnEight = tk.Button(root, text="8", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY)
btnEight.grid(row=2+2, column=2)
btnEight.bind("<Button-1>", addToDisplay)

btnNine = tk.Button(root, text="9", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY)
btnNine.grid(row=2+2, column=3)
btnNine.bind("<Button-1>", addToDisplay)

btnMultiplication = tk.Button(root, text="*", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY, command=lambda: addSimbol("*"))
btnMultiplication.grid(row=2+2, column=4)
# btnMultiplication.bind("<Button-1>", addSimbol)

#region Row 4
btnD = tk.Button(root, text="D", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY)
btnD.grid(row=3+2, column=0)
btnD.bind("<Button-1>", addToDisplay)

btnFour = tk.Button(root, text="4", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY)
btnFour.grid(row=3+2, column=1)
btnFour.bind("<Button-1>", addToDisplay)

btnFive = tk.Button(root, text="5", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY)
btnFive.grid(row=3+2, column=2)
btnFive.bind("<Button-1>", addToDisplay)

btnSix = tk.Button(root, text="6", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY)
btnSix.grid(row=3+2, column=3)
btnSix.bind("<Button-1>", addToDisplay)

btnSubtraction = tk.Button(root, text="-", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY, command=lambda: addSimbol("-"))
btnSubtraction.grid(row=3+2, column=4)

#region Row 5
btnE = tk.Button(root, text="E", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY)
btnE.grid(row=4+2, column=0)
btnE.bind("<Button-1>", addToDisplay)

btnOne = tk.Button(root, text="1", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY)
btnOne.grid(row=4+2, column=1)
btnOne.bind("<Button-1>", addToDisplay)

btnTwo = tk.Button(root, text="2", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY)
btnTwo.grid(row=4+2, column=2)
btnTwo.bind("<Button-1>", addToDisplay)

btnThree = tk.Button(root, text="3", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY)
btnThree.grid(row=4+2, column=3)
btnThree.bind("<Button-1>", addToDisplay)

btnSum = tk.Button(root, text="+", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY, command=lambda: addSimbol("+"))
btnSum.grid(row=4+2, column=4)

#region Row 6
btnF = tk.Button(root, text="F", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY)
btnF.grid(row=5+2, column=0)
btnF.bind("<Button-1>", addToDisplay)

btnAbs = tk.Button(root, text="Abs", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY, command=absoluteNumber)
btnAbs.grid(row=5+2, column=1)

btnZero = tk.Button(root, text="0", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY)
btnZero.grid(row=5+2, column=2)
btnZero.bind("<Button-1>", validateZero)

btnDot = tk.Button(root, text=".", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY, command=addDot)
btnDot.grid(row=5+2, column=3)

btnEqual = tk.Button(root, text="=", padx=paddingX, pady=paddingY, width=sizeX, height=sizeY, command=obtainResult)
btnEqual.grid(row=5+2, column=4)

load_file()

#region on_key_press
def on_key_press(event):
    # print(event)
    # 1-9
    # for i in range(1, 10):
    #     if event.char == str(i):
    #         add(str(i))
    
    # 0
    # if event.char == "0":
    #     validateZeroWithText()
    
    # if event.char == ".":
    #     addDot()

    # Backspace
    # if event.char == "\x08":
    #     delete(event)
        
    # Enter, return
    if event.char == "\r":
        obtainResult()

root.bind("<KeyPress>", on_key_press)

root.mainloop()