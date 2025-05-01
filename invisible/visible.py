# 🔒 Invisible Text Scanner for LLM Input Protection

import unicodedata

# --- Step 1: Define scanner functions ---
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def remove_invisible_characters(text):
    """
    Removes invisible or non-printable Unicode characters.
    Categories: Cc (Control), Cf (Format), Co (Private Use), Cn (Unassigned)
    """
    return ''.join(
        ch for ch in text
        if unicodedata.category(ch) not in ('Cc', 'Cf', 'Co', 'Cn')
    )

def has_invisible_characters(text):
    """
    Returns True if any invisible characters are found.
    """
    return any(unicodedata.category(ch) in ('Cc', 'Cf', 'Co', 'Cn') for ch in text)

def find_invisible_characters(text):
    """
    Returns a list of tuples: (index, character, unicode name, unicode category)
    """
    invisible = []
    for idx, ch in enumerate(text):
        cat = unicodedata.category(ch)
        if cat in ('Cc', 'Cf', 'Co', 'Cn'):
            name = unicodedata.name(ch, "Unnamed or Unassigned")
            invisible.append((idx, repr(ch), name, cat))
    return invisible
def decode_from_tag_chars(pua_text):
    """
    Decodes a string that was encoded using Private Use Area steganography (PUA offset).
    Assumes characters were encoded as: chr(0xE0000 + ord(ch))
    """
    decoded = ''.join(chr(ord(ch) - 0xE0000) for ch in pua_text)
    return decoded
