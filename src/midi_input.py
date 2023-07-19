import time

import pygame
import pygame.midi

pygame.init()
pygame.midi.init()


class MidiEvent:
    def __init__(self, midi_event) -> None:
        ((key_id, note, velocity, channel), timestamp) = midi_event
        self.key_id = key_id
        self.note = note
        self.velocity = velocity
        self.channel = channel
        self.timestamp = timestamp

    def __str__(self) -> str:
        return f'key_id: {self.key_id}, note: {self.note}, velocity: {self.velocity}'

    def to_dict(self):
        ret = {
            'key_id': self.key_id,
            'note': self.note,
            'velocity': self.velocity,
            'channel': self.channel,
            'time_stamp': self.timestamp,
        }
        return ret


class MidiDevice:
    def __init__(self, id) -> None:
        self.id = id
        d = pygame.midi.get_device_info(id)
        self.interf = d[0]
        self.name = d[1]
        self.input = d[2]
        self.output = d[3]
        self.opened = d[4]
        self.midi_io = None

    def __str__(self) -> str:
        return f'{self.interf}, {self.name}, {self.is_input}, {self.is_output}, {self.is_opened}'
    
    @property
    def is_input(self):
        return self.input == 1
    
    @property
    def is_output(self):
        return self.output == 1

    @property
    def is_opened(self):
        return self.opened == 1

    def open_input(self):
        self.midi_io = pygame.midi.Input(self.id)

    def polling(self, sleep_sec=0.1) -> list[MidiEvent]:
        if self.midi_io is None:
            self.open_input()
        while True:
            if self.midi_io.poll():
                midi_events = self.midi_io.read(10)
                midi_events = [MidiEvent(e) for e in midi_events]
                return midi_events

            time.sleep(sleep_sec)

    # def __del__(self):
    #     if self.midi_io is not None:
    #         self.midi_io.close()


class Midi:
    @classmethod
    def get_info(cls) -> dict:
        return {
            'count': pygame.midi.get_count(),
            'default_input_id': pygame.midi.get_default_input_id(),
            'default_output_id': pygame.midi.get_default_output_id(),
        }

    @classmethod
    def get_devices(cls) -> list[MidiDevice]:
        devices = []
        for idx in range(pygame.midi.get_count()):
            device = MidiDevice(idx)
            devices.append(device)
        return devices


if __name__ == '__main__':
    info = Midi.get_info()
    for k, v in info.items():
        print(k, v)

    devices = Midi.get_devices()

    in_device = None
    for d in devices:
        if d.is_input:
            in_device = d

    if in_device is None:
        print('No input midi device.')
    else:
        midi_events = in_device.polling()
        for event in midi_events:
            print(event)

