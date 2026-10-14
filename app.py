
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cấu hình trang
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="📚",
    layout="wide"
)

st.title("📚 QUẢN LÝ ĐIỂM SINH VIÊN")
st.write("Ứng dụng quản lý và thống kê kết quả học tập của sinh viên.")

# 2. Tạo DataFrame
du_lieu = {
    "Họ và tên": [
        "Bùi Lê Nhã Thy",
        "Lê Nguyễn Bảo Ngân",
        "Nguyễn Châu Tuyết Anh",
        "Đỗ Hoàng Nhã",
        "Nguyễn Ái Xuân Trường",
        "Lý Nguyễn Thảo My",
        "Nguyễn Trần Quế Anh",
        "Nguyễn Nguyên Nhung",
        "Trương Huỳnh Nhật Vy",
        "Nguyễn Vinh Quang"
    ],
    "Điểm chuyên cần": [8, 9, 7, 6, 7, 10, 10, 8, 9, 9],
    "Điểm giữa kỳ": [7, 8, 6, 8, 9, 10, 10, 8, 8, 10],
    "Điểm cuối kỳ": [9, 8, 7, 6, 10, 8, 8, 9, 9, 10]
}

df = pd.DataFrame(du_lieu)

# 3. Tính điểm tổng kết
df["Điểm tổng kết"] = (
    df["Điểm chuyên cần"] * 0.2
    + df["Điểm giữa kỳ"] * 0.3
    + df["Điểm cuối kỳ"] * 0.5
)

# 4. Xếp loại sinh viên
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

# 5. Thống kê kết quả
st.subheader("📊 Thống kê kết quả học tập")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Điểm trung bình",
    f"{df['Điểm tổng kết'].mean():.2f}"
)
c2.metric(
    "Điểm cao nhất",
    f"{df['Điểm tổng kết'].max():.2f}"
)
c3.metric(
    "Điểm thấp nhất",
    f"{df['Điểm tổng kết'].min():.2f}"
)
c4.metric(
    "Số sinh viên đạt",
    f"{(df['Điểm tổng kết'] >= 5).sum()}/{len(df)}"
)

# 6. Bảng điểm hoàn chỉnh
st.subheader("📋 Bảng điểm sinh viên")

st.dataframe(
    df.round({"Điểm tổng kết": 2}),
    use_container_width=True,
    hide_index=True
)

# 7. Tra cứu sinh viên
st.subheader("🔎 Tra cứu điểm cá nhân")

ten_sv = st.selectbox(
    "Chọn sinh viên",
    df["Họ và tên"]
)

sv = df[df["Họ và tên"] == ten_sv].iloc[0]

st.write("**Họ và tên:**", sv["Họ và tên"])

a, b, c = st.columns(3)
a.metric("Điểm chuyên cần", f"{sv['Điểm chuyên cần']:.1f}")
b.metric("Điểm giữa kỳ", f"{sv['Điểm giữa kỳ']:.1f}")
c.metric("Điểm cuối kỳ", f"{sv['Điểm cuối kỳ']:.1f}")

d, e = st.columns(2)
d.metric("Điểm tổng kết", f"{sv['Điểm tổng kết']:.2f}")
e.metric("Xếp loại", sv["Xếp loại"])

# 8. Biểu đồ điểm tổng kết
st.subheader("📈 Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(12, 5))

ax.bar(
    df["Họ và tên"],
    df["Điểm tổng kết"]
)

ax.set_title("Điểm tổng kết của sinh viên")
ax.set_xlabel("Họ và tên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
ax.tick_params(axis="x", labelrotation=45)

plt.setp(ax.get_xticklabels(), ha="right")
fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

# 9. Thông tin người thực hiện
st.divider()
st.caption("BÀI TẬP PYTHON - QUẢN LÝ ĐIỂM SINH VIÊN")
st.write("Người thực hiện: [Nguyễn Ái Xuân Trường]")
```
