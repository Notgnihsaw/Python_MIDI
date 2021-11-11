# This script will accept a Mido MIDI object and play it using pygame.
import mido, hashlib, pygame, sys

from pygame.locals import *

import midi_file_generator

# save MIDI file:
# mid.save('new_song.mid')

def play_mido_MIDI(sequence):
    # we generate a unique hash for the file name
    midi_hash = hash(sequence)

    # saves the sequence so it can be read by pygame later.
    sequence.save('Python_MIDI/MIDI_output_files/' + str(midi_hash) + '.mid')

    # mixer config
    freq = 44100  # audio CD quality
    bitsize = -16   # unsigned 16 bit
    channels = 2  # 1 is mono, 2 is stereo
    buffer = 1024   # number of samples
    pygame.mixer.init(freq, bitsize, channels, buffer)

    # set volume:
    pygame.mixer.music.set_volume(0.8)

    try:
        # use the midi file you just saved
        play_music('Python_MIDI/MIDI_output_files/' + str(midi_hash) + '.mid')
    except KeyboardInterrupt:
        # if user hits Ctrl/C then exit
        # (works only in console mode)
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()
        raise SystemExit

# use code from https://stackoverflow.com/questions/6030087/play-midi-files-in-python

def play_music(midi_filename):
  '''Stream music_file in a blocking manner'''
  clock = pygame.time.Clock()
  pygame.mixer.music.load(midi_filename)
  pygame.mixer.music.play()

  while pygame.mixer.music.get_busy():
    clock.tick(30) # check if playback has finished
