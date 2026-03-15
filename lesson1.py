import pandas as pd

try:
    data = pd.read_csv('scores.csv', encoding='utf-8')
    
    # Hiển thị 5 dòng đầu tiên thay vì toàn bộ (tiết kiệm không gian)
    print("--- 5 dòng đầu tiên ---")
    print(data.head())
    
    # Kiểm tra cấu trúc dữ liệu
    print("\n--- Thông tin dữ liệu ---")
    data.info()
    
    # Kiểm tra các giá trị thống kê cơ bản (trung bình, min, max...)
    print("\n--- Thống kê mô tả ---")
    print(data.describe())

except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'scores.csv'. Hãy kiểm tra lại đường dẫn.")