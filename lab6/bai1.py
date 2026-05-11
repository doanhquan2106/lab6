import hashlib

def hash_data(data):
    sha256 = hashlib.sha256(data.encode()).hexdigest()
    sha512 = hashlib.sha512(data.encode()).hexdigest()
    return sha256, sha512


text = input("Nhập dữ liệu cần băm: ")

sha256_hash, sha512_hash = hash_data(text)

print("\nKết quả băm:")
print("SHA-256:", sha256_hash)
print("SHA-512:", sha512_hash)


# Nhập dữ liệu lần 2 để so sánh
text2 = input("\nNhập lại dữ liệu để kiểm tra : ")

sha256_hash2, sha512_hash2 = hash_data(text2)

print("\nKết quả lần 2:")
print("SHA-256:", sha256_hash2)
print("SHA-512:", sha512_hash2)


# So sánh
if sha256_hash == sha256_hash2:
    print("\n SHA-256: Không thay đổi")
else:
    print("\n SHA-256: Đã thay đổi")

if sha512_hash == sha512_hash2:
    print(" SHA-512: Không thay đổi")
else:
    print(" SHA-512: Đã thay đổi")