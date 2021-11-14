import unittest, mido

import midi_file_generator, midi_player

#print(midi_file_generator.generate_A440())

class MIDIFileTest(unittest.TestCase):

    def test_parse_note_string(self):
        self.assertEqual(midi_file_generator.parse_note_string("Cn4"), ('C', 'n', 4))
        self.assertEqual(midi_file_generator.parse_note_string("Bb-1"), ('B', 'b', -1))
        self.assertEqual(midi_file_generator.parse_note_string("D#9"), ('D', '#', 9))
        self.assertEqual(midi_file_generator.parse_note_string("C#4"), ('C', '#', 4))
    
    def test_note_to_MIDI_number(self):
        self.assertEqual(midi_file_generator.note_to_MIDI_number('C', 'n', -1), 0)
        self.assertEqual(midi_file_generator.note_to_MIDI_number('C', 'n', -2), -1)
        self.assertEqual(midi_file_generator.note_to_MIDI_number('C', 'n', 9), 120)
        self.assertEqual(midi_file_generator.note_to_MIDI_number('C', '#', -1), 1)
        self.assertEqual(midi_file_generator.note_to_MIDI_number('B', 'b', -1), 10)
        self.assertEqual(midi_file_generator.note_to_MIDI_number('B', 'n', -1), 11)
        self.assertEqual(midi_file_generator.note_to_MIDI_number('C', 'n', 4), 60)
        self.assertEqual(midi_file_generator.note_to_MIDI_number('A', 'n', 4), 69)
    
    def test_generate_A440(self):
        msg = mido.Message('note_on', note=69, time=0)
        self.assertEqual(msg, midi_file_generator.generate_A440())
    
    def test_generate_note_messages(self):
        results = midi_file_generator.generate_note_messages(60, 0, 1)
        #generating a C4 for 1 second. 
        self.assertEqual(results[0], mido.Message('note_on', note=60, time=1))
        self.assertEqual(results[1], mido.Message('note_off', note=60, time=1))

class MIDIPlayerTest(unittest.TestCase):

    @unittest.skip('already tested')
    def test_play_sample_MIDI(self):
        mid = mido.MidiFile('Python_MIDI/MIDI_output_files/MIDI_test_sample.mid')

        midi_player.play_music('Python_MIDI/MIDI_output_files/MIDI_test_sample.mid')
    
    #@unittest.skip
    def test_play_C4(self):
        c4_midi_messages = midi_file_generator.generate_note_messages(60, 0, 512)
        #print(c4_midi_messages[0])
        #print(c4_midi_messages[1])

        c4_midi_track = midi_file_generator.messages_to_MIDI_file([c4_midi_messages[0], c4_midi_messages[1]])
        #print(c4_midi_track)

        midi_player.play_mido_MIDI(c4_midi_track)
        


if __name__ == '__main__':
    unittest.main()