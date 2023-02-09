import flet as ft

def main(page: ft.Page):
    page.title="Trabajo selección de equipo"
    #listaequipos = ["Real Madrid", "Liverpool", "Manchester City", "Manchester United", "Bayern de Múnich", "Paris Saint Germain", "Atletico de Madrid", "Arsenal", "FC Barcelona", "Borussia Dortmund"]
    listaseleccionados = []

    lv = ft.ListView(expand=2, spacing=10, padding=10, auto_scroll=True)

    def añadirFichero(x):
        p = open("Equipos_Seleccionados.txt", "w")
        for i in listaseleccionados:
            p.write(i+"/")
        p.close()
    
    def abrirFichero():
        vEquiposFichero = []
        #/home/raullm/Documentos/GitKraken/Seleccion_De_Equipos/Equipos.txt
        #/home/joseangelmartosplazas/Documentos/Seleccion_De_Equipos/Equipos.txt
        f = open("Equipos.txt","r")
        for linea in f:
            lineasl = linea.replace("\n","")
            vEquiposFichero.append(lineasl)
        f.close()        
        print (vEquiposFichero)
        return(vEquiposFichero)


    def funcionalidadboton(i):
        sel = menu.value
        if (listaseleccionados.count(sel) == 0):
            listaseleccionados.append(menu.value)
            row = ft.Row(spacing=10, controls = [ft.Text(sel),ft.Image(width=20, height=20, src=f"Imagenes\{sel}.png")])
            lv.controls.append(row)
            print(listaseleccionados)
        else:
            dlg = ft.AlertDialog(
            title=ft.Text("No puedes seleccionar el mismo equipo"))
            page.dialog = dlg
            dlg.open = True

        page.update()


    def imagen(e):
        if menu.value=="Liverpool":
        
            img.src="Liverpool.png"
    
        elif menu.value=="Real Madrid":
        
            img.src="Real Madrid.png"
        elif menu.value=="Manchester City":
        
            img.src="Manchester City.png"
        elif menu.value=="Manchester United":
        
            img.src="Manchester United.png"
        elif menu.value=="Bayern de Múnich":
        
            img.src="Bayern de Múnich.png"
        elif menu.value=="Atletico de Madrid":
        
            img.src="Atletico de Madrid.png"
        elif menu.value=="Arsenal":
        
            img.src="Arsenal.png"
        elif menu.value=="FC Barcelona":
        
            img.src="FC Barcelona.png"
        elif menu.value=="Borussia Dortmund":
        
            img.src="Borussia Dortmund.png"
        else:
            menu.value=="Paris Saint Germain"
        
            img.src="Paris Saint Germain.png"
        page.update()

    
    #Inicio programa principal

    menu =  ft.Dropdown(label="Equipos",hint_text="Elige tu equipo", autofocus=True, on_change=imagen)
    
    
    listaequipos = abrirFichero()
    
    for e in listaequipos:
        menu.options.append(ft.dropdown.Option(e))
   
    
    img = ft.Image(
        src=f"d",
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
    )

    btn_añadir_equipo = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=funcionalidadboton)
    btn_añadir_fichero = ft.FloatingActionButton(icon=ft.icons.ABC, on_click=añadirFichero)
    row2 = ft.Row(spacing=10, controls=[btn_añadir_equipo, btn_añadir_fichero])

    page.add(menu,img, lv, row2)

ft.app(target=main, assets_dir="Imagenes")