import streamlit as st
import pandas as pd

def main():
    df = pd.read_csv("01 Spotify.csv")

    df.set_index("Artist", inplace=True)
    st.bar_chart(df[df["Stream"] > 1000000000]["Stream"])


if __name__ == "__main__":
    main()
