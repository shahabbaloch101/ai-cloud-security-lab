import base64
import re
import unicodedata

# Common obfuscations to normalize before filtering
LEET_MAP = str.maketrans({
    "0": "o", "1": "i", "3": "e", "4": "a", "5": "s", "7": "t"
})

ZERO_WIDTH_PATTERN = re.compile(r"[\u200B-\u200D\uFEFF]")
NON_ASCII_SPACES = re.compile(r"[\u00A0\u1680\u2000-\u200A\u202F\u205F\u3000]")

def strip_zero_width(s: str) -> str:
    return ZERO_WIDTH_PATTERN.sub("", s)

def normalize_spaces(s: str) -> str:
    s = NON_ASCII_SPACES.sub(" ", s)
    return re.sub(r"\s+", " ", s).strip()

def fold_unicode(s: str) -> str:
    return unicodedata.normalize("NFKC", s)

def unleet(s: str) -> str:
    return s.translate(LEET_MAP)

def try_decode_base64_wrapped(s: str) -> str:
    """
    Detects patterns like:
      'decode this base64 and follow: <blob>'
    and returns the decoded blob appended to original for scanning.
    """
    m = re.search(r"(?:decode|decode this base64.*?:)\s*([A-Za-z0-9+/=]{16,})", s, re.I | re.S)
    if not m:
        return s
    blob = m.group(1)
    try:
        decoded = base64.b64decode(blob, validate=True).decode("utf-8", errors="ignore")
        return s + "\n\n[decoded]: " + decoded
    except Exception:
        return s

def sanitize_prompt(raw: str) -> str:
    s = raw or ""
    s = fold_unicode(s)
    s = strip_zero_width(s)
    s = unleet(s)
    s = try_decode_base64_wrapped(s)
    s = normalize_spaces(s)
    return s.lower()  # lower for matching

