import flet as ft

def main(page: ft.Page):
    page.title="Trabajo selección de equipo"

    def imagen(e):
        if menu.value=="Liverpool":
        
            img.src="Liverpool.png"
    
        elif menu.value=="Real Madrid":
        
            img.src="Real Madrid.png"
        elif menu.value=="Manchester City":
        
            img.src="Manchester City.png"
        elif menu.value=="Bayern de Múnich":
        
            img.src="Bayern de munich.png"
        else:
            menu.value=="Paris Saint Germain"
        
            img.src="Paris Saint Germain.jpeg"
        page.update()

    menu =  ft.Dropdown(label="Equipos",hint_text="Elige tu equipo",options=[
            ft.dropdown.Option("Real Madrid"),
            ft.dropdown.Option("Manchester City"),
            ft.dropdown.Option("Liverpool"),
            ft.dropdown.Option("Bayern de Múnich"),
            ft.dropdown.Option("Paris Saint Germain"),
            ], autofocus=True, on_change=imagen)
    
    img = ft.Image(
        src=f"d",
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
    )
    
    page.add(menu,img)






ft.app(target=main, assets_dir="Imagenes")