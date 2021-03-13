from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

oled = SSD1306_I2C(128, 64, i2c)

while True:
    regb = "00111011"
    regi = "00111010"
    alu = "00101001"

    rega0 = machine.Pin(2).value()
    rega1 = machine.Pin(3).value()
    rega2 = machine.Pin(4).value()
    rega3 = machine.Pin(5).value()
    rega4 = machine.Pin(6).value()
    rega5 = machine.Pin(7).value()
    rega6 = machine.Pin(8).value()
    rega7 = machine.Pin(9).value()
    rega = str(rega0) + str(rega1) + str(rega2) + str(rega3) + str(rega4) + str(rega5) + str(rega6) + str(rega7)

    regb0 = machine.Pin(10).value()
    regb1 = machine.Pin(11).value()
    regb2 = machine.Pin(12).value()
    regb3 = machine.Pin(13).value()
    regb4 = machine.Pin(14).value()
    regb5 = machine.Pin(15).value()
    regb6 = machine.Pin(16).value()
    regb7 = machine.Pin(17).value()
    regb = str(regb0) + str(regb1) + str(regb2) + str(regb3) + str(regb4) + str(regb5) + str(regb6) + str(regb7)

    alu0 = machine.Pin(18).value()
    alu1 = machine.Pin(19).value()
    alu2 = machine.Pin(20).value()
    alu3 = machine.Pin(21).value()
    alu4 = machine.Pin(22).value()
    alu5 = machine.Pin(26).value()
    alu6 = machine.Pin(27).value()
    alu7 = machine.Pin(28).value()
    alu = str(alu0) + str(alu1) + str(alu2) + str(alu3) + str(alu4) + str(alu5) + str(alu6) + str(alu7)



    oled.text("Binary Display", 5, 0)
    oled.text("", 5, 10)
    oled.text("Reg A "+ str(rega), 0, 20)
    oled.text("Reg B "+ str(regb), 0, 30)
    oled.text("ALU   "+ str(alu), 0, 40)



    oled.show()
    sleep(1)
    oled.fill(0)