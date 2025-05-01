
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
    Safely decodes characters encoded in the PUA range (U+E0000 and above).
    Skips any character outside this expected encoding.
    """
    decoded_chars = []
    for ch in pua_text:
        code = ord(ch)
        if 0xE0000 <= code <= 0x10FFFF:
            decoded_chars.append(chr(code - 0xE0000))
        else:
            # Optionally, log or handle unexpected characters
            return
    return ''.join(decoded_chars)
