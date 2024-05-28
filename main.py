import flet as ft
import code as cd

def main (page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def generate_password(e):
        id = input_id.value
        password = f"{cd.main(id)}\n"
        if (len(password) < 10):
            input_id.error_text = "ERROR: Id is not validated."
        else:
            input_id.error_text = ""
            input_id.value = ""
            password_generated.value = f"PASSWORD: {password}"
            password_generated.color = "#ffffff"
        page.update()

    generate_button = ft.ElevatedButton("GENERATE PASSWORD", on_click=generate_password)
    password_generated = ft.Text("PASSWORD: None", size=30, weight=ft.FontWeight.W_800, color="#3D3D3D")
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