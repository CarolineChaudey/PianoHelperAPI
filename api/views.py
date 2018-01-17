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
                #desc_track.append(['off', event.tick, event.data[0]])
                print("");
            elif event_type == "NoteOnEvent":
                if event.data[1] == 0:
                    print("");
                    #desc_track.append(['off', event.tick, event.data[0]])
                else:
                    desc_track.append(['on', event.tick, convert_note(event.data[0])])
        result.append(desc_track)
    return result


def convert_note(note_code):
    if note_code in (24, 36, 48, 60, 72, 84, 96):
        return 1
    elif note_code in (26, 38, 50, 62, 74, 86, 98):
        return 2
    elif note_code in (28, 40, 52, 64, 76, 88, 100):
        return 3
    elif note_code in (29, 41, 53, 65, 77, 89, 101):
        return 4
    elif note_code in (31, 43, 55, 67, 79, 91, 103):
        return 5
    elif note_code in (33, 45, 57, 69, 81, 93, 105):
        return 6
    elif note_code in (35, 47, 59, 71, 83, 95, 107):
        return 7
    elif note_code in (25, 37, 49, 61, 73, 85, 97):
        return 1.5
    elif note_code in (27, 39, 51, 63, 75, 87, 99):
        return 2.5
    elif note_code in (30, 42, 54, 66, 78, 90, 102):
        return 4.5
    elif note_code in (32, 44, 56, 68, 80, 92, 104):
        return 5.5
    elif note_code in (34, 46, 58, 70, 82, 94, 106):
        return 6.5
    else:
        return "wtf"
