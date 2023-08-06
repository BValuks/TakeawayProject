from lib.menu import Menu

def test_formatted_menu_returns_formatted_menu():
    menu = Menu()
    assert menu.formatted_menu == 