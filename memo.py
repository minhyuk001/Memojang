from tkinter import *
from tkinter import filedialog

root = Tk()

root.title("메모장")

root.geometry("1000x800")

text_area = Text(root, font=("Helvetica", 12))
text_area.pack(fill=BOTH, expand=1)

def open_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, "r") as file:
        content = file.read()
        text_area.delete("1.0", END)
        text_area.insert(END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    content = text_area.get("1.0", END)
    with open(file_path, "w") as file:
        file.write(content)

menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="열기(O)", command=open_file)
file_menu.add_command(label="저장(S)", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="끝내기(X)", command=root.quit)
menu_bar.add_cascade(label="파일(F)", menu=file_menu)


root.config(menu=menu_bar)

root.mainloop()

