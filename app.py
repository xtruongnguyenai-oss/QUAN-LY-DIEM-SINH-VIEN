#1. Tạo DataFrame
import streamlit as st
import pandas as pd

du_lieu = {
    "Họ và tên": ["Bùi Lê Nhã Thy", "Lê Nguyễn Bảo Ngân", "Nguyễn Châu Tuyết Anh", "Đỗ Hoàng Nhã", "Nguyễn Ái Xuân Trường", 
               "Lý Nguyễn Thảo My", "Nguyễn Trần Quế Anh", "Nguyễn Nguyên Nhung", "Trương Huỳnh Nhật Vy", "Nguyễn Vinh Quang"],
    "Điểm chuyên cần": [8, 9, 7, 6, 7, 10, 10, 8, 9, 9],
    "Điểm giữa kỳ": [7, 8, 6, 8, 9, 10, 10, 8, 8, 10],
    "Điểm cuối kỳ": [9, 8, 7, 6, 10, 8, 8, 9, 9, 10]
}

df = pd.DataFrame(du_lieu)

st.dataframe(df)

#2. Tính điểm tổng kết
df['Điểm tổng kết']= (
    df["Điểm chuyên cần"] * 0.2
    + df["Điểm giữa kỳ"] * 0.3
    + df["Điểm cuối kỳ"] * 0.5
)
st.dataframe(df)

#3. Xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["Xếp loại"] = df["Điểm tổng kết"].apply(xep_loai)

st.dataframe(df)

# 4. Thống kê điểm sinh viên

# Tính điểm trung bình
print("Điểm trung bình:", round(df["Điểm tổng kết"].mean(), 2))

# Tìm sinh viên có điểm cao nhất
print("\nSinh viên có điểm cao nhất:")
print(df.loc[df["Điểm tổng kết"].idxmax()].to_string())

# Tìm sinh viên có điểm thấp nhất
print("\nSinh viên có điểm thấp nhất:")
print(df.loc[df["Điểm tổng kết"].idxmin()].to_string())

# Đếm số sinh viên đạt từ 5 điểm trở lên
print("\nSố sinh viên đạt:", (df["Điểm tổng kết"] >= 5).sum())

#5 Trực quan hóa
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))

plt.bar(df["Họ và tên"], df["Điểm tổng kết"])

plt.title("Điểm tổng kết của sinh viên")
plt.xlabel("Họ và tên")
plt.ylabel("Điểm tổng kết")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()

