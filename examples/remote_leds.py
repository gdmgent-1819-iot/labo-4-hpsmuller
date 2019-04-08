import time
from bluezero import microbit
# xx moet vervangen worden door het adres van de raspberry pi
# yy moet vervangen worden door het adres van de microbit
# beide kunne worden gevonden in de terminal
ubit = microbit.Microbit(adapter_addr='xx:xx:xx:xx:xx:xx',
                         device_addr='yy:yy:yy:yy:yy:yy',
                         accelerometer_service=True,
                         button_service=True,
                         led_service=True,
                         magnetometer_service=False,
                         pin_service=False,
                         temperature_service=True)
ubit.connect()
while ubit.button_a < 1:
    ubit.pixels = [0b00000, 0b01000, 0b11111, 0b01000, 0b00000]
    time.sleep(0.5)
    ubit.clear_display()

while ubit.button_b < 1:
    ubit.pixels = [0b00000, 0b00010, 0b11111, 0b00010, 0b00000]
    time.sleep(0.5)
    ubit.clear_display()

ubit.disconnect()