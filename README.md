# Lzro's_Macropad

This is a custom-built macropad for various usecases. The goal is to have different macros for different apps so that when you change app the macros change. It also has a ring with SK6812Mini LEDs. It has 10 mx cherry switches for the macro buttons.

<img width="1161" height="751" alt="Captura de pantalla 2026-01-11 232131" src="https://github.com/user-attachments/assets/fe94f06e-7f76-4ad2-92f7-5a571a116bee" />

## Project Overview
I have built this macropad so that every switch is directly connected to one GPIO pin on the XIAO RP2040. A feature that will be added some time in the near future is LED reactivity, so that when you click a button, the LEDs make a wave from were the button is located.

## Hardware Specifications
- **Microcontroller:** Seeed Studio XIAO RP2040.
- **Switches:** 10x MX mechanical switches.
- **Lighting:** 16x addressable RGB LEDs (SK6812 Mini) in three stripes (all connected to one GPIO pin).
- **Mounting:** M3 hardware with heat-set inserts with a 3d printed case printed in to halves.

## Pinout Reference
These are the pinouts of the XIAO board to all the components:

| Component | XIAO Pin | GPIO |
| :--- | :--- | :--- |
| **Switches 1-4** | D26, D27, D28, D29 | GPIO26, 27, 28, 29 |
| **Switches 5-6** | D6, D7 | GPIO6, 7 |
| **Switches 7-10**| D0, D1, D2, D3 | GPIO0, 1, 2, 3 |
| **RGB Data** | D4 | GPIO4 |

<img width="1284" height="887" alt="Captura de pantalla 2026-01-11 232509" src="https://github.com/user-attachments/assets/50e428c4-edaf-4ae9-9818-3a3c369ed380" />
<img width="794" height="577" alt="Captura de pantalla 2026-01-11 232618" src="https://github.com/user-attachments/assets/403f2fb2-2698-4a3f-9c84-dfbea0e64783" />
<img width="928" height="674" alt="Captura de pantalla 2026-01-11 232704" src="https://github.com/user-attachments/assets/096f7409-d9dc-4fb9-b025-3bdb12b5b1d7" />

## 3D Enclosure & Assembly
I designed the case so that you only have to print 2 parts, the two halves come together with 4 M3 screws and heat-set inserts:

- **Top Plate:** I designed the top part with the cutouts for the 10 switches as well as a cutout to see the controller and a bit of the PCB, I also added 3 0.20mm thick stripes as diffusers for the LED lights (wich can be printed in white while the rest of the body is printed in black. If you don't have a multicolor 3d printer you can print the entire to part in white, although there will be light bleed.
  <img width="1152" height="708" alt="Captura de pantalla 2026-01-11 231522" src="https://github.com/user-attachments/assets/439fa932-70f4-4c89-bf70-96fb10f4ff93" />
- **Bottom Base:** The bottom part features a recesed part so that the pins of the switches do not crash onto the case. It also has 4 countersunc holes for the 4 M3 screws. Some anti-slip pads can be added beside the holes for better grip on the desk, although it is not needed for it to function.
  <img width="1157" height="741" alt="Captura de pantalla 2026-01-11 231456" src="https://github.com/user-attachments/assets/a09196a4-af7d-45cc-8bd0-67fa40704229" />
  

## Firmware
This project runs **KMK** on **CircuitPython**.

## Repository Contents
- The files ended on .kicad_sch/pro/pcb are the PCB files.
- The Gerbers.zip contains the files for PCB manufacturing.
- The files with the name screenshot contain photos of the product.
- The file code.py contains the core firmware for the pcb to work (it can be changed to your specific needs).
- Lzro's_Macropad.step contains the 3d model of the macropad.
- The BOM file contains all the list of materials needed for manufacturing this project.
