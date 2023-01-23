import flet as ft

def main(page: ft.Page):
    page.title="Trabajo selección de equipo"
    listaequipos = ["Real Madrid", "Liverpool", "Manchester City", "Bayern de Múnich", "Paris Saint Germain"]
    

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

    
    
    menu =  ft.Dropdown(label="Equipos",hint_text="Elige tu equipo", autofocus=True, on_change=imagen)
    
    
    
    
    for e in listaequipos:
        menu.options.append(ft.dropdown.Option(e))
   
    
    img = ft.Image(
        src=f"d",
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
    )
    
    page.add(menu,img)






ft.app(target=main, assets_dir="Imagenes")