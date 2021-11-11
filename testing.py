import unittest, mido

import midi_file_generator

#print(midi_file_generator.generate_A440())

class MIDIFileTest(unittest.TestCase):

    def test_parse_note_string(self):
        self.assertEqual(midi_file_generator.parse_note_string("Cn4"), ('C', 'n', 4))
        self.assertEqual(midi_file_generator.parse_note_string("Bb-1"), ('B', 'b', -1))
        self.assertEqual(midi_file_generator.parse_note_string("D#9"), ('D', '#', 9))
        self.assertEqual(midi_file_generator.parse_note_string("C#4"), ('C', '#', 4))

if __name__ == '__main__':
    unittest.main()