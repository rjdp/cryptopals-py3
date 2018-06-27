import codecs

enc_hex_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
l = [''.join("{:x}".format(x ^ y ) for x in codecs.decode(enc_hex_str, "hex")) for y in range(256)]

possible_stmts = []

for a in l:
    try:
       possible_stmts.append(codecs.decode(a, 'hex').decode('utf-8'))
    except:
       pass

max(possible_stmts, key=lambda x: sum(x.count(char) for char in list("etaoin")))