'''
Created on 16 de mar de 2016

@author: fvj
'''

CONST = 2.**(1./12.)
NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#' ]

freq = 27.5
i = 0
todas_freqs = []

while(freq<20000):
    print(str(NOTES[i%12]) + " " + str(freq))
    todas_freqs.append(freq)
    i += 1
    freq *= CONST

freq = 27.5
freq /= CONST
i = -1
while(freq>20):
    print(str(NOTES[i%12]) + " " + str(freq))
    todas_freqs.append(freq)
    i -= 1
    freq /= CONST
    

print(len(todas_freqs))
print(todas_freqs)