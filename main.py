import flet as ft
import code as cd

def main (page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def generate_password(e):
        id = input_id.value
        password = f"{cd.main(id)} "
        password_generated.value += password

    generate_button = ft.ElevatedButton("GENERATE PASSWORD", on_click=generate_password)
    password_generated = ft.Text("PASSWORD: ")
    input_id = ft.TextField(label="Write Device ID here", value="")

    page.add(
        ft.Row([
            password_generated
        ],
        alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([
            input_id,
        ],
        alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([
            generate_button,
        ],
        alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)