#!/usr/bin/env python3

import random
import time

from hue_api import HueApi

MIN_HUE = 0
MAX_HUE = 65535

MIN_SATURATION = 0
MAX_SATURATION = 255

HUES = {
  'red': 0,
  'orange': 2000,
  'yellow': 6000,
  'green': 25000,
  'blue': 42000,
  'violet': 48000,
}

RAINBOW_COLORS = [
  HUES['red'],
  HUES['orange'],
  HUES['yellow'],
  HUES['green'],
  HUES['blue'],
  HUES['violet'],
]

WINDOWS_BY_ID = [
  [11], # Window 1/R
  [10], # Window 2/O
  [9], # Window 3/Y (Gym)
  [13, 1, 2, 3, 4], # Window 4/G (Office)
  [12, 19], # Window 5/B
  [14, 17], # Window 6/I
  [16, 18], # Window 7/V
]


api = HueApi()

# Create new API key:
#api.create_new_user('bridge ip address')
#api.save_api_key('foo.key')

# Load existing API key:
api.load_existing('foo.key')

print('fetching lights...')
lights = api.fetch_lights()

i = 0
while True:
    for window_idx in range(len(WINDOWS_BY_ID)):
        color_idx = (window_idx + i) % len(RAINBOW_COLORS)

        for light in lights:
            if light.id not in WINDOWS_BY_ID[window_idx]:
                continue
            #hue = random.randint(MIN_HUE, MAX_HUE)
            #sat = random.randint(MIN_SATURATION, MAX_SATURATION)
            hue = RAINBOW_COLORS[color_idx]
            light.set_color(hue, MAX_SATURATION)

    i += 1
    time.sleep(1)

