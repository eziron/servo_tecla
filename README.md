# servo_tecla

## Librerias necesarias
    pip install pyserial pynput
    
debes asegurarte de cual es el puerto COM en que está tu arduino, lo puedes ver en el IDE de arduino o en administrador de dispositivos, Puertos (COM y LPT)
## lo debes cambiar en tecla.py en la linea 
    arduino = serial.Serial('COM4', 9600)

Cambiando el numero del puerto COM a tu numero respectivo
