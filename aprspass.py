# Define a function called aprspass that takes a callsign as input
def aprspass(callsign: str):
    """
    This function takes a callsign string as input and returns a hash value.
    The callsign is trimmed up to the position of '-' if it exists, and the first 10 characters are converted to uppercase.
    The hash value is calculated by XORing the ASCII values of the characters in the callsign two bytes at a time.
    The high bit of the hash value is masked off so that the number is always positive.
    """
    # Find the position of '-' in callsign
    stop_here = callsign.find('-')

    # If '-' is found, trim the callsign up to the position of '-'
    if stop_here != -1:
        callsign = callsign[:stop_here]

    # Convert the first 10 characters of callsign to uppercase
    real_call = callsign[:10].upper()

    # Initialize hash_value
    hash_value = 0x73e2

    # Hash real_call two bytes at a time
    for i in range(0, len(real_call), 2):
        hash_value ^= ord(real_call[i]) << 8
        if i+1 < len(real_call):
            hash_value ^= ord(real_call[i + 1])

    # Mask off the high bit so number is always positive
    return hash_value & 0x7fff
