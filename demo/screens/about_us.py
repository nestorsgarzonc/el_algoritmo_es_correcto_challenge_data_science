import streamlit as st


def about_us():
    st.title('Team')
    col1, col2 = st.beta_columns(2)
    col1.markdown('### Nestor Sebastian Garzon Contreras')
    col1.markdown('Estudiante de ingenieria de \nsistemas y computacion')
    col1.image(
        'https://media-exp1.licdn.com/dms/image/C4E03AQHOZDtz42bCXg/profile-displayphoto-shrink_800_800/0/1579381204249?e=1624492800&v=beta&t=_8ja6JfaNrv4gUDmD2nPsuSkTAIpsNeSBjyM8IDDe34',
        width=150
    )
    col1.markdown(
        '[LinkedIn](https://www.linkedin.com/in/sebastiangarzonc/)'
    )

    col2.markdown('### Santiago Leonardo Delgado Mejia')
    col2.markdown('Estudiante de ingenieria de \nsistemas y computacion')
    col2.image(
        'https://media-exp1.licdn.com/dms/image/C4E03AQGCSIROThgeXA/profile-displayphoto-shrink_800_800/0/1591926647586?e=1624492800&v=beta&t=6rfLe_H8ycpDEwYoltbwDyIqNJL2G_jvtibodLJGfVo',
        width=150
    )
    col2.markdown(
        '[LinkedIn](https://www.linkedin.com/in/santiago-leonardo-delgado-mej%C3%ADa-8a97811a8/)'
    )
