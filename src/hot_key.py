import pyautogui
import Quartz


class MediaKey:
    # NSEvent.h
    _NSSystemDefined = 14

    # hidsystem/ev_keymap.h
    SOUND_UP = 0
    SOUND_DOWN = 1
    MUTE = 7
    PLAY = 16
    NEXT = 17
    PREVIOUS = 18
    FAST = 19
    REWIND = 20

    @classmethod
    def _HIDPostAuxKey(cls, key):
        def doKey(down):
            ev = Quartz.NSEvent.otherEventWithType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_(
                cls._NSSystemDefined, # type
                (0,0), # location
                0xa00 if down else 0xb00, # flags
                0, # timestamp
                0, # window
                0, # ctx
                8, # subtype
                (key << 16) | ((0xa if down else 0xb) << 8), # data1
                -1 # data2
                )
            cev = ev.CGEvent()
            Quartz.CGEventPost(0, cev)
        doKey(True)
        doKey(False)
    
    @classmethod
    def press_key(cls, key):
        cls._HIDPostAuxKey(key)


class Hotkey:
    YT_FORWARD = 'right'
    YT_BACK = 'left'
    YT_SPEED_UP = '>'
    YT_SPEED_DOWN = '<'

    YTM_BACK = 'h'
    YTM_FORWARD = 'l'

    @classmethod
    def press_key(cls, key):
        pyautogui.press(key)


if __name__ == '__main__':
    # HIDPostAuxKey(NX_KEYTYPE_SOUND_DOWN)
    # HIDPostAuxKey(NX_KEYTYPE_NEXT)
    # HIDPostAuxKey(NX_KEYTYPE_PREVIOUS)
    # HIDPostAuxKey(NX_KEYTYPE_MUTE)
    MediaKey.press_key(MediaKey.PLAY)