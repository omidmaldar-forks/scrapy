"""
Transitional module for moving to the w3lib library.

For new code, always import from w3lib.http instead of this module
"""

from w3lib.http import *

def decode_chunked_transfer(chunked_body):
    """Parsed body received with chunked transfer encoding, and return the
    decoded body.

    For more info see:
    http://en.wikipedia.org/wiki/Chunked_transfer_encoding

    """
    body_parts, h, t = [], b'', chunked_body
    while t:
        h, t = t.split(b'\r\n', 1)
        if h == b'0':
            break
        size = int(h, 16)
        body_parts.append(t[:size])
        t = t[size+2:]
    return b''.join(body_parts)

