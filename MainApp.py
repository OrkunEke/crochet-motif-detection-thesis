import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import tensorflow as tf
import numpy as np
from tensorflow.keras.utils import load_img, img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input
from instructions import Instructions
from ui import UI


class MainApp:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)
        self.class_indices = {'Harlequin Stitch': 0, 'alpine crochet': 1, 'basket weave crochet stitch': 2,
                              'feather stitch': 3, 'herringbone crochet': 4, 'jasmine crochet': 5, 'moss crochet': 6,
                              'shell crochet': 7, 'star stitch': 8, 'waffle stitch': 9}
        self.class_indices = {v: k for k, v in self.class_indices.items()}

        self.current_page = 0
        self.current_instructions = []

        self.instructions = Instructions()

    def predict(self, file_path):
        img = load_img(file_path, target_size=(224, 224))
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        predictions = self.model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)[0]
        predicted_label = self.class_indices[predicted_class]
        ui.result_label.config(text=f"Assumed type of crochet motif: {predicted_label}")
        self.current_instructions = self.instructions.get_instructions(predicted_label)
        ui.go_button.pack(pady=10)

    def round_corners(self, image, radius):
        mask = Image.new('L', image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle([0, 0, image.size[0], image.size[1]], radius, fill=255)
        rounded_image = Image.new('RGBA', image.size)
        rounded_image.paste(image, (0, 0), mask)
        return rounded_image

    def show_instruction(self, page):
        self.current_page = page
        instruction = self.current_instructions[page]
        blueprint_path = instruction["image"]
        blueprint_img = Image.open(blueprint_path)
        blueprint_img = blueprint_img.resize((400, 400))
        blueprint_img = self.round_corners(blueprint_img, 10)
        blueprint_img = ImageTk.PhotoImage(blueprint_img)
        ui.blueprint_panel.config(image=blueprint_img)
        ui.blueprint_panel.image = blueprint_img
        ui.instruction_label.config(text=instruction["text"])

        if self.current_page == 0:
            ui.prev_button.pack_forget()
        else:
            ui.prev_button.pack(side=tk.LEFT, padx=10)

        if self.current_page == len(self.current_instructions) - 1:
            ui.next_button.pack_forget()
        else:
            ui.next_button.pack(side=tk.RIGHT, padx=10)

    def next_page(self):
        if self.current_page < len(self.current_instructions) - 1:
            self.show_instruction(self.current_page + 1)

    def previous_page(self):
        if self.current_page > 0:
            self.show_instruction(self.current_page - 1)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Crochet Motif Detection")
    root.geometry("800x650")

    main_app = MainApp(model_path='modelfull.h5')
    ui = UI(root, main_app)

    root.mainloop()