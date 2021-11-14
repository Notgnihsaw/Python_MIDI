# this script will generate basic MIDI files. 
import mido
from mido import Message, MidiFile, MidiTrack

NOTES = ("A", "B", "C", "D", "E", "F", "G")
ACCIDENTALS = ("n", "#", "b")

#converts a note in the form of note, accidental, octave
# into its corresponding MIDI number. 
# For example, C#5 -> 73; C-1 = 
def note_to_MIDI_number(note, accidental, octave):
    midi_number = 0

    note = note.upper()

    if octave >= -1 and octave <= 9:
        # Parses note name
        if note == "C":
            midi_number = 0
        elif note == "D":
            midi_number = 2
        elif note == "E":
            midi_number = 4
        elif note == "F":
            midi_number = 5
        elif note == "G":
            midi_number = 7
        elif note == "A":
            midi_number = 9
        elif note == "B":
            midi_number = 11
        else:
            return -1

        # parses accidental
        if accidental == "#":
            midi_number += 1
        elif accidental == "b":
            midi_number -= 1
        elif accidental == "n":
            midi_number += 0
        else: 
            return -1

        # scales by octave
        midi_number += ((octave + 1)* 12)

        if (midi_number <= 127) and (midi_number >= 0):
            return midi_number
        else:
            return -1
    else:
        return -1

# Converts a note string to a MIDI number.
def string_note_to_MIDI_number(note):
    note_name, accidental, octave = parse_note_string(note)

    return note_to_MIDI_number(note_name, accidental, octave)


# separates a note in the form of A4 or Bb3 into 
# its components of note degree, accidental, and octave.
# It is assumed that this is well-formed into "XYZ": 
# where X is a note name from A-G; Y is one of "n", "#", "b"; and Z is a signal digit number (which can be negative)
def parse_note_string(note):
    note_name = note[0]
    accidental = note[1]

    octave = 0

    if note.endswith("-1"):
        octave = -1
    else: 
        octave = int(note[-1])
    
    return note_name, accidental, octave

def generate_note_messages(note_number, start_time, duration):
    note_on_msg = Message('note_on', note=note_number, time=start_time)
    note_off_msg = Message('note_off', note=note_number, time=start_time + duration)
    return note_on_msg, note_off_msg

def generate_A440():
    msg = mido.Message('note_on', note=69, time=0)
    return msg

# generates a major scale
def generate_major_scale(root_note, duration):
    major_semitones = (2, 2, 1, 2, 2, 2, 1)
    return generate_scale(major_semitones, root_note, duration)

# generates a major pentatonic scale
def generate_maj_pentatonic_scale(root_note, duration):
    semitones = (2, 2, 3, 2, 3)
    return generate_scale(semitones, root_note, duration)

# generates an arbitrary scale based on a sequence of semitones. 
# the root note is the MIDI number of the root note of the scale.
# The sequence is all the same length, with no space in between notes and no overlapping notes.
def generate_scale(semitone_sequence, root_note, duration):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    time = 0

    #iterates through the semitone sequence and adds the note to the MIDI sequence.
    for semitones in semitone_sequence:
        # using extend because generate_note_messages returns two outputs.
        # semitones represents the semitones from the root note to go up
        track.extend(generate_note_messages(root_note + semitones, time + duration, duration))
        time += duration
    
    return mid