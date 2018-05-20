EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:switches
LIBS:relays
LIBS:motors
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Raspberry_Pi_2_3 J?
U 1 1 5B01EDCB
P 2400 2450
F 0 "J?" H 3100 1200 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 2000 3350 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_2x20" H 3400 3700 50  0001 C CNN
F 3 "" H 2450 2300 50  0001 C CNN
	1    2400 2450
	1    0    0    -1  
$EndComp
$Comp
L MCP3208 U?
U 1 1 5B01EE18
P 6000 1750
F 0 "U?" H 5800 2275 50  0000 R CNN
F 1 "MCP3208" H 5800 2200 50  0000 R CNN
F 2 "" H 6100 1850 50  0001 C CNN
F 3 "" H 6100 1850 50  0001 C CNN
	1    6000 1750
	1    0    0    -1  
$EndComp
$Comp
L Conn_02x08_Odd_Even J?
U 1 1 5B01EEC3
P 5700 3200
F 0 "J?" H 5750 3600 50  0000 C CNN
F 1 "Conn_02x08_Odd_Even" H 5750 2700 50  0000 C CNN
F 2 "" H 5700 3200 50  0001 C CNN
F 3 "" H 5700 3200 50  0001 C CNN
	1    5700 3200
	1    0    0    -1  
$EndComp
$Comp
L Conn_01x16_Female J?
U 1 1 5B01EF22
P 8300 2200
F 0 "J?" H 8300 3000 50  0000 C CNN
F 1 "Conn_01x16_Female" H 8300 1300 50  0000 C CNN
F 2 "" H 8300 2200 50  0001 C CNN
F 3 "" H 8300 2200 50  0001 C CNN
	1    8300 2200
	1    0    0    -1  
$EndComp
$Comp
L S102S01 U?
U 1 1 5B01EFE1
P 9800 4950
F 0 "U?" H 9600 5150 50  0000 L CNN
F 1 "S102S01" H 9800 5150 50  0000 L CNN
F 2 "Housings_SIP:SIP4_Sharp-SSR_Pitch7.62mm_Straight" H 9600 4750 50  0001 L CIN
F 3 "" H 9765 4950 50  0001 L CNN
	1    9800 4950
	1    0    0    -1  
$EndComp
$Comp
L 4N28 U?
U 1 1 5B01F062
P 9900 1800
F 0 "U?" H 9700 2000 50  0000 L CNN
F 1 "4N28" H 9900 2000 50  0000 L CNN
F 2 "Housings_DIP:DIP-6_W7.62mm" H 9700 1600 50  0001 L CIN
F 3 "" H 9900 1800 50  0001 L CNN
	1    9900 1800
	1    0    0    -1  
$EndComp
$Comp
L 4N28 U?
U 1 1 5B01F0DD
P 9900 2250
F 0 "U?" H 9700 2450 50  0000 L CNN
F 1 "4N28" H 9900 2450 50  0000 L CNN
F 2 "Housings_DIP:DIP-6_W7.62mm" H 9700 2050 50  0001 L CIN
F 3 "" H 9900 2250 50  0001 L CNN
	1    9900 2250
	1    0    0    -1  
$EndComp
$EndSCHEMATC
