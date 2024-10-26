import flet as ft
from country_dict import country_flags_dict

class FlagImage(ft.Image):
    def __init__(self, src):
        super().__init__()
        self.flag_image = ft.Image(width=250, height=175, src=src)

class FlagName(ft.Text):
    def __init__(self, name):
        super().__init__()
        self.flag_name = ft.Text(color="white",value=name,size=20)

class Move(ft.IconButton):
    def __init__(self, on_backward, on_forward):
        super().__init__()
        self.backward = ft.IconButton(
            icon=ft.icons.ARROW_BACK_IOS_NEW_ROUNDED,
            on_click=on_backward
        )
        self.forward = ft.IconButton(
            icon=ft.icons.ARROW_FORWARD_IOS_ROUNDED,
            on_click=on_forward
        )
        self.content = [self.backward, self.forward]

class FlagApp(ft.Container):
    def __init__(self, image, name, move):
        super().__init__()
        self.content = ft.Column(
            [
                ft.Row(controls=[image.flag_image], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(controls=[name.flag_name], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(controls=move.content, alignment=ft.MainAxisAlignment.CENTER),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

def main(page: ft.Page):
    page.title = "Flag Display"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#0C0A3E"

    flag_data = list(country_flags_dict.items())
    current_index = 0

    def update_display():
        flag_code, (flag_name, flag_src) = flag_data[current_index]
        image.flag_image.src = flag_src
        name.flag_name.value = flag_name
        page.update()

    def on_backward(e):
        nonlocal current_index
        current_index = (current_index - 1) % len(flag_data)
        update_display()

    def on_forward(e):
        nonlocal current_index
        current_index = (current_index + 1) % len(flag_data)
        update_display()

    # Initialize components
    flag_code, (initial_name, initial_src) = flag_data[current_index]
    image = FlagImage(initial_src)
    name = FlagName(initial_name)
    move = Move(on_backward, on_forward)
    app = FlagApp(image, name, move)

    # Add components to the page
    page.add(app)
    update_display()

ft.app(target=main, assets_dir="png250px")