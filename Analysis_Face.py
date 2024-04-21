import os
import cv2
import ctypes
from deepface import DeepFace
from PIL import Image, ImageTk
from tkinter import Button
from tkinter import filedialog

def get_screen_resolution():
    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def resize_and_display_image(img_path, canvas):
    # Đọc ảnh từ đường dẫn được chọn
    img = Image.open(img_path)
     # Chỉnh sửa kích thước ảnh nếu cần
    max_width = canvas.winfo_width()
    max_height = canvas.winfo_height()
    if img.width > max_width or img.height > max_height:
        img = img.resize((img.width // 10, img.height // 10))
    # Chuyển đổi ảnh thành định dạng phù hợp để hiển thị trên canvas
    # Chuyển đổi ảnh thành định dạng phù hợp để hiển thị trên canvas
    img = ImageTk.PhotoImage(img)
    # Hiển thị ảnh trên canvas
    canvas.create_image(0, 0, anchor='nw', image=img)
    canvas.update()

def frame_face(frame, age, gender, race, emotion):
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = f"Age: {age}, Gender: {gender}, Race: {race}, Emotion: {emotion}"
    text_lines = text.split(", ")
    text_x = 10
    text_y = 0
    
    for i, line in enumerate(text_lines):
        cv2.putText(frame, line, (text_x, text_y + (i+1) * 30), font, 0.5, (0, 255, 255), 1, cv2.LINE_AA)
    
    return frame

def analyze_face(img_path, canvas):

    objs = DeepFace.analyze(img_path, actions=['age', 'gender', 'race', 'emotion'])
    
    # Tạo một biến để theo dõi vị trí y cho mỗi dòng văn bản
    y_position = 20
    
    for obj in objs:
        age = obj["age"]
        gender = obj["dominant_gender"]
        race = obj["dominant_race"]
        emotion = obj["dominant_emotion"]

        # Hiển thị thông tin khuôn mặt trên canvas_text, mỗi thông tin một dòng dọc xuống
        text = f"INFORMATION "
        canvas.create_text(
            20, y_position,
            anchor="nw",
            text=text,
            fill="#FFFFFF", 
            font=("Inter SemiBold", 16)
        )
        text = f"\nAge: {age}\nGender: {gender}\nRace: {race}\nEmotion: {emotion}"
        canvas.create_text(
            25, y_position,
            anchor="nw",
            text=text,
            fill="#FFFF00",  # Màu vàng
            font=("Inter SemiBold", 14)
        )
        # Đọc và hiển thị hình ảnh khuôn mặt trên canvas_image
        frame = cv2.imread(img_path)
        frame = frame_face(frame, age, gender, race, emotion)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=img)
        canvas.create_image(0, y_position, anchor='nw', image=img)
        canvas.update()
      
    

def capture_face(canvas, window):
    canvas.delete("all")
    cap = cv2.VideoCapture(0)
    img_path = "captured_face.jpg"

    def save_and_analyze_frame():
        ret, frame = cap.read()
        cv2.imwrite(img_path, frame)
        print("Face captured and saved as", img_path)
        cap.release()
        cv2.destroyAllWindows()
        analyze_face(img_path, canvas)

    # Tạo nút "Chụp ảnh" và gán hàm callback
    capture_button = Button(window, text="Take a picture", command=save_and_analyze_frame)
    capture_button.place(x=420.0, y=555.0, width=135.0, height=40.0)

    # Start capturing
    while True:
        ret, frame = cap.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(image=img)
        canvas.create_image(0, 0, anchor='nw', image=img)
        canvas.update()
    
        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
  

def capture_and_analyze_face_from_file(canvas):
    canvas.delete("all")
    # Chọn tệp ảnh từ cửa sổ mở tệp
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    
    if img_path:
        # Đọc và hiển thị ảnh trên canvas
        resize_and_display_image(img_path, canvas)
        # Phân tích khuôn mặt
        analyze_face(img_path, canvas)
    else:
        print("No image file selected.")
