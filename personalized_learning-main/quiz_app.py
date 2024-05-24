import tkinter as tk
from tkinter import messagebox
from recommendation import recommend_path
from database import save_progress

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personalized Learning Path Generator")
        
        self.questions = [
            "What is the capital of France?",
            "What is 2 + 2?",
            "Who wrote 'To Kill a Mockingbird'?"
        ]
        self.options = [
            ["London", "Paris", "Berlin", "Madrid"],
            ["3", "4", "5", "6"],
            ["Harper Lee", "Jane Austen", "J.K. Rowling", "Ernest Hemingway"]
        ]
        self.answers = [1, 1, 0]
        self.user_answers = []
        
        self.question_label = tk.Label(root, text=self.questions[0])
        self.question_label.pack(pady=20)
        
        self.var = tk.IntVar()
        self.options_frame = tk.Frame(root)
        self.options_frame.pack(pady=20)
        self.create_options(0)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

    def create_options(self, q_index):
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        for i, option in enumerate(self.options[q_index]):
            rb = tk.Radiobutton(self.options_frame, text=option, variable=self.var, value=i)
            rb.pack(anchor='w')
    
    def next_question(self):
        self.user_answers.append(self.var.get())
        if len(self.user_answers) == len(self.questions):
            self.show_results()
        else:
            self.question_label.config(text=self.questions[len(self.user_answers)])
            self.create_options(len(self.user_answers))
    
    def show_results(self):
        correct = sum([1 for i in range(len(self.answers)) if self.user_answers[i] == self.answers[i]])
        messagebox.showinfo("Results", f"You got {correct} out of {len(self.questions)} correct!")
        path = recommend_path(self.user_answers)
        save_progress("John Doe", self.user_answers, path[0])
        messagebox.showinfo("Recommended Path", f"Recommended Learning Path: {path[0]}")
