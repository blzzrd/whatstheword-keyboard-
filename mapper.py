from dataclasses import dataclass
from typing import ClassVar, Dict



@dataclass(frozen=True)
class Layouts():
    def __init__(self, alphabetic: bool):
        if alphabetic:
            self.alphabetic = True

    QWERTY_LAYOUT: str = "qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
    COLEMAK_LAYOUT: str = "wqfpgjluy;[]\\arstdhneio'zxcvbkm,./"
    DVORAK_LAYOUT: str = "',.pyfgcrl/=\\aoeuidhtns-;qjkxbmwvz"

    Q2C: ClassVar[Dict[str, str]] = create_mapping(QWERTY_LAYOUT, COLEMAK_LAYOUT)
    C2D: ClassVar[Dict[str, str]] = create_mapping(COLEMAK_LAYOUT, DVORAK_LAYOUT)
    Q2D: ClassVar[Dict[str, str]] = create_mapping(QWERTY_LAYOUT, DVORAK_LAYOUT)

    def create_mapping(self, layout1: str, layout2: str) -> dict[str, str]:
        """
        Usage:
        create_mapping(QWERTY_LAYOUT, COLEMAK_LAYOUT)
        create_mapping(COLEMAK_LAYOUT, DVORAK_LAYOUT)
        create_mapping(QWERTY_LAYOUT, DVORAK_LAYOUT)
        """
        mapping = dict(zip(layout1, layout2))

        if (len(layout1) != len(layout2)):
            print("Unequal lengths in layouts.")
            return {}
        
        # strip away any non-letter characters for simplicity
        if self.alphabetic:
            for val in list(mapping):
                if(not val.isalpha() or not mapping[val].isalpha()):
                    del mapping[val]
        return mapping