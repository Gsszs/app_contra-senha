import flet as ft
import password as cd

def main (page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def generate_password(e):
        if (len(input_id.value) == 11):
            if (input_id.value[-1].isdigit()):
                print(f"Input id -1 = {input_id.value[-1]}")
                id = input_id.value
                password = f"{cd.main(id)}\n"
                password_generated.value = f"Password: \n{password}"
                password_generated.color = "#ffffff"
                input_id.error_text = ""
            else:
                input_id.error_text = "ERROR: ID is incorrect."
        elif(len(input_id.value) < 11 or len(input_id.value) > 11):
            input_id.error_text = "ERROR: Write correct ID (11 caracters)."
        else:
            input_id.error_text = "ERROR: Generate ID error."
        
        page.update()

    generate_button = ft.ElevatedButton("GENERATE PASSWORD", on_click=generate_password, color=ft.colors.GREEN_400)
    password_generated = ft.Text("\nPassword: ", size=28, weight=ft.FontWeight.W_400, color="#3D3D3D")
    input_id = ft.TextField(label="Write Device ID here", value="")

    page.add(
        ft.Row([
            input_id,
        ],
        alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([
            generate_button,
        ],
        alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([
            password_generated,
        ],
        alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)