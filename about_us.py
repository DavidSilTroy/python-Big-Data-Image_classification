import streamlit as st


def about_us():
    st.header('Thomas More Geel - Big Data')
    st.subheader('Team 1: JAD Solutions')
    # body =  st.container()
    # body.write("Coming soon.... (in Winter)")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("assets/img/Jetze Luyten.png")
        st.subheader("Jetze Luyten")
        st.markdown("[Github](https://github.com/JetzeLuyten)")

    with col2:
        st.image("assets/img/Axel Van Gestel.png")
        st.subheader("Axel Van Gestel")
        st.markdown("[Github](https://github.com/A-Van-Gestel)")

    with col3:
        image = st.image("assets/img/David Silva.png")
        st.subheader("David Silva")
        st.markdown("[Github](https://github.com/DavidSilTroy)")
