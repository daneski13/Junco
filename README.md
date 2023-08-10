<h1 align="center">Junco</h1>

[![License: CERN Open Hardware Licence v2](https://img.shields.io/badge/license-CERN%20Open%20Hardware%20Licence%20v2-blue)](./LICENSE)

[![QMK: Compatibility](https://img.shields.io/badge/QMK-Powered-brightgreen?logo=data:image/png;base64,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)](https://github.com/qmk/qmk_firmware)
[![VIA: Compatibility](https://img.shields.io/badge/VIA-Supported-brightgreen?logo=data:image/png;base64,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)](https://usevia.app/)

Named after a small North American bird, Junco is a 60% Raspberry Pi Pico powered split keyboard boasting a 4x6 layout with an aggressive columnar stagger, 2-4 rotary encoders, and per-key RGB lighting.

![Junco](./img/Junco.webp)

Want to contribute? Check out [Contributing](./CONTRIBUTING.md).

Junco is inspired by the excellent [crkbd](https://github.com/foostan/crkbd), [Iris](https://keeb.io/collections/iris-split-ergonomic-keyboard/products/iris-keyboard-split-ergonomic-keyboard), [Kimiko](https://github.com/Keycapsss/Kimiko), [Sofle](https://github.com/josefadamcik/SofleKeyboard), and [Ferris](https://github.com/pierrechevalier83/ferris) keyboards.

- [Design Philosophy and Quirks](#design-philosophy-and-quirks)
  - [Philosophy](#philosophy)
  - [Quirks](#quirks)
- [Build Guide / Assembly](#build-guide--assembly)
  - [Parts](#parts)
    - [Required](#required)
    - [Optional - RGB](#optional---rgb)
  - [Soldering](#soldering)
    - [Diodes](#diodes)
    - [RGB (Optional)](#rgb-optional)
    - [Pico](#pico)
    - [Hot-swap Sockets](#hot-swap-sockets)
    - [TRRS jack and Rotary Encoders](#trrs-jack-and-rotary-encoders)
  - [Case](#case)
  - [Flashing the firmware](#flashing-the-firmware)
- [Troubleshooting](#troubleshooting)
  - [No LEDs are working](#no-leds-are-working)
  - [Some LEDs are not working](#some-leds-are-not-working)
  - [An entire row or column of keys is not working](#an-entire-row-or-column-of-keys-is-not-working)
  - [Random key or keys not working](#random-key-or-keys-not-working)

## Design Philosophy and Quirks

### Philosophy

In my search for an ergonomic split keyboard, I came across several great keyboards, but I craved a combination of features and ideas from several with my own flavor. Iris' aesthetics, Kimiko's stagger and layout, elements of Ferris' philosophy.

I also wanted to use Raspberry Pi Picos for the controller as it has many advantages over the ProMicro that is normally used in custom keyboards. At the time, Pico powered keyboards were not yet really a thing and weren't yet supported by the main QMK branch. Thus, I created my own keyboard.

The Junco was designed around a set of goals, similar in vain to the Ferris.

**Goals:**

- Low-Cost
- Raspberry Pi Pico / RP2040
  - Superior flash storage and processing power compared to the common ATMega32 ProMicro
  - Faster than STM32 blackpill with more flash storage at the same cost or less
- Comfort
  - Aggressive Columnar Stagger
- Aesthetics
  - Almost all soldering done on the backside of PCB, optional RGB
- 60% layout
  - Near perfect blend of compactness and easy use without crazy combos or layer gymnastics
- Multiple rotary encoder support
- Hot-swap switches
- Plug and play either side of the split
  - Convenience and traveling
  - Flexible cable management
- Minimal different parts and easy to source
  - No need to buy a different types of LEDs or diodes. No reset switches, capacitors, resistors etc. required.

**Non-goals:**

- Reversible PCB
  - Can make assembly confusing and more error prone
- Multi-switch support
  - MX switches should use MX spacing, Choc switches should use Choc spacing.
- OLED Support
  - OLEDs are an added cost and somewhat comprise the aesthetics in my opinion. Don't find useful for a keyboard, more of a novelty.

### Quirks

Being my first venture into keyboard design... Junco unfortunately suffers from a few "quirks" at the moment that may or may not bother you:

- The case files currently provided in this repo assume PCB mounted switches and uses a 3mm switch plate that is flush with the PCB. This presents some problems that a more proper suspended switch plate would not have:
  - Mounting the Pico on the backside with headers causes a bit of the header to be exposed on the front side of the PCB, so the switch plate provided in this repo will not sit flush with the PCB.
  - The TRRS jack is also soldered on the backside, causing another uneven surface for the switch plate.
  - Thus, material must be removed from the back of the switch plate in the proper places for a flush fit.
    - Heat-gunning the switch plate in the proper area, lining it up with the PCB, and squishing provides a quick and *dirty* solution if done correctly.
  - **PRs are welcome to improve upon the case files or to create new cases as I am a 3D design novice.** A proper fix would be to have the PCB rest on the middle section's lip about 1.5mm below the switch plate. This would also allow plate mounted switches to properly latch onto the switch plate.

## Build Guide / Assembly

### Parts

#### Required

Where "56-58" is the count, 58 is needed with 2 rotary encoders. subtract from 58 every additional encoder (4 encoders 56, with 3 encoders 57).

| Name                                 | Count                   | Remarks                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Potential Storefront                                                        |
| ------------------------------------ | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| PCB                                  | 2 (1 left and 1 right)  | PCBs can be ordered from manufacturers such as JLCPCB and LCSC                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                             |
| MX Hot-swap Sockets                  | 56-58                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                             |
| Diodes                           | 62                      |Surface mount SOD-123 1N4148, _or_ through-hole 1N4148 diode. These are both common and inexpensive, any one should do. Through hole is usually easier to solder.                                                                                                                                                                                                                                                                                                                                                                                                                                              | SMD: [AliExpress](https://www.aliexpress.us/item/2251832663565152.html) <br>[JLCPCB Part#: C2972760](https://jlcpcb.com/partdetail/3368026-1N4148SOD123/C2972760)<br> Through-hole: [AliExpress](https://www.aliexpress.us/item/2251832473773777.html)           |
| Raspberry Pi Picos                   | 2                       | PCB is specifically designed with the official Pico and YD-2040 type clone in mind, however several [other clone types](https://docs.google.com/spreadsheets/d/1LPjy6F5lHfUkmsrM5zlZmc5auYy5YBakW8Awe6hYFWo) should be compatible (Waveshare, WeAct, EstarDyn, Tenstar). Also, the case is currently designed assuming the Pico is soldered with [headers](https://www.sparkfun.com/products/17907), but surface mounting the Pico is supported on the PCB. | [AliExpress, YD-2040](https://www.aliexpress.us/item/3256803909832318.html) |
| TRRS Jacks                           | 2                       | PJ-320A                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [AliExpress](https://www.aliexpress.us/item/2255800474897706.html)          |
| TRRS Cable (3.5mm "Headphone" Cable) | 1                       | TRRS (4 pole) is currently required, not TRS (3 pole)                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                             |
| MX Style Switches                    | 56-58                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                             |
| Key Caps                             | 56-58                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                             |
| Rotary Encoders and Caps             | 2-4                     | EC-11 Rotary Encoder                                                                                                                                                                                                                                                                                                                                                                                                                                        | [AliExpress](https://www.aliexpress.us/item/2261799870168498.html)          |
| M3 6mm or 6mm+ Screws and Nuts       | 8                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                             |
| Case                                 | 1 Left Set, 1 Right Set | Case files are located in the [case folder](./Case).                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                             |
| Micro USB Cable or USB-C Cable       | 1                       | USB cable for connecting the keyboard to your computer, dependent on what the Pico you chose uses.                                                                                                                                                                                                                                                                                                                                                          |                                                                             |

#### Optional - RGB

These parts are necessary for the RGB lighting.

| Name                                          | Count | Remarks                                                                                                                                                                            | Potential Storefront                                               |
| --------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| 74AHCT1G125 Voltage Level Shifter/ Bus Buffer | 2     | SOT23-5 Footprint <br/> <br/> Required for LEDs to work properly, Pico runs at 3.3V while the LEDs will require 5V                                                                 | [AliExpress](https://www.aliexpress.us/item/3256803831434811.html) <br> [JLCPCB Part# C7484](https://jlcpcb.com/partdetail/TexasInstruments-SN74AHCT1G125DBVR/C7484)|
| RGB SMD LEDs (Prefer SK6803MINI-E)            | 74    | The 3MA SK6803MINI-E is highly recommended over the more traditional 12MA SK6812MINI-E due to its smaller current draw, allowing the LEDs to be very bright at manageable wattage. | [AliExpress](https://www.aliexpress.us/item/3256803450292556.html) <br> [JLCPCB Part# C5184589](https://jlcpcb.com/partdetail/Normand-SK6803MINIE/C5184589)|

### Soldering

The PCB is not reversible, there is a dedicated right and left half in the KiCad PCB files. Almost all of the soldering will occur on the backside of the PCB. 

#### Diodes

Solder the diodes as you see in the photo.
SMD diodes are soldered on the back of the board. 
Through-hole diodes are inserted on the back of the board, and soldered on the front.

**Note** that the diodes have polarity, ensure the line on the diode matches the silkscreen.

# @todo Get a phot of Through-hole diodes

![Soldered Diodes](./img/diodes.webp)

#### RGB (Optional)

All LEDs must be soldered to the PCB for RGB to work properly, even if you will not be using backlight or will be using an encoder that covers an LED. (They are wired in serial).

First solder the level shifter. It's tiny & squirrley - [drag soldering](https://www.youtube.com/watch?v=wUyetZ5RtPs)" is a good method. See photo:

![Level Shifter Soldered](./img/level_shifter.webp)

All LEDs will be soldered facing _down from you_. The LEDS for per-key RGB will be soldered on the back of the board, while the LED's for the underglow will be soldered on the front of the board.

**Note** the LED orientation is very important. One of the pads on each LED will be misshapen relative to the others, this pad should connect to the PCB pad that is marked by the L shape on the silkscreen. For a sanity check, a corner of the LED's front-side will also be "cut", this corner must also line up with the L shape on the silkscreen.

# @todo REWRITE this and add update pictures
Blue is LEDs that will face away from you, towards the front-side of the PCB for the per-key lighting. Red will face "up" at you for the underglow:

![LED Orientation](./img/LED_orientation.svg)

![LEDs Soldered](./img/LED.webp)

After you finish the next step of soldering the Pico to the PCB, recommend plugging the keyboard in and flashing QMK to ensure the LEDs are lighting up. If there are any issues, check the troubleshooting section.

#### Pico

If you are soldering the Pico surface mount style, go ahead with soldering it to the backside of the PCB and you can skip to the next section.

If you are soldering the Pico using headers, first solder the Pico to the headers and then the header/Pico to the PCB. 

**Ensure that you are soldering the Pico/Header onto the backside of the PCB.**

The best way to go about this method is to rest the shorter end of the headers in the through-holes of the PCB on a flat surface and place the Pico on top, through the longer end of the header. This will stabilize the headers somewhat and ensure proper spacing. Solder the Pico to the 2 header pins on the both the "top" and "bottom" of the Pico to hold it in place. Proceed to solder the Pico to the rest of the header's pins.

After the Pico is soldered to the header, flip the PCB over and solder the sticking-out header pins to the PCB. Start with the 2 "top" and 2 "bottom" header pins to hold it in place, being sure to minimize the space between the header's plastic and the PCB. Proceed to solder the PCB to the rest of the header's pins.

The end result will look like this:

Backside of PCB:

![Pico Soldered, PCB Backside](./img/pico_backside.webp)

Front-side of PCB:

![Pico Soldered, PCB Frontside](./img/pico_frontside.webp)

#### Hot-swap Sockets

Place hot-swap sockets on the backside of the PCB and solder. See photo:

![Hot-swap Sockets Soldered](./img/hotswap.webp)

#### TRRS jack and Rotary Encoders

The process for soldering the TRRS jack and the process for the rotary encoders are very similar.

On the **backside** of the PCB, place the TRRS jack. On the front-side of the PCB, bend the pins of the TRRS jack to "latch" onto the PCB and solder.

Backside PCB:

![TRRS Soldered, Backside](./img/trrs_backside.webp)

Front-side PCB:

![TRRS Soldered, Front-side](./img/trrs_frontside.webp)

On the **front-side** of the PCB, place the rotary encoder(s). On the backside of the PCB, bend the pins of the encoder to "latch" onto the PCB and solder.

Front-side PCB:

![Rotary Encoder Soldered, Front-side](./img/rotary_frontside.webp)

Backside PCB:

![Rotary Encoder Soldered, Back-side](./img/rotary_backside.webp)


### Case

At the moment, the case files included in the [case directory](./Case) support 3D printing of a case assuming PCB mounted switches (since the 3mm switch plate is resting on the PCB). Since I do not own or have easy access to a 3D printer, the case was designed to be easy to print with 3rd party printing services in-mind such as Treatstock.

Raw files are provided for designing your own case if you see fit. Further work on the case may occur in the future to properly suspend the switch plate. PRs are welcome.

The case is comprised of 4 parts, 8 M3 screws, and 8 M3 nuts.

To have a functional case you need the Bottom Left and Bottom Right along with a Left Switch Plate and a Right Switch Plate. 4 M3 screws and their nuts will hold the switch plate and bottom together for each side of the split. Recommend printing the bottom in white at 40% infill so the underglow LEDs can bleed through.

The naming schemes "- 2 Rotary" and "- 4 Rotary" are products of the raw files used to model the case.

The switch plates named "- 2 Rotary" assume 1 rotary encoder will be used on that side of the split. One by they thumb keys.

The switch plates named "- 4 Rotary" assume 2 rotary encoders will be used on that side of the split. One by the thumb keys and one in the far bottom corner

If you would like to have 3 rotary encoders rather than 2 total or 4 total you would use both variants. The side that will have 2 rotary encoders will use the "- 4 Rotary", while the other side with 1 rotary encoder will use the "- 2 Rotary".

As mentioned in [design quirks](#quirks), there are some problems with making the switch plate flush with the PCB. After you get it flush, you can completely assemble your keyboard! Assembly goes in the reverse of the following:

-- Keycaps --

-- Switches --

-- Case Switch Plate -- (screw + nut connect the plate with the bottom)

-- PCB --

-- Case Bottom --

### Flashing the firmware

Junco is powered by the QMK firmware, see the [build environment setup](https://docs.qmk.fm/#/getting_started_build_tools). Brand new to QMK? Start with the [Complete Newbs Guide](https://docs.qmk.fm/#/newbs).

Flashing instructions can be found [here](https://github.com/qmk/qmk_firmware/tree/master/keyboards/junco).

Congratulations and enjoy your split keyboard!

## Troubleshooting

### No LEDs are working

Try the following until problem solved:

1. Ensure the level shifter is properly soldered onto the PCB, re-solder as needed.
2. There is a diode without a corresponding switch located to the top right of the Pico on both sides of the split, check and re-solder that diode as needed.
    1. Short the pads on either side of the diode on both halves.
       1. If some the LEDs turn on, re-solder the diodes. Replace it if problem persists.
       2. If no LEDs turn on after shorting the diode's pads, there is likely a problem with the first LED, move to the next section for the first LED in the electrical order. If that still doesn't work, the level shifter is likely damaged and needs to be replaced.

### Some LEDs are not working

Go through the LED electrical order (pictured below) until you reach the problem LED. That LED **or** the one previous to it has a problem.

LED Electrical Order (1-8 are underglow):

![LED Order](./img/LED_order.webp)

Right side is identical but mirrored.

Try the following until problem solved:

1. Check that the pads of LED not turning on and its previous are soldered correctly, re-solder for a better connection as needed.
2. Double check that the LED not turning on is in the correct orientation.
3. If the soldering looks good and the orientation is correct, try re-soldering all the pads any way for good measure.
4. If re-soldering didn't work than the LED is likely dead or damaged in which case replace it.

### An entire row or column of keys is not working

In this case, there is most likely a problem with the PCB's connection to the Pico. Note that the bottom row of keys is staggered by 2, so the the corresponding matrix column is shifted.

Rows:

![Matrix Rows](./img/Matrix_Rows.webp)

Cols:

![Matrix Rows](./img/Matrix_Cols.webp)

The right side is identical but mirrored.

Try the following until problem solved:

1. Double check that you have soldered the Pico into the correct holes.
2. Ensure the soldering connections of the Pico to the PCB is good (if you used a header to solder the Pico onto the PCB one of the connections to the through-hole is likely bad). Re-solder as needed.
3. If none of the connections are obviously bad, use the image above to see what row/column corresponds to what connection (GP numbering on back of PCB). Re-solder that specific connection for good measure and test.
4. If re-soldering the connection didn't work, your Pico or PCB is likely damaged. Rule out the Pico by directly shorting the that row or column's corresponding pad on the Pico with another column/row pad (connecting one row and one column). If a key press is registered, there is a problem with your PCB, see the bottom of the next section about potentially fixing paths on the PCB. If no keypress is registered, the Pico is damaged and have fun de-soldering your Pico (hot-air station or careful work with a heat gun is the best way).

### Random key or keys not working

Note that the bottom row of keys is staggered by 2, so the the corresponding matrix column is shifted. See the photo in the above section.

If it's not a row or column of keys, than there is a bad connection between your switch and PCB.

Try the following until problem solved:

1. Re-seat the switch in the hot-swap socket.
2. Try a different switch.
3. Check the soldering of the hot-swap socket to the PCB, re-solder as needed
4. Short the PCB pads on either side of the hot-swap socket, if that registers a keypress, the hot-swap socket is bad and needs to replaced.
5. Check the diode.
   1. Check the soldering of the diode to the PCB and re-solder as needed.
   2. Double check that the diode is oriented correctly.
   3. Make sure diode actually works and has a good connection.
      1. Read the diode with a multimeter, typically reads a little more than 0.6. Higher numbers usually means the solder connection is bad, de-solder and re-solder the diode. If not reading, diode is bad and needs to be replaced.
      2. No multimeter? Short either side of the diode and press the key. If that works either the diode's connection is bad and re-solder, or the diode is dead and needs to be replaced.
6. If none of the above worked, the problem is most likely with the paths inside the PCB.
   1. You can try the following: (credit to [crkbd](https://github.com/foostan/crkbd) guide)
      1. "Visually inspect the PCB. If it looks scratched or damaged anywhere along the path from ProMicro to diode to keyswitch, the path might be interrupted. If you find a spot that looks damaged, you can use some wire to bypass the section that is damaged (e.g. connecting the ProMicro directly to the first pad of the diode). If this fixes the key, then you can either opt to keep the wire permanently, or you can try to repair the path. The path can be repaired by carefully scraping off the paint from a section of the path that is okay on either side of the damaged part (use a small flat head screwdriver intended for electronics). Then clean carefully with alcohol and solder a new connection. Youtube might have some guides on how to do this."
