from django.http import HttpResponse
import midi


def get_all(request) :
    return HttpResponse("1) Skyrim\n2) GOT\n3) Requiem for a Dream\n4) Zelda")


def get(request, music_id) :
    if music_id == "1":
        return get_midi_pattern("api/sheets/Dragonborn-Skyrim.mid")
    elif music_id == "2":
        pattern = midi.read_midifile("api/sheets/GameofThrones.mid")
        nbTracks = len(pattern.tracks)
        return get_midi_pattern("Nb tracks = ", nbTracks)
    elif music_id == "3":
        return get_midi_pattern("api/sheets/rfd.mid")
    elif music_id == "4":
        return get_midi_pattern("api/sheets/ThemeA.mid")
    else:
        return HttpResponse("No such song")


def get_midi_pattern(path):
    pattern = midi.read_midifile(path)
    return HttpResponse(pattern)
