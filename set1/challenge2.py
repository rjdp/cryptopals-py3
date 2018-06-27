import codecs


def xor_hex_strs(hex1, hex2):
    """
    >>> xor_hex_strs('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')
    '746865206b696420646f6e277420706c6179'
    """
    return "".join(
        [
            "{:x}".format(x ^ y)
            for x, y in zip(codecs.decode(hex1, "hex"), codecs.decode(hex2, "hex"))
        ]
    )
