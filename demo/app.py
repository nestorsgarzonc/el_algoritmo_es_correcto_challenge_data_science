from screens.home import home
from screens.demo import demo
from screens.about_us import about_us
from components.sidebar import sidebar
import streamlit as st

PAGES = {
    "Inicio": home,
    "Demo": demo,
    "Sobre nosotros": about_us,
}


if __name__ == '__main__':
    selection = sidebar(PAGES)
    page = PAGES[selection]()
