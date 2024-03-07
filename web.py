import streamlit as st
import main


current_video = st.video(main.links[main.num])

next_button = st.button('Next')
pre_button = st.button('Previous')

if next_button:
    main.num += 1


if pre_button:
    main.num -= 1




