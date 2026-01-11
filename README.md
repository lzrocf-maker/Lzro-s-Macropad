# ⌨️ Lzro's_Macropad

A custom-designed 10-key mechanical macropad with an integrated RGB ring, powered by the **Seeed Studio XIAO RP2040** and **KMK Firmware**.

## 🚀 Project Overview
**Lzro's_Macropad** is a DIY productivity tool designed for efficiency. It features a custom PCB with a direct GPIO mapping (no diodes required) and a semi-translucent 3D-printed enclosure for optimized RGB lighting effects.

## 🛠 Hardware Specifications
- **Microcontroller:** Seeed Studio XIAO RP2040 (RP2040 ARM Cortex M0+).
- **Switches:** 10x MX-compatible mechanical switches.
- **Lighting:** 16x addressable RGB LEDs (WS2812B/SK6812) in a ring configuration.
- **Mounting:** M3 hardware with heat-set inserts for a professional finish.

## 📌 Pinout Reference
Based on the custom KiCad PCB schematic:

| Component | XIAO Pin | GPIO |
| :--- | :--- | :--- |
| **Switches 1-4** | D26, D27, D28, D29 | GPIO26, 27, 28, 29 |
| **Switches 5-6** | D6, D7 | GPIO6, 7 |
| **Switches 7-10**| D0, D1, D2, D3 | GPIO0, 1, 2, 3 |
| **RGB Data** | D4 | GPIO4 |

## 🏗️ 3D Enclosure & Assembly
The case consists of two 3D-printed parts designed for a secure and clean assembly:

- **Top Plate:** 2mm thick main body (printed in black). It features **three 0.20mm thin sections** (printed in white/translucent) that act as light diffusers for the internal LEDs. It uses **M3 heat-set inserts** in the corners.
- **Bottom Base:** Features countersunk holes for M3 screws. 
- **Assembly:** The unit is held together by four M3 screws. Two screws pass through integrated mounting holes in the PCB, while the other two provide clamping pressure, securing the board between the top and bottom plates.

## 💻 Firmware
This project runs **KMK** on **CircuitPython**. 

**Main advantages:**
- No complex build environment needed.
- Instant keymap customization by editing `code.py`.
- Native support for the RP2040's features.

## 📁 Repository Contents
- **/hardware**: KiCad PCB design files (`.kicad_pcb`, `.kicad_sch`) and manufacturing Gerbers.
- **/firmware**: `code.py` configuration and KMK library setup.
- **/3d_models**: STL files for the Top Plate and Bottom Base.
- **/assets**: Renders (including `image_4ffce3.png`) and schematic screenshots.
