from pynput import keyboard as kb
import serial

arduino = serial.Serial('COM4', 9600)

def pulsa(tecla):
    if(tecla == kb.KeyCode.from_char('w')):
        arduino.write("A".encode())

    if(tecla == kb.KeyCode.from_char('q')):
        return False

def suelta(tecla):
    if(tecla == kb.KeyCode.from_char('w')):
        arduino.write("B".encode())



with kb.Listener(pulsa, suelta) as escuchador:
	escuchador.join()