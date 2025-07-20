import tkinter as tk
from tkinter import ttk, messagebox
from subjects import subjects
from tips import tips, tips
import random
import os

class StudyMateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("bAC StudyMate")
        self.root.geometry("800x600")
        
        # État des chapitres (en mémoire)
        self.chapter_status = {}
        
        # Interface
        self.create_widgets()
    
    def vddf ():
        root.configure(root , fg= "green")









    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Section Matières
        ttk.Label(main_frame, text="select a subject:").grid(row=0, column=0, sticky=tk.W)
        
        self.subject_var = tk.StringVar()
        self.subject_menu = ttk.Combobox(main_frame, textvariable=self.subject_var, values=list(subjects.keys()))
        self.subject_menu.grid(row=1, column=0, sticky=tk.EW, pady=5)
        self.subject_menu.bind("<<ComboboxSelected>>", self.load_chapters)
        
        # Frame pour les chapitres
        self.chapters_frame = ttk.LabelFrame(main_frame, text="chapter", padding="10")
        self.chapters_frame.grid(row=2, column=0, sticky=tk.EW, pady=10)
        
        # Section Notes
        ttk.Label(main_frame, text="Notes:").grid(row=0, column=1, sticky=tk.W)
        self.notes_text = tk.Text(main_frame, wrap=tk.WORD, width=40, height=20)
        self.notes_text.grid(row=1, column=1, rowspan=4, padx=10, sticky=tk.NSEW)
        
        scrollbar = ttk.Scrollbar(main_frame, command=self.notes_text.yview)
        scrollbar.grid(row=1, column=2, rowspan=4, sticky=tk.NS)
        self.notes_text.config(yscrollcommand=scrollbar.set)
        
        # Section Conseils
        tips_frame = ttk.LabelFrame(main_frame, text="study advice ", padding="10")
        tips_frame.grid(row=3, column=0, sticky=tk.EW, pady=10)
        
        self.tip_label = ttk.Label(tips_frame, text="", wraplength=300)
        self.tip_label.pack()
        
        ttk.Button(tips_frame, text="random advice", command=self.show_random_tip).pack(pady=5)
        
        # Configuration du redimensionnement
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=2)
        main_frame.rowconfigure(2, weight=1)
        
    def load_chapters(self, event):
        # Efface les chapitres précédents
        for widget in self.chapters_frame.winfo_children():
            widget.destroy()
            
        subject = self.subject_var.get()
        if not subject:
            return
            
        # Charge les notes
        self.load_notes(subject.lower())
        
        # Affiche les chapitres
        for i, chapter in enumerate(subjects[subject]):
            chapter_frame = ttk.Frame(self.chapters_frame)
            chapter_frame.pack(fill=tk.X, pady=2)
            
            ttk.Label(chapter_frame, text=chapter, width=30).pack(side=tk.LEFT)
            
            # Boutons d'état
            status_var = tk.StringVar(value="none")
            self.chapter_status[(subject, chapter)] = status_var
            
            ttk.Radiobutton(chapter_frame, text="done", variable=status_var, value="done" ).pack(side=tk.LEFT, padx=2)
            ttk.Radiobutton(chapter_frame, text="review", variable=status_var, value="review").pack(side=tk.LEFT, padx=2)
            ttk.Radiobutton(chapter_frame, text="hard", variable=status_var, value="hard").pack(side=tk.LEFT, padx=2)
    
    def load_notes(self, subject):
        self.notes_text.delete(1.0, tk.END)
        filename = f"notes/{subject}.txt"
        
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                self.notes_text.insert(tk.END, f.read())
        else:
            self.notes_text.insert(tk.END, f"Aucune note disponible pour {subject.capitalize()}")
    
    def show_random_tip(self):
        tip = random.choice(tips + tips)
        self.tip_label.config(text=tip)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudyMateApp(root)
    root.mainloop()
