import mido, numpy

import midi_file_generator


# Map MIDI_number to specific frequencies, using Equal Temperament.
def midi_number_to_freq(midi_number):