import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Spotify Streamers",
    page_icon=":musical_note:",
    layout="wide",
)

def main():
    df = pd.read_csv("01 Spotify.csv")

    df.set_index("Track", inplace=True)

    artists = df["Artist"].value_counts().index
    artist = st.selectbox("Artista", artists)
    df_artist = df[df["Artist"] == artist]

    albums = df_artist["Album"].value_counts().index
    album = st.selectbox("Álbum", albums)
    df_album = df[df["Album"] == album]

    display = st.checkbox("Display")

    if display:
        st.bar_chart(df_album["Stream"])


if __name__ == "__main__":
    main()
