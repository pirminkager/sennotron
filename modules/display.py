# -*- coding: utf-8 -*-
import time
import Adafruit_CharLCD as LCD
import types
import datetime

# Pin configuration
lcd_rs        = 25
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 27

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# lcd_columns = 20
# lcd_rows    = 4

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
			   lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

# Patch Adafruit_Char_LCD to add special character support
def _message_new(self, text):
  text = text.decode('utf-8','ignore')         #decode to utf-8
  line = 0
  for char in text:
    if ord(char) == 228 or ord(char) == 196:   #ä
      self.write8(0b11100001, True)
    elif ord(char) == 246 or ord(char) == 214: #ö
      self.write8(0b11101111, True)
    elif ord(char) == 252 or ord(char) == 220: #ü
      self.write8(0b11110101, True)
    elif ord(char) == 176:                     #°
      self.write8(0b11011111, True)
    elif ord(char) == 181:                     #µ
      self.write8(0b11100100, True)
    elif char == '\n':                         #newline (not used)
      line += 1
      col = 0 if self.displaymode & LCD_ENTRYLEFT > 0 else self._cols-1
      self.set_cursor(col, line)
    else:                                      #normal routine
      self.write8(ord(char), True)
lcd.message = types.MethodType(_message_new, lcd)
# end patch

# Routines to fill display with our desired information
# Display is divided into tree section
#
#   ##################
#   #Vorwärmen       # <-- The Active State
#   #12.3°C  01:20:32# <-- Temp; Remaining Time
#   ##################
#

def writestep(input):
  lcd.set_cursor(0,0)
  lcd.message(str('{:'+str(lcd_columns+1)+'}').format(input))

def writetemp(input):
  lcd.set_cursor(0,1)
  lcd.message(str('{:04.1f}').format(input)+'°C ')

def writetime(input):
  lcd.set_cursor(8,1)
  #lcd.message(str(datetime.timedelta(seconds=int(input)))+'   ') #not so nice
  lcd.message(time.strftime("%H:%M:%S", time.gmtime(int(input)))) #better formatting
