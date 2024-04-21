
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


def back_to_main(back_to_main_screen, window):
    window.destroy()
    back_to_main_screen()

def show_user_manual(window, back_to_main_screen):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame2")


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
        423.0,
        0.0,
        900.0,
        600.0,
        fill="#1CDEEA",
        outline="")

    canvas.create_rectangle(
        0.0,
        0.0,
        423.0,
        82.0,
        fill="#0006A0",
        outline="")

    canvas.create_text(
        31.0,
        10.0,
        anchor="nw",
        text="Analyze Face",
        fill="#FFFFFF",
        font=("Inter ExtraBold", 40 * -1)
    )

    canvas.create_text(
        146.0,
        221.0,
        anchor="nw",
        text="User manual",
        fill="#000000",
        font=("Inter ExtraBold", 40 * -1)
    )

    canvas.create_text(
        31.0,
        158.0,
        anchor="nw",
        text="Analysis Face !",
        fill="#000000",
        font=("Inter ExtraBold", 40 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        185.0,
        417.0,
        image=image_image_1
    )

    canvas.create_text(
        450.0,
        151.0,
        anchor="nw",
        text="Usage options:\n\n  1. Accurate facial analysis:     \n       - Analyze faces using photos from the camera.     \n       - Analysis from imported image files.\n\n2. Real-time facial analysis",
        fill="#FFFFFF",
        font=("Inter SemiBold", 22 * -1)
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
        x=120.0,
        y=513.0,
        width=165.0,
        height=45.0
    )
    window.resizable(False, False)
    window.mainloop()