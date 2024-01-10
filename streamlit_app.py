import streamlit as st

from zp_fetch import ZPSession

st.set_page_config(layout="wide")

"""
# Welcome to Vincent's zwift data utility

You can also contact me on discord: [Vincent](discordapp.com/users/vincent.davis)

"""

st.write("Login to ZwiftPower using your Zwift account. No data is stored.")
username = None
password = None
if username is None:
    username = st.text_input(label="UserName", placeholder="username")
if password is None:
    password = st.text_input(label="Password", placeholder="password")

zps = ZPSession(login_data={"username": username, "password": password})

event_url = None
cat = None
format = None
if event_url is None:
    cat = st.radio(label="Category", options=["ALL", "A", "B", "C", "D", "E"])
    format = st.radio(label="Format", options=["msec", "elapsed"])
    event_url = st.text_input(
        label="Event URL (may take a few seconds)", placeholder="https://zwiftpower.com/events.php?zid=4073983"
    )
if event_url and cat and format:
    cat = cat.replace("ALL", "")
    df = zps.get_primes_from_url(event_url, cat, format)
    st.download_button(
        label="Download csv file",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name=f"Event_prime_ID_{id}_CAT_{cat}_FORMAT_{format}.csv",
        mime="text/csv",
    )
    st.dataframe(df)
