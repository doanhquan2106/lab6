import hashlib

def calculate_sha512(file_path):
    """Hàm tính mã SHA-512 của một file"""
    hash_sha512 = hashlib.sha512()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha512.update(chunk)
        return hash_sha512.hexdigest()
    except FileNotFoundError:
        return None

def so_sanh_hai_anh():
    # 1. Khai báo tên 2 file ảnh bạn đã tải về 
    anh_1 = "images - Sao chép.png" 
    anh_2 = "images.png" # Tên file ảnh thứ 2 trong thư mục của bạn
    
    print(f"--- SO SÁNH TÍNH TOÀN VẸN GIỮA 2 FILE ---")
    
    # 2. Tính toán mã băm cho từng ảnh
    hash_1 = calculate_sha512(anh_1)
    hash_2 = calculate_sha512(anh_2)
    
    if hash_1 is None or hash_2 is None:
        print("Lỗi: Kiểm tra lại tên file ảnh trong thư mục!")
        return

    # 3. Hiển thị kết quả băm
    print(f"\n[Ảnh 1]: {anh_1}")
    print(f"Mã Hash: {hash_1}")
    
    print(f"\n[Ảnh 2]: {anh_2}")
    print(f"Mã Hash: {hash_2}")
    
    print("-" * 50)

    # 4. So sánh và đưa ra kết luận
    if hash_1 == hash_2:
        print("=> KẾT QUẢ: Hai ảnh hoàn toàn GIỐNG NHAU về nội dung dữ liệu.")
    else:
        print("=> KẾT QUẢ: Hai ảnh KHÁC NHAU. (Mã Hash không khớp)")

if __name__ == "__main__":
    so_sanh_hai_anh()