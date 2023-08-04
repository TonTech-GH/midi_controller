from src.midi_input import Midi, MidiDevice, MidiEvent
from src.hot_key import MediaKey, Hotkey


class KeyConf:
    def __init__(self, key_id, note, velocity, key_func, func_param) -> None:
        self.key_id = key_id
        self.note = note
        self.velocity = velocity
        self.key_func = key_func
        self.func_param = func_param    

    def is_equal(self, event: MidiEvent):
        if self.key_id != event.key_id:
            return False
        if self.note != event.note:
            return False
        if self.velocity != event.velocity:
            return False
        return True


class DdjFlx4:
    CONF = [
        # ---------- Media Key -----------
        # right play/pause -> play/pause
        KeyConf(key_id=145, note=11, velocity=127, key_func=MediaKey.press_key, func_param=MediaKey.PLAY),

        # right hotkey [1, 0] -> previous
        KeyConf(key_id=153, note= 4, velocity=127, key_func=MediaKey.press_key, func_param=MediaKey.PREVIOUS),

        # right hotkey [1, 1] -> next
        KeyConf(key_id=153, note= 5, velocity=127, key_func=MediaKey.press_key, func_param=MediaKey.NEXT),

        # ---------- Youtube Hot Key -----------
        # right hotkey [0, 2] -> YouTube 10秒戻し
        KeyConf(key_id=153, note= 2, velocity=127, key_func=Hotkey.press_key, func_param=Hotkey.YT_BACK),

        # right hotkey [0, 3] -> YouTube 10秒進む
        KeyConf(key_id=153, note= 3, velocity=127, key_func=Hotkey.press_key, func_param=Hotkey.YT_FORWARD),

        # right hotkey [1, 2] -> YouTube 再生速度アップ
        KeyConf(key_id=153, note= 6, velocity=127, key_func=Hotkey.press_key, func_param=Hotkey.YT_SPEED_DOWN),

        # right hotkey [1, 3] -> YouTube 再生速度ダウン
        KeyConf(key_id=153, note= 7, velocity=127, key_func=Hotkey.press_key, func_param=Hotkey.YT_SPEED_UP),

        # ---------- Youtube Music Hot Key -----------
        # right hotkey [0, 0] -> YouTubeMusic 10秒戻し
        KeyConf(key_id=153, note= 0, velocity=127, key_func=Hotkey.press_key, func_param=Hotkey.YTM_BACK),

        # right hotkey [0, 1] -> YouTubeMusic 10秒戻し
        KeyConf(key_id=153, note= 1, velocity=127, key_func=Hotkey.press_key, func_param=Hotkey.YTM_FORWARD),

        # ---------- Other -----------
        # FX ON/OFF -> 終了
        KeyConf(key_id=148, note=71, velocity=127, key_func=None, func_param=None),
    ]

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
        is_finished = False
        while True:
            if is_finished:
                break

            events = self.device.polling()
            for e in events:
                for conf in self.CONF:
                    if not conf.is_equal(e):
                        continue

                    if conf.key_func is None:
                        is_finished = True
                        break
                    else:
                        conf.key_func(conf.func_param)

if __name__ == '__main__':
    ddj = DdjFlx4()
    ddj.polling()
