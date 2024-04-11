import streamlit as st
import pandas as pd
import altair as alt

def run():
    data = pd.read_csv("../archive/shopping_behavior_updated.csv")

    st.set_page_config(
        page_title="Lab6",
        page_icon="💻",
    )

    st.write("# Adv. Python Lab 6")

    st.markdown(
        """
        Develop a Streamlit app for a retail company aiming to analyze consumer behavior and shopping
        habits. The company has provided a dataset encompassing customer demographics,
        purchase history, product preferences, and shopping channels. The objective of this
        exercise is to create a visually engaging and interactive app that focuses on utilizing data
        visualizations to provide insightful analytics.
        """
    )

    st.text("")
    st.subheader("Dataset Overview")
    st.write(data.head())

    st.text("")
    st.text("")
    st.text("")
    @st.cache_data
    def create_donut_chart(data, column, use_container_width=True):
        value_counts = data[column].value_counts().reset_index()
        value_counts.columns = ['category', 'value']
        
        chart = alt.Chart(value_counts).mark_arc(innerRadius=50).encode(
            theta=alt.Theta(field="value", type="quantitative"),
            color=alt.Color(field="category", type="nominal"),
        )

        st.altair_chart(chart, use_container_width=use_container_width)


    st.subheader('Donut Charts')

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.write("#### Gender Distribution")
        create_donut_chart(data, 'Gender')

    with col2:
        st.write("#### Season Distribution")
        create_donut_chart(data, 'Season')

    with col3:
        st.write("#### Frequency of Purchases Distribution")
        create_donut_chart(data, 'Frequency of Purchases')

    with col4:
        st.write("#### Category Distribution")
        create_donut_chart(data, 'Category')

    sales_by_location = data.groupby('Location')['Purchase Amount (USD)'].sum()
    average_purchase_by_location = data.groupby('Location')['Purchase Amount (USD)'].mean()

    st.subheader('Sales Metrics by Location')

    st.write('#### Total Sales by Location')
    st.bar_chart(sales_by_location)

    st.write('#### Average Purchase Amount by Location')
    st.bar_chart(average_purchase_by_location)

    ##
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.subheader("Bar Chart")
    x_column0 = st.selectbox('Select X axis:', data.columns, index=data.columns.get_loc('Season'))
    y_column0 = st.selectbox('Select Y axis:', data.columns, index=data.columns.get_loc('Purchase Amount (USD)'), key=2)
    st.text("")
    average_purchase_by_season = data.groupby(x_column0)[y_column0].mean()

    st.bar_chart(average_purchase_by_season)


    ##
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.subheader("Line Chart")
    x_column1 = st.selectbox('Select X axis:', data.columns, index=data.columns.get_loc('Age'))
    y_column1 = st.selectbox('Select Y axis:', data.columns, index=data.columns.get_loc('Purchase Amount (USD)'))
    st.text("")
    average_purchase_by_age = data.groupby(x_column1)[y_column1].mean()

    st.line_chart(average_purchase_by_age)


    ##
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.subheader("Scatterplot")
    x_column2 = st.selectbox('Select X axis:', data.columns, index=data.columns.get_loc('Age'), key=5)
    y_column2 = st.selectbox('Select Y axis:', data.columns, index=data.columns.get_loc('Purchase Amount (USD)'), key=3)
    st.text("")
    st.scatter_chart(data[[x_column2, y_column2]][:50])


if __name__ == "__main__":
    run()