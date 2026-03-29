import streamlit as st
import pandas as pd
import plotly.express as px

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

#per day
st.subheader("Revenue per Day 📈")
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
df_clean = df.dropna(subset=['Date'])
daily_revenue = df_clean.groupby(df_clean['Date'].dt.date)['Total_Price'].sum().reset_index()

fig_area = px.area(daily_revenue, x='Date', y='Total_Price', markers=True,
                   color_discrete_sequence=['#2ecc71'])
st.plotly_chart(fig_area, use_container_width=True)

#top menus
st.subheader("Top 5 Best Selling Menu 🏆")
top5 = df.groupby('Menu_Name')['Qty'].sum().sort_values(ascending=False).head(5).reset_index()

fig_bar = px.bar(top5, x='Qty', y='Menu_Name', orientation='h',
                 color='Qty', color_continuous_scale='YlOrRd')
fig_bar.update_layout(yaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig_bar, use_container_width=True)

#per menu
st.subheader("Revenue Proportion 🍩")
revenue_menu = df.groupby('Menu_Name')['Total_Price'].sum().reset_index()

fig_pie = px.pie(revenue_menu, values='Total_Price', names='Menu_Name', hole=0.2,
                 color_discrete_sequence=px.colors.qualitative.Pastel)
fig_pie.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig_pie, use_container_width=True)

#nutrition per order
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
col_n1.metric("🔥 แคลอรี่ (kcal)", f"{cal}")
col_n2.metric("🥩 โปรตีน (g)", f"{protein}")
col_n3.metric("🍚 คาร์บ (g)", f"{carb}")
col_n4.metric("🥑 ไขมัน (g)", f"{fat}")
col_n5.metric("🍬 น้ำตาล (g)", f"{sugar}")
