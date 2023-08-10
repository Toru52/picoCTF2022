def convert(c):
  if 'a' <= c <= 'z': return convert(c.upper()).lower()
  table = 'ZGSOCXPQUYHMILERVTBWNAFJDK'
  if c in table: return chr(table.index(c) + 65)
  return c

cipher_text = open("message.txt").read()
print("".join(convert(c) for c in cipher_text))