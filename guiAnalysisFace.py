from pathlib import Path
from tkinter import Canvas, Button, PhotoImage
from Analysis_Face import *

def back_to_main(back_to_main_screen, window):
    window.destroy()
    back_to_main_screen()
def analyze_face_accurate(window, back_to_main_screen):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 600,
        width = 900,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        1.0,
        900.0,
        49.0,
        fill="#0006A0",
        outline="")

    canvas.create_text(
        42.0,
        6.0,
        anchor="nw",
        text="Analyze Face",
        fill="#FFFFFF",
        font=("Inter ExtraBold", 30 * -1)
    )

    canvas_video = Canvas(
            window,
            bg="#D9D9D9",
            height=451,
            width=606,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
    canvas_video.place(x=20, y=100)
    text_info = canvas.create_text(
        20, 20, 
        anchor="nw", 
        text="", 
        fill="#000000", 
        font=("Inter SemiBold", 14)
    )  
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back_to_main(back_to_main_screen, window),
        relief="flat"
    )
    button_1.place(
        x=720.0,
        y=513.0,
        width=165.0,
        height=45.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: capture_face(canvas_video, window),
        relief="flat"
    )
    button_2.place(
        x=720.0,
        y=440.0,
        width=165.0,
        height=48.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: capture_and_analyze_face_from_file(canvas_video),
        relief="flat"
    )
    button_3.place(
        x=720.0,
        y=322.0,
        width=165.0,
        height=48.0
    )

    canvas.create_text(
        782.0,
        395.0,
        anchor="nw",
        text="or",
        fill="#000000",
        font=("Inter SemiBold", 30 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
