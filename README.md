[![QMK: Compatible](https://img.shields.io/badge/QMK-Compatible-success)](https://github.com/qmk/qmk_firmware)
[![License: CERN Open Hardware Licence v1.2](https://img.shields.io/badge/license-CERN%20Open%20Hardware%20Licence%20v1.2-blue)](https://github.com/Daneski13/Junco/blob/main/LICENSE)

<h1 align="center">Junco</h1>

Junco is a Raspberry Pi Pico powered split keyboard boasting a 4x6 layout with an aggressive columnar stagger. It has 5 "thumb" keys and support for 2-4 rotary encoders.

Junco is inspired by the excellent [crkbd](https://github.com/foostan/crkbd), [Iris](https://keeb.io/collections/iris-split-ergonomic-keyboard/products/iris-keyboard-split-ergonomic-keyboard), and [Kimiko](https://github.com/Keycapsss/Kimiko) keyboards.

## Table of Contents  <!-- omit from toc -->
- [Design and Quirks](#design-and-quirks)
- [Photos](#photos)
- [Build Guide / Assembly](#build-guide--assembly)
  - [Parts](#parts)
    - [Required](#required)
    - [Optional](#optional)
  - [Soldering](#soldering)

## Design and Quirks

The Junco was designed be a low-cost and feature-rich split keyboard for MX Style switches, supporting per key RGB lighting and up to 4 rotary encoders. It was built to support the RP2040 powered Raspberry Pi Pico which offers superior flash storage and processing power at a lower cost compared to the more common ATMega32 powered ProMicro that is used in many keyboards. TODO: Design Philosophy

Unfortunately, the Junco suffers from a few design "quirks":

- The switches, and by extension RGB LEDs are "upside down."
  - Typically the LED is directly under the legend of the keycap, on the upper-half of the switch. On the Junco, the LEDs are on the lower-half of the switch. This leads to much less vibrant keycap legends in comparison which may bother some.
- The case assumes that the Pico is mounted on the backside of the PCB with headers. If soldering the Pico with headers, a bit of header will be exposed on the front side of the PCB, so the switch plate will not sit flush with the PCB requiring removal of material from the switch plate.

## Photos

## Build Guide / Assembly

### Parts

#### Required

Where "58-60" is the count, 60 is needed with 2 rotary encoders. subtract from 60 every additional encoder after 2 (4 encoders 58 is needed, with 3 encoders 59 is needed).

| Name | Count | Remarks | Potential Link |
|---|---|---|---|
| PCB | 2 |  |  |
| Kailh Hotswap Socket | 58-60 |  |  |
| SMD Diodes | 60 | SOD-123 1N4148 | [AliExpress](https://www.aliexpress.us/item/2251832663565152.html) |
| Raspberry Pi Pico | 2 | PCB is specifically designed with the official Pico and YD-2040 type clone in mind, however several [other clone types](https://docs.google.com/spreadsheets/d/1LPjy6F5lHfUkmsrM5zlZmc5auYy5YBakW8Awe6hYFWo) should be compatible. Also, the case is currently designed assuming the Pico is soldered with [headers](https://www.sparkfun.com/products/17907),  but surface mount of the Pico is supported on the PCB.  | [AliExpress](https://www.aliexpress.us/item/3256803909832318.html) |
| TRRS Jack | 2 | PJ-320A | [AliExpress](https://www.aliexpress.us/item/2255800474897706.html) |
| TRRS Cable (3.5mm "Headphone" Cable) | 1 | TRRS (4 pole) is currently required, not TRS (3 pole) |  |
| Key Switches | 58-60 |  |  |
| Key Cap | 58-60 |  |  |
| Rotary Encoder and Cap | 2-4 | EC-11 Rotary Encoder | [AliExpress](https://www.aliexpress.us/item/2261799870168498.html) |
| M3 6mm or 6mm+ Screw and Nut | 8 |  |  |
| Case | 1 Left Set, 1 Right Set | Case files are located in the [case folder](./Case) |  |
| Micro USB Cable or USB-C Cable | 1 | USB cable for connecting the keyboard to your computer, dependent on what the Pico you chose uses. |  |

#### Optional

These parts are necessary for the RGB lighting.

| Name | Count | Remarks | Potential Link |
|---|---|---|---|
| Voltage Level Shifter/ Bus Buffer | 2 | SOT23-5 74AHCT1G125 | [AliExpress](https://www.aliexpress.us/item/3256803831434811.html) |
| RGB SMD LEDs | 60 | The 3MA SK6803MINI-E is highly recommended over the more traditional 12MA SK6812MINI-E due to its smaller current draw, allowing the LEDs to be brighter without drawing too much power. | [AliExpress](https://www.aliexpress.us/item/3256803450292556.html) |

### Soldering
