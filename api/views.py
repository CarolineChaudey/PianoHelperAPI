from django.http import HttpResponse
import midi


def get_all(request) :
    return HttpResponse("1) Keyboard cat\n2) GOT\n3) Requiem for a Dream\n4) Zelda")


def get(request, music_id) :
    if music_id == "1":
        pattern = midi.read_midifile("api/sheets/keyboard_cat.mid")
        result = format_pattern(pattern)
        return HttpResponse(result)
    elif music_id == "2":
        pattern = midi.read_midifile("api/sheets/GameofThrones.mid")
        result = format_pattern(pattern)
        return HttpResponse(result)
    elif music_id == "3":
        pattern = midi.read_midifile("api/sheets/rfd.mid")
        result = format_pattern(pattern)
        return HttpResponse(result)
    elif music_id == "4":
        pattern = midi.read_midifile("api/sheets/ThemeA.mid")
        result = format_pattern(pattern)
        return HttpResponse(result)
    else:
        return HttpResponse("No such song")


def get_midi_pattern(path):
    pattern = midi.read_midifile(path)
    return HttpResponse(pattern)


def format_pattern(pattern):
    result = []
    for track in pattern:
        desc_track = []
        for event in track:
            event_type = event.__class__.__name__
            if event_type == "NoteOffEvent" or event_type == "NoteOnEvent":
                desc_track.append(event)
        result.append(desc_track)
    return result
