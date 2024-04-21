from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from guiAnalysisFace import analyze_face_accurate
from guiManual import show_user_manual
from guiPredictFace import predict_age_gender
def destroy_window(window):
    window.destroy()
def main():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame3")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Tk()
    window.geometry("900x600")
    window.configure(bg="#FFFFFF")

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
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: predict_age_gender(window=window, back_to_main_screen=main),
        relief="flat"
    )
    button_1.place(
        x=450.0,
        y=369.0,
        width=405.0,
        height=70.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: analyze_face_accurate(window=window, back_to_main_screen=main),
        relief="flat"
    )
    button_2.place(
        x=450.0,
        y=268.0,
        width=405.0,
        height=70.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_user_manual(window=window, back_to_main_screen=main),
        relief="flat"
    )
    button_3.place(
        x=450.0,
        y=468.0,
        width=265.0,
        height=45.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: destroy_window(window),
        relief="flat"
    )
    button_4.place(
        x=720.0,
        y=470.0,
        width=135.0,
        height=43.0
    )

    canvas.create_rectangle(
        0.0,
        1.0,
        900.0,
        78.0,
        fill="#0006A0",
        outline="")

    canvas.create_rectangle(
        0.0,
        1.0,
        900.0,
        78.0,
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
        61.0,
        381.0,
        anchor="nw",
        text="Wellcome to ",
        fill="#000000",
        font=("Inter ExtraBold", 40 * -1)
    )

    canvas.create_text(
        57.0,
        438.0,
        anchor="nw",
        text="Analysis Face !",
        fill="#000000",
        font=("Inter ExtraBold", 40 * -1)
    )

    canvas.create_text(
        450.0,
        185.0,
        anchor="nw",
        text="Options ....",
        fill="#000000",
        font=("Inter ExtraBold", 40 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        184.0,
        270.0,
        image=image_image_1
    )
    window.resizable(False, False)
    window.mainloop()
if __name__ == "__main__":
    main()