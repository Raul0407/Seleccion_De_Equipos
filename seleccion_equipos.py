import flet as ft

def main(page: ft.Page):
    page.title="Trabajo selección de equipo"

    menu =  ft.Dropdown(label="Equipos",hint_text="Elige tu equipo",options=[
            ft.dropdown.Option("Real Madrid"),
            ft.dropdown.Option("Manchester City"),
            ft.dropdown.Option("Liverpool"),
            ft.dropdown.Option("Bayern de Múnich"),
            ft.dropdown.Option("Paris Saint Germain"),
            ], autofocus=True)

    img = ft.Image(
        src=f"Real Madrid.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    
    page.add(img)
    page.add(menu)





ft.app(target=main, assets_dir="Imagenes")