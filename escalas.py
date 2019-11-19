"""
Created on 8 de mar de 2016

@author: Frederico
"""

# from audio import sine_tone


class Escala(list):
    NOTAS = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    ESCALAS = {
        'major': [0, 2, 4, 5, 7, 9, 11],
        'minor': [0, 2, 3, 5, 7, 8, 10],
        'harmonic': [0, 2, 3, 5, 7, 8, 11],
        'melodic': [0, 2, 3, 5, 7, 9, 11],
        'pentatonic': [0, 3, 5, 7, 10],
        'diminished': [0, 3, 6, 9],
        'cromatic': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        'pentatonic_blues': [0, 3, 5, 6, 7, 10],
        'fibonacci': [0, 1, 1, 2, 3, 5, 8],
        'ionian': [0, 2, 4, 5, 7, 9, 11],
        'dorian': [0, 2, 3, 5, 7, 9, 10],
        'phrygian': [0, 1, 3, 5, 7, 8, 10],
        'lydian': [0, 2, 4, 6, 7, 9, 11],
        'mixolydian': [0, 2, 4, 5, 7, 9, 10],
        'aeolian': [0, 2, 3, 5, 7, 8, 10],
        'locrian': [0, 1, 3, 5, 6, 8, 10],
    }

    FREQS = {'A': 440.0,
             'A#': 466.16,
             'B': 493.88,
             'C': 523.25,
             'C#': 554.37,
             'D': 587.33,
             'D#': 622.25,
             'E': 659.25,
             'F': 698.46,
             'F#': 739.99,
             'G': 783.99,
             'G#': 830.61}

    INSTRUMENTS = {
        'guitar': ['E', 'A', 'D', 'G', 'B', 'E'],
        'bass': ['E', 'A', 'D', 'G'],
        'ukulele': ['G', 'C', 'E', 'A'],
        'cavaquinho': ['D', 'G', 'B', 'D'],
    }

    def __init__(self, tonica, tipo_escala, *args):
        list.__init__(self, *args)
        self.tonica = tonica.upper()
        self.tipo_escala = tipo_escala.lower()
        self._make_escala()
        
    def __repr__(self, *args, **kwargs):
        return str(self.tonica) + " " + str(self.tipo_escala) + ": " + ", ".join(self)
        
    def _make_escala(self):
        index_tonica = self.NOTAS.index(self.tonica)
        del self[:]
        for dist_tonica in self.ESCALAS[self.tipo_escala]:
            self.append(self.NOTAS[(index_tonica+dist_tonica)%len(self.NOTAS)])
    
    def print_escala(self, instrument='guitar'):
        print('\n{} {} on a {}:'.format(self.tonica, self.tipo_escala, instrument))
        print('  0  1   2   3   4   5   6   7   8   9   10  11  12')
        string_order = Escala.INSTRUMENTS[instrument]
        string_order.reverse()
        for note in string_order:
            self.print_string(Escala(note, 'cromatic'))
    
    def print_string(self, string):
        string.append(string[0])
        printed_string = string.tonica
        if string[0] in self:
            if string[0] == self[0]:
                printed_string += " O|"
            else:
                printed_string += " X|"
        else:
            printed_string += "  |"
        for nota in string[1:]:
            if nota in self:
                if nota == self[0]:
                    printed_string += '-O-|'
                else:
                    printed_string += '-X-|'
            else:
                printed_string += '---|'
        print(printed_string)
        
    # def play(self, length=1, oitavas=1):
    #     todas_freqs = []
    #     for i in range(oitavas):
    #         for note in self:
    #             freq = self.FREQS[note]
    #             if freq < Escala.FREQS[self[0]]:
    #                 freq *= 2
    #             todas_freqs.append(freq*(2**i))
    #     for note in todas_freqs:
    #         sine_tone(note, length)


if __name__ == '__main__':
    escala = Escala('C', 'major')
    print(escala)
    escala.print_escala()
    escala.print_escala('ukulele')
    escala.print_escala('bass')
    # escala.play(0.05)

    # sine_tone(440, 2)
    # sine_tone(432, 2)
    # sine_tone(420, 2)
