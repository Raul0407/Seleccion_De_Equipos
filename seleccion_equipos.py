import flet as ft


def main(page:ft.Page):
    page.title="Trabajo selección de equipo"

    img = ft.Image(
        src=f"Real Madrid.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    
    page.add(img)





ft.app(target=main, assets_dir="Imagenes")