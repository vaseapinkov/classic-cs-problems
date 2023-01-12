def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()


key1 = int(input("Key 1: "))  # 16493641440011151697716960069
key2 = int(input("Key 2: "))  # 38741633540093441350658408292

print(decrypt(key1, key2))
