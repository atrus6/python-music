from midiutil.MidiFile import MIDIFile
import sys
import random
from walker import Walkerrandom

asdf = dict()
file = open('cleaned-C.csv', 'r')

for line in file:
    sp = line.split()
    asdf[' '.join(sp[:-1])] = int(sp[-1])

wrand = Walkerrandom(asdf.values(), asdf.keys())

my = MIDIFile(1)

track = 0
time = 501

my.addTrackName(track, time, sys.argv[1])
my.addTempo(track, time, 120)

track = 0
channel = 0
time = 0
duration = 1

notes = [[1], [0.5, 0.5], [0.25, 0.5, 0.25], [0.25, 0.25, 0.5], [0.5, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25]]

chords = ['single', 'triplet', 'seventh']

bars = []
for i in range(500):
    bars.append(random.choice(notes))

song = [item for sublist in bars for item in sublist]

for note in song:
    which_chord = random.random()
    which_note = int(wrand.random())+60

    volume = 100

    if time % 1 != 0:
        volume = 90

    if which_chord <= 0.666:
        my.addNote(track, channel, which_note, time, 1*note, volume)
    elif which_chord <= 0.91:
        my.addNote(track, channel, which_note - 1, time, 1*note, volume)
        my.addNote(track, channel, which_note + 1, time, 1*note, volume)
        my.addNote(track, channel, which_note + 3, time, 1*note, volume)
    else:
        my.addNote(track, channel, which_note - 1, time, 1*note, volume)
        my.addNote(track, channel, which_note + 1, time, 1*note, volume)
        my.addNote(track, channel, which_note + 3, time, 1*note, volume)
        my.addNote(track, channel, which_note + 5, time, 1*note, volume)

    time = time + note

b = open(sys.argv[1]+'.mid', 'wb')
my.writeFile(b)
b.close()
