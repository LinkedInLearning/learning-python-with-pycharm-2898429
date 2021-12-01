from melodia.core.track import Track
from melodia.music import chord
from melodia.io import midi


def generate_audio(audio_folder='./sound_effects'):
    track = Track(signature=(4, 4))

    track.add(chord.maj('C3', (1, 4)))
    track.add(chord.maj('D3', (1, 4)))
    track.add(chord.min('A3', (1, 4)))
    track.add(chord.maj7('G3', (1, 2)))

    with open(f'{audio_folder}/intro.mid', 'wb') as f:
        midi.dump(track, f)

    track = Track(signature=(1, 4))
    track.add(chord.maj('C2', (1, 8)))
    track.add(chord.maj('F2', (1, 8)))
    track.add(chord.maj('F#2', (1, 4)))

    with open(f'{audio_folder}/reset.mid', 'wb') as f:
        midi.dump(track, f)
