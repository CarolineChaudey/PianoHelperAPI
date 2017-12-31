from django.http import HttpResponse
import midi, json


patterns = ['keyboard_cat.mid', 'GameofThrones.mid', 'rfd.mid', 'ThemeA.mid'];
pattern_path = 'api/sheets/'


def get_all(request) :
    return HttpResponse(patterns)


def get(request, music_id) :
    try:
        pattern = get_midi_pattern(patterns[int(music_id)])
    except IndexError:
        return HttpResponse("No such song")
    formatted = format_pattern(pattern)
    result = json.dumps(formatted)
    return HttpResponse(result)


def get_midi_pattern(pattern_name):
    path = pattern_path + pattern_name
    pattern = midi.read_midifile(path)
    return pattern


def format_pattern(pattern):
    result = []
    for track in pattern:
        desc_track = []
        for event in track:
            event_type = event.__class__.__name__
            if event_type == "NoteOffEvent":
                desc_track.append(['off', event.tick, event.data[0]])
            elif event_type == "NoteOnEvent":
                desc_track.append(['on', event.tick, event.data[0]])
        result.append(desc_track)
    return result
