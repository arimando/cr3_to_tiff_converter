import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter.ttk import Progressbar
import rawpy
import imageio
from threading import Thread
import locale

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title(self.get_text("CR3 to TIFF Converter"))

        self.input_dir = ""
        self.output_dir = ""

        self.create_widgets()

    def get_text(self, english, italian=None):
        lang = locale.getdefaultlocale()[0]
        if lang and lang.startswith("it"):
            return italian if italian else english
        return english

    def create_widgets(self):
        self.input_label = tk.Label(self.root, text=self.get_text("Input Folder:", "Cartella di Input:"))
        self.input_label.grid(row=0, column=0, padx=10, pady=5, sticky='e')

        self.input_entry = tk.Entry(self.root, width=50)
        self.input_entry.grid(row=0, column=1, padx=10, pady=5)

        self.input_button = tk.Button(self.root, text=self.get_text("Browse...", "Sfoglia..."), command=self.browse_input)
        self.input_button.grid(row=0, column=2, padx=10, pady=5)

        self.output_label = tk.Label(self.root, text=self.get_text("Output Folder:", "Cartella di Output:"))
        self.output_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')

        self.output_entry = tk.Entry(self.root, width=50)
        self.output_entry.grid(row=1, column=1, padx=10, pady=5)

        self.output_button = tk.Button(self.root, text=self.get_text("Browse...", "Sfoglia..."), command=self.browse_output)
        self.output_button.grid(row=1, column=2, padx=10, pady=5)

        self.convert_button = tk.Button(self.root, text=self.get_text("Start Conversion", "Inizia Conversione"), command=self.start_conversion)
        self.convert_button.grid(row=2, column=1, padx=10, pady=20)

        self.info_button = tk.Button(self.root, text="Info", command=self.show_info)
        self.info_button.grid(row=2, column=2, padx=10, pady=20)

        self.progress = Progressbar(self.root, orient='horizontal', length=400, mode='determinate')
        self.progress.grid(row=3, column=0, columnspan=3, padx=10, pady=20)

        self.log_text = scrolledtext.ScrolledText(self.root, width=60, height=10, wrap=tk.WORD)
        self.log_text.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    def browse_input(self):
        self.input_dir = filedialog.askdirectory()
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, self.input_dir)

    def browse_output(self):
        self.output_dir = filedialog.askdirectory()
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, self.output_dir)

    def log(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)

    def start_conversion(self):
        self.input_dir = self.input_entry.get()
        self.output_dir = self.output_entry.get()

        if not os.path.exists(self.input_dir):
            messagebox.showerror(self.get_text("Error", "Errore"), self.get_text(f"Input directory '{self.input_dir}' does not exist.", f"La cartella di input '{self.input_dir}' non esiste."))
            return

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        cr3_files = [f for f in os.listdir(self.input_dir) if f.lower().endswith('.cr3')]
        if not cr3_files:
            messagebox.showerror(self.get_text("Error", "Errore"), self.get_text(f"No CR3 files found in the input directory '{self.input_dir}'.", f"Nessun file CR3 trovato nella cartella di input '{self.input_dir}'."))
            return

        self.progress["value"] = 0
        self.progress["maximum"] = len(cr3_files)

        self.log_text.delete(1.0, tk.END)  # Clear previous log

        # Run the conversion in a separate thread to avoid freezing the GUI
        conversion_thread = Thread(target=self.convert_files, args=(cr3_files,))
        conversion_thread.start()

    def convert_files(self, cr3_files):
        for index, filename in enumerate(cr3_files):
            cr3_path = os.path.join(self.input_dir, filename)
            tiff_filename = os.path.splitext(filename)[0] + '.tiff'
            tiff_path = os.path.join(self.output_dir, tiff_filename)

            try:
                # Load the CR3 file
                with rawpy.imread(cr3_path) as raw:
                    # Convert to a numpy array
                    rgb_image = raw.postprocess()

                # Save the image as TIFF
                imageio.imsave(tiff_path, rgb_image)
                self.log(self.get_text(f"Successfully converted {filename} to {tiff_filename}.", f"Convertito con successo {filename} in {tiff_filename}."))
            except Exception as e:
                self.log(self.get_text(f"An error occurred while converting {filename}: {e}", f"Si è verificato un errore durante la conversione di {filename}: {e}"))

            self.progress["value"] += 1
            self.root.update_idletasks()

        messagebox.showinfo(self.get_text("Info", "Informazione"), self.get_text("All files have been successfully converted.", "Tutti i file sono stati convertiti con successo."))

    def show_info(self):
        messagebox.showinfo("Info", "Created by F. Federico with the help of AI")

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = ConverterApp(root)
        root.mainloop()
    except Exception as e:
        with open("error_log.txt", "w") as f:
            f.write(str(e))
        messagebox.showerror("Error", "An unexpected error occurred. Please check the error_log.txt file for more details.")
