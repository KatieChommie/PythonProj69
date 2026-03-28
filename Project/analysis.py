import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("daily_sales.csv")

st.title("Restaurant Sales Dashboard 📊")

total_revenue = df['Total_Price'].sum()
total_orders = df['Order_ID'].nunique()
avg_order_value = total_revenue / total_orders if total_orders > 0 else 0

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue 💰", f"{total_revenue:,.0f} บาท")
col2.metric("Total Orders 🧾", total_orders)
col3.metric("Avg Order Value 📊", f"{avg_order_value:,.2f} บาท")

# Raw Data
st.subheader("Raw Data 📄")
st.dataframe(df)

st.subheader("Revenue per Day 📈")

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
df_clean = df.dropna(subset=['Date'])

daily_revenue = df_clean.groupby(df_clean['Date'].dt.date)['Total_Price'].sum()

st.bar_chart(daily_revenue)

st.subheader("Top 5 Best Selling Menu 🏆")
top5 = (
    df.groupby('Menu_Name')['Qty']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
st.bar_chart(top5)

st.subheader("Revenue per Menu 💵")
revenue_menu = (
    df.groupby('Menu_Name')['Total_Price']
    .sum()
    .sort_values(ascending=False)
)
st.bar_chart(revenue_menu)

st.subheader("Nutrition per Order 🥗")
order = st.selectbox("เลือกรายการออเดอร์ (Order ID)", df['Order_ID'].unique())
order_df = df[df['Order_ID'] == order]

cal = order_df['Cal'].sum()
protein = order_df['Protein'].sum()
carb = order_df['Carb'].sum()
fat = order_df['Fat'].sum()
sugar = order_df['Sugar'].sum()

st.write(f"**ข้อมูลโภชนาการรวมของบิลเลขที่:** `{order}`")
col_n1, col_n2, col_n3, col_n4, col_n5 = st.columns(5)
col_n1.metric("🔥 แคลอรี่", f"{cal} kcal")
col_n2.metric("🥩 โปรตีน", f"{protein} g")
col_n3.metric("🍚 คาร์บ", f"{carb} g")
col_n4.metric("🥑 ไขมัน", f"{fat} g")
col_n5.metric("🍬 น้ำตาล", f"{sugar} g")
