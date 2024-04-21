from tkinter import Tk, Canvas, Button, PhotoImage
from pathlib import Path
from Guess_Age_Gender import *

def back_to_main(back_to_main_screen, window):
    window.destroy()
    back_to_main_screen()

def predict_age_gender(window, back_to_main_screen):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame1")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=600,
        width=900,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        1.0,
        900.0,
        49.0,
        fill="#0006A0",
        outline=""
    )
    canvas.create_text(
        42.0,
        6.0,
        anchor="nw",
        text="Analyze Face",
        fill="#FFFFFF",
        font=("Inter ExtraBold", 30 * -1)
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
        x=700.0,
        y=513.0,
        width=165.0,
        height=45.0
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
    recognize_age_gender_camera(canvas_video)  

    window.resizable(False, False)
    window.mainloop()
