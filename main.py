import flet as ft

def main(page: ft.Page):
    page.theme_mode = 'LIGHT'
    page.title = "Login Example"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def login(e):
        if username.value == "admin" and password.value == "admin":
            page.clean()
            show_home_page()
        else:
            error_message.value = "Invalid username or password!"
            page.update()

    def show_home_page():
        def go_to_page(e):
            content.value = f"Welcome to the {e.control.data} page!"
            page.update()

        nav_bar = ft.Row(
            [
                ft.IconButton(icon=ft.icons.HOME, data="Home", on_click=go_to_page),
                ft.IconButton(icon=ft.icons.PERSON, data="Profile", on_click=go_to_page),
                ft.IconButton(icon=ft.icons.SETTINGS, data="Settings", on_click=go_to_page)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )
        
        content = ft.Text(value="Welcome to the Home page!", text_align=ft.TextAlign.CENTER)
        page.add(nav_bar, content)

    username = ft.TextField(label="Username", width=200)
    password = ft.TextField(label="Password", password=True, width=200)
    login_button = ft.ElevatedButton(text="Login", on_click=login, width=200)
    error_message = ft.Text(color=ft.colors.RED, text_align=ft.TextAlign.CENTER)

    login_form = ft.Column(
        [username, password, login_button, error_message],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )
    page.add(login_form)

ft.app(target=main)
