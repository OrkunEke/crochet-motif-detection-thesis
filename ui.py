import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class UI:
    def __init__(self, root, main_app):
        self.root = root
        self.main_app = main_app

        self.background_image = Image.open('assets/background1.PNG')
        self.background_image = self.background_image.resize(
            (root.winfo_screenwidth(), root.winfo_screenheight()),
            Image.Resampling.LANCZOS
        )
        self.bg_image = ImageTk.PhotoImage(self.background_image)

        self.background_label = tk.Label(root, image=self.bg_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.top_frame = tk.Frame(root, bg='#FEECE0', bd=5)
        self.top_frame.place(relx=0.5, rely=0.1, anchor='n')

        self.btn = self.create_rounded_button(self.top_frame, text="🧶Load Image🧶", command=self.load_image)
        self.btn.pack()

        placeholder_path = 'assets/landscape-placeholder.png'
        placeholder_img = Image.open(placeholder_path)
        placeholder_img = placeholder_img.resize((400, 400))
        self.placeholder_img = ImageTk.PhotoImage(placeholder_img)

        self.panel = tk.Label(self.top_frame, image=self.placeholder_img)
        self.panel.pack(pady=10)
        self.panel.image = self.placeholder_img

        self.result_label = tk.Label(self.top_frame, text="🧵Load your motif to learn how to crochet it!🧵 ", font=("Helvetica", 18), bg='#FEECE0')
        self.result_label.pack(pady=10)

        self.go_button = self.create_rounded_button(root, text="Go to Instructions", command=self.go_to_instructions)
        self.go_button.pack_forget()

        self.instruction_frame = tk.Frame(root, bg='#FEECE0', bd=5)

        self.cancel_button = self.create_rounded_button(self.instruction_frame, text="Cancel",
                                                        command=self.back_to_main)
        self.cancel_button.pack(anchor='nw', padx=0, pady=10)

        self.blueprint_panel = tk.Label(self.instruction_frame)
        self.blueprint_panel.pack()

        self.instruction_label = tk.Label(self.instruction_frame, text="", font=("Helvetica", 14), wraplength=600,
                                          bg='#FEECE0')
        self.instruction_label.pack(pady=10)

        self.prev_button = self.create_rounded_button(self.instruction_frame, text="⪻ Previous Step",
                                                      command=self.previous_page)
        self.next_button = self.create_rounded_button(self.instruction_frame, text="Next Step ⪼", command=self.next_page)

    def create_rounded_button(self, parent, text, command):
        canvas = tk.Canvas(parent, width=150, height=50, bd=0, highlightthickness=0)
        canvas.pack(pady=10)

        radius = 25
        canvas.create_arc((0, 0, radius, radius), start=90, extent=90, fill="#FEBDAD", outline="#FEBDAD")
        canvas.create_arc((150 - radius, 0, 150, radius), start=0, extent=90, fill="#FEBDAD", outline="#FEBDAD")
        canvas.create_arc((0, 50 - radius, radius, 50), start=180, extent=90, fill="#FEBDAD", outline="#FEBDAD")
        canvas.create_arc((150 - radius, 50 - radius, 150, 50), start=270, extent=90, fill="#FEBDAD", outline="#FEBDAD")
        canvas.create_rectangle((radius // 2, 0, 150 - radius // 2, 50), fill="#FEBDAD", outline="#FEBDAD")
        canvas.create_rectangle((0, radius // 2, 150, 50 - radius // 2), fill="#FEBDAD", outline="#FEBDAD")

        button_text = canvas.create_text(75, 25, text=text, font=("Helvetica", 14), fill="black")

        canvas.tag_bind(button_text, "<Button-1>", lambda event: command())
        canvas.tag_bind("all", "<Enter>", lambda event: canvas.itemconfig(button_text, fill="white"))
        canvas.tag_bind("all", "<Leave>", lambda event: canvas.itemconfig(button_text, fill="black"))

        return canvas

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = Image.open(file_path)
            img = img.resize((400, 400))
            img = self.main_app.round_corners(img, 10)
            img = ImageTk.PhotoImage(img)
            self.panel.config(image=img)
            self.panel.image = img
            self.main_app.predict(file_path)

    def go_to_instructions(self):
        self.top_frame.place_forget()
        self.go_button.pack_forget()
        self.instruction_frame.place(relx=0.5, rely=0.1, anchor='n')
        self.main_app.show_instruction(0)

    def back_to_main(self):
        self.instruction_frame.place_forget()
        self.top_frame.place(relx=0.5, rely=0.1, anchor='n')
        self.go_button.pack_forget()

    def show_instruction(self, page):
        self.main_app.show_instruction(page)

    def next_page(self):
        self.main_app.next_page()

    def previous_page(self):
        self.main_app.previous_page()

    def round_button(self, button):
        button.config(
            relief="flat",
            borderwidth=2,
            highlightthickness=0,
            bg="#FEBDAD",
            fg="black",
            activebackground="#FEBDAD",
            activeforeground="black"
        )
        button.bind("<Enter>", lambda e: e.widget.config(bg="#FEECE0"))
        button.bind("<Leave>", lambda e: e.widget.config(bg="#FEBDAD"))

