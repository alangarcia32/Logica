from tkinter import *
import socket
from time import sleep

serverAddress = ('192.168.1.175', 2222)
bufferSize = 1024
UDPclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

height = 500
width = 900

root = Tk()
root.title("DOG FEEDER")

def refresh():
    command = "get_data"
    UDPclient.sendto(command.encode('utf-8'), serverAddress)
    
    data, address = UDPclient.recvfrom(bufferSize)
    data = data.decode('utf-8')
    dataArray = data.split(':')        
    
    frame = Frame(root, bg = "#222831")
    frame.place(relwidth = 1, relheight = 1)

    printTemp = Label(frame, text = "Temperatura: " + dataArray[0], bg = "#222831", fg = "gray", font = "Ubuntu 18 bold", padx = 20, pady = 20)
    printTemp.place(rely = 0.1, relx = 0.1, relheight = 0.1, relwidth = 0.3)

    printHume = Label(frame, text = "Humedad: " + dataArray[1], bg = "#222831", fg = "gray", font = "Ubuntu 18 bold", padx = 20, pady = 20)
    printHume.place(rely = 0.3, relx = 0.1, relheight = 0.1, relwidth = 0.3)

    printWeight = Label(frame, text = "Distancia: " + dataArray[2], bg = "#222831", fg = "gray", font = "Ubuntu 18 bold", padx = 20, pady = 20)
    printWeight.place(rely = 0.5, relx = 0.1, relheight = 0.1, relwidth = 0.3)

    referscar = Button(frame, text = "Refrescar", bg = "#00ADB5", fg = "black", font = "Raleway 11 bold", padx = 7, pady = 7, activebackground = "black",
                       activeforeground = "white", relief = "flat", highlightbackground = "#112D4E", command = refresh)
    referscar.place(rely = 0.75, relx = 0.2, relheight = 0.13, relwidth = 0.2)

    cerrar = Button(frame, text = "Cerra el Programa", bg = "#00ADB5", fg = "black", font = "Raleway 11 bold", padx = 7, pady = 7, activebackground = "black",
                    activeforeground = "white", relief = "flat", highlightcolor = "#112D4E", command = CloseWindow)
    cerrar.place(rely = 0.75, relx = 0.6, relheight = 0.13, relwidth = 0.2)

def CloseWindow():
    root.quit()

try:
    canvas = Canvas(root, height = height, width = width)
    canvas.pack()
    
    command = "get_data"
    UDPclient.sendto(command.encode('utf-8'), serverAddress)
    
    data, address = UDPclient.recvfrom(bufferSize)
    data = data.decode('utf-8')
    dataArray = data.split(':')      

    frame = Frame(root, bg = "#222831")
    frame.place(relwidth = 1, relheight = 1)

    printTemp = Label(frame, text = "Temperatura: " + dataArray[0], bg = "#222831", fg = "gray", font = "Ubuntu 18 bold", padx = 20, pady = 20)
    printTemp.place(rely = 0.1, relx = 0.1, relheight = 0.1, relwidth = 0.3)

    printHume = Label(frame, text = "Humedad: " + dataArray[1], bg = "#222831", fg = "gray", font = "Ubuntu 18 bold", padx = 20, pady = 20)
    printHume.place(rely = 0.3, relx = 0.1, relheight = 0.1, relwidth = 0.3)

    printWeight = Label(frame, text = "Distancia: " + dataArray[2], bg = "#222831", fg = "gray", font = "Ubuntu 18 bold", padx = 20, pady = 20)
    printWeight.place(rely = 0.5, relx = 0.1, relheight = 0.1, relwidth = 0.3)

    referscar = Button(frame, text = "Refrescar", bg = "#00ADB5", fg = "black", font = "Raleway 11 bold", padx = 7, pady = 7, activebackground = "black",
                       activeforeground = "white", relief = "flat", highlightbackground = "#112D4E", command = refresh)
    referscar.place(rely = 0.75, relx = 0.2, relheight = 0.13, relwidth = 0.2)

    cerrar = Button(frame, text = "Cerra el Programa", bg = "#00ADB5", fg = "black", font = "Raleway 11 bold", padx = 7, pady = 7, activebackground = "black",
                    activeforeground = "white", relief = "flat", highlightcolor = "#112D4E", command = CloseWindow)
    cerrar.place(rely = 0.75, relx = 0.6, relheight = 0.13, relwidth = 0.2)
    
    root.mainloop()

except Exception as e:
    print("An error occurred:", e)

finally:
    UDPclient.close()