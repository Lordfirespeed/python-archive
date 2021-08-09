def a2b(msg, tofile):
    if not tofile:
        return bin(int.from_bytes(msg.encode(), 'big'))
    else:
        with open('Binary.txt', 'w') as file:
            file.write(bin(int.from_bytes(msg.encode(), 'big')))


def b2a(bin, fromfile):
    if not fromfile:
        n = int(bin, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    else:
        with open('Binary.txt', 'r') as file:
            string = (file.read()).replace(" ", "")
            n = int(string, 2)
        with open('Text.txt', 'w') as file:
            file.write(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
