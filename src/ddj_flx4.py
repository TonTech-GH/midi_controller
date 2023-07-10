import time

from src.midi_input import Midi, MidiDevice, MidiEvent
from src.hot_key import HIDPostAuxKey, NX_KEYTYPE_PLAY, NX_KEYTYPE_NEXT, NX_KEYTYPE_PREVIOUS


class DdjFlx4:
    def __init__(self) -> None:
        self.device = self.get_input_device()
    
    def get_input_device(self) -> MidiDevice:
        for device in Midi.get_devices():
            if not device.is_input:
                continue
            if device.name == b'DDJ-FLX4':
                return device
        return None

    def polling(self):
        finished = False
        while True:
            if finished:
                break

            events = self.device.polling()
            for e in events:
                if e.key_id == 145 and e.note == 11 and e.velocity == 127:
                    # right play/pause
                    HIDPostAuxKey(NX_KEYTYPE_PLAY)

                if e.key_id == 153 and e.note == 4 and e.velocity == 127:
                    # right hotkey [1, 0]
                    HIDPostAuxKey(NX_KEYTYPE_PREVIOUS)

                if e.key_id == 153 and e.note == 5 and e.velocity == 127:
                    # right hotkey [1, 1]
                    HIDPostAuxKey(NX_KEYTYPE_NEXT)

                if e.key_id == 148 and e.note == 71 and e.velocity == 127:
                    # FX ON/OFF
                    finished = True

if __name__ == '__main__':
    ddj = DdjFlx4()
    ddj.polling()
