# 8-Bit BreadBoard Computer Pico Display
 
This is a simple MicroPython scipt that leverages the ssd1366 library [Github](https://github.com/stlehmann/micropython-ssd1306) and checks for 24 input pins for wether they are high-low.  This allows for 3 sets of 8-bit buses.  So for example, if your building [Ben Eaters 8-Bit Breadboard Computer](https://eater.net/8bit) then you could use this script to display the contents of the A & B Registers and the ALU.

The hardware is simple.  Just one [Raspberry Pi Pico](https://www.raspberrypi.org/products/raspberry-pi-pico/),and one SSD1366 0.96" Oled Screen[SSD1366 0.96" Oled Screen](https://www.aliexpress.com/item/32896971385.html?spm=a2g0o.productlist.0.0.11c014f2CbemBp&algo_pvid=a69887ef-3c42-4623-a629-12002ee8da4b&algo_expid=a69887ef-3c42-4623-a629-12002ee8da4b-2&btsid=2100bb4716156062543096043e20a0&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_).

You then simply add the Python Script and library from this repo and connect up the Oled via I2C.   [Getting Started](https://www.tomshardware.com/uk/how-to/oled-display-raspberry-pi-pico)


<img src="https://github.com/djh82uk/8-Bit-BreadBoard-Computer-Pico-Display/blob/main/Oled-Display.jpg" width="200" height="200" />
