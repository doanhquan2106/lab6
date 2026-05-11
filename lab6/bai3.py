import hashlib
import os

def calculate_hash(file_path):
    """Hàm tính mã SHA-256 của một file"""
    hash_sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def simulate_file_transfer():
    # 1. MÔ PHỎNG PHÍA NGƯỜI GỬI (SENDER)
    file_name = "document.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("Dữ liệu quan trọng: Chuyển khoản 100 triệu đồng.") 
    
    print(f"[GỬI] Đang chuẩn bị file: {file_name}")
    sender_hash = calculate_hash(file_name)
    print(f"[GỬI] Mã Hash gốc: {sender_hash}")
    print("-" * 50)

    # 2. MÔ PHỎNG QUÁ TRÌNH TRUYỀN TẢI (TRÊN ĐƯỜNG TRUYỀN)
    # Giả sử hacker can thiệp vào file hoặc lỗi đường truyền
    attack = input("Tôi là hackker? (y/n): ").lower()
    if attack == 'y':
        with open(file_name, "w", encoding="utf-8") as f:
            f.write("Dữ liệu quan trọng: Chuyển khoản 1 đồng.") # Hacker sửa nội dung
        print("!!! CẢNH BÁO: File đã bị chỉnh sửa trên đường truyền !!!")
    else:
        print("... File được truyền đi an toàn ...")
    print("-" * 50)

    # 3. MÔ PHỎNG PHÍA NGƯỜI NHẬN (RECEIVER)
    print(f"[NHẬN] Đã nhận được file. Đang kiểm tra tính toàn vẹn...")
    receiver_hash = calculate_hash(file_name)
    print(f"[NHẬN] Mã Hash tính toán lại: {receiver_hash}")

    # Bước quan trọng nhất: So sánh
    if receiver_hash == sender_hash:
        print("=> KẾT QUẢ: File AN TOÀN và NGUYÊN VẸN. (Khớp mã Hash)")
    else:
        print("=> KẾT QUẢ: File ĐÃ BỊ THAY ĐỔI HOẶC LỖI! (Mã Hash không khớp)")

    # Dọn dẹp file tạm sau khi chạy xong
    if os.path.exists(file_name):
        os.remove(file_name)

if __name__ == "__main__":
    simulate_file_transfer()