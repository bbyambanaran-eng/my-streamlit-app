import streamlit as st
import pandas as pd

st.set_page_config(page_title="Борлуулалтын график", page_icon="📊")

st.title("Бүтээгдэхүүний борлуулалт")
st.write("Бүтээгдэхүүн сонгоод сарын борлуулалтыг графикаар хараарай.")

sales = {
    "Сар": ["1-р сар", "2-р сар", "3-р сар", "4-р сар", "5-р сар", "6-р сар"],
    "Кофе": [120, 150, 135, 180, 170, 210],
    "Цай": [90, 110, 105, 130, 125, 160],
    "Жүүс": [140, 125, 160, 155, 190, 220],
}

df = pd.DataFrame(sales).set_index("Сар")

selected_product = st.selectbox(
    "Бүтээгдэхүүн сонгоно уу:",
    ["Кофе", "Цай", "Жүүс"]
)

st.subheader(f"{selected_product} — сарын борлуулалт")
st.bar_chart(df[selected_product])

st.write(f"Нийт борлуулалт: **{df[selected_product].sum()} ширхэг**")