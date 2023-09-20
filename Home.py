import streamlit as st
import pandas as pd

st.write("""
         # Chatbot Prototype
         """)
st.markdown("This is a paragraph and it looks awesome!")

left_column, right_column = st.columns(2)

left_column.button("Press me!")

with right_column:
    chosen = st.radio(
        'Sorting hat', ("Testing", "testing 2", "testing3", "testing4"))
    st.write(f"You are in the {chosen} house!")


def load_data():
    data = pd.read_csv("world-data-2023.csv")
    return data


def main():
    st.title("Countries of the World (2023)")

    df = load_data()

#     st.write("""## Data Overview

# This should be a body of text
#              """)
    st.write(df.head())

    num_rows = st.slider("Select number of rows to display: ", 5, 100, 10)
    st.dataframe(df.head(num_rows))

    st.line_chart(df["GDP"])


if __name__ == "__main__":
    main()
