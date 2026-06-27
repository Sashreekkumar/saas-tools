import re
import html
from urllib.parse import unquote

def clean_url(url):
    # Repeatedly decode until nothing changes
    previous = None

    while url != previous:
        previous = url

        # URL decoding (%25 -> %, %3D -> =, etc.)
        url = unquote(url)

        # Fix escaped slashes
        url = url.replace(r"\/", "/")

        # Decode unicode escapes (\u003d -> =)
        try:
            url = url.encode().decode("unicode_escape")
        except:
            pass

        # Decode HTML entities if any
        url = html.unescape(url)

    return url


raw = input("Paste URL: ").strip()
print("\nCleaned URL:\n")
print(clean_url(raw))