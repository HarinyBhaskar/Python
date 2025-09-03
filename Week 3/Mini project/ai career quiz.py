import tkinter as tk
from tkinter import messagebox, ttk
import json
import logging
from datetime import datetime
import random
import csv

# ----------------- Logging -----------------
logging.basicConfig(filename="quiz_log.txt",
                    level=logging.INFO,
                    format="%(asctime)s - %(message)s")

def log_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        logging.info(f"{func.__name__} executed in {end - start}")
        return result
    return wrapper

def validate_input(func):
    def wrapper(self, *args, **kwargs):
        if not self.name_var.get().strip() or not self.domain_var.get():
            messagebox.showerror("Error", "Please enter your name and select a domain!")
            return
        return func(self, *args, **kwargs)
    return wrapper

# ----------------- Load Quiz Data from CSV -----------------
def load_questions_from_csv(filename="questions_full.csv"):
    quiz_data = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                domain = row["domain"]
                question = row["question"]
                options = [row["option1"], row["option2"], row["option3"], row["option4"]]
                answer = row["answer"]

                if domain not in quiz_data:
                    quiz_data[domain] = []
                quiz_data[domain].append((question, options, answer))
    except Exception as e:
        logging.error(f"Error loading CSV: {e}")
        messagebox.showerror("Error", f"Failed to load questions from {filename}")
    return quiz_data

QUIZ_DATA = load_questions_from_csv()

# ----------------- Classes -----------------
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self):
        self.score += 1

    def to_dict(self):
        return {"name": self.name, "score": self.score}


class Leaderboard:
    def __init__(self, filename="scores.json"):
        self.filename = filename

    def load_scores(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except:
            return []

    def save_score(self, player: Player):
        data = self.load_scores()
        data.append(player.to_dict())
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def get_top_scores(self, n=5):
        data = self.load_scores()
        return sorted(data, key=lambda x: x["score"], reverse=True)[:n]


class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 AI Career Quiz Game 🎯")
        self.root.geometry("900x600")
        self.root.configure(bg="#f3e6f9")  # Mild purple

        self.player = None
        self.questions = []
        self.current_q = 0

        self.name_var = tk.StringVar()
        self.domain_var = tk.StringVar(value="")

        self.leaderboard = Leaderboard()
        self.setup_start_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def setup_start_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Welcome to AI Career Quiz 🎓",
                 font=("Arial", 24, "bold"), bg="#f3e6f9", fg="#2c3e50").pack(pady=20)

        tk.Label(self.root, text="Enter your name:", font=("Arial", 14),
                 bg="#f3e6f9").pack(pady=10)
        tk.Entry(self.root, textvariable=self.name_var,
                 font=("Arial", 14), width=30).pack(pady=5)

        tk.Label(self.root, text="Select Domain:", font=("Arial", 14),
                 bg="#f3e6f9").pack(pady=10)

        for domain in QUIZ_DATA.keys():
            tk.Radiobutton(self.root, text=domain, variable=self.domain_var,
                           value=domain, font=("Arial", 13),
                           bg="#f3e6f9").pack(anchor="center")

        tk.Button(self.root, text="Start Quiz 🚀",
                  font=("Arial", 14, "bold"), bg="#9b59b6", fg="white",
                  command=self.start_quiz).pack(pady=20)

        tk.Button(self.root, text="View Leaderboard 🏆",
                  font=("Arial", 14, "bold"), bg="#2980b9", fg="white",
                  command=self.show_leaderboard).pack(pady=10)

    @log_time
    @validate_input
    def start_quiz(self):
        name = self.name_var.get().strip()
        domain = self.domain_var.get()

        self.player = Player(name)
        self.questions = random.sample(QUIZ_DATA[domain], len(QUIZ_DATA[domain]))
        self.current_q = 0
        self.show_question()

    def show_progress(self):
        progress = ttk.Progressbar(self.root, length=400, mode="determinate")
        progress["maximum"] = len(self.questions)
        progress["value"] = self.current_q
        progress.pack(pady=10)

    def show_question(self):
        self.clear_screen()

        if self.current_q < len(self.questions):
            q, options, ans = self.questions[self.current_q]

            tk.Label(self.root, text=f"Q{self.current_q+1}: {q}",
                     font=("Arial", 18, "bold"), wraplength=700,
                     bg="#f3e6f9").pack(pady=40)

            self.show_progress()

            random.shuffle(options)
            for option in options:
                btn = tk.Button(self.root, text=option, font=("Arial", 14),
                                width=25, height=2, bg="#3498db", fg="white",
                                command=lambda opt=option: self.check_answer(opt, ans))
                btn.pack(pady=10)
        else:
            self.show_result()

    def check_answer(self, selected, correct):
        if selected == correct:
            self.player.add_score()
            messagebox.showinfo("Correct ✅", "🎉 Well done!")
        else:
            messagebox.showerror("Wrong ❌", f"Correct answer was: {correct}")

        self.current_q += 1
        self.show_question()

    def show_result(self):
        self.clear_screen()

        tk.Label(self.root, text=f"Quiz Completed 🎯\n\nName: {self.player.name}\nScore: {self.player.score}",
                 font=("Arial", 20, "bold"), bg="#f3e6f9", fg="#2c3e50").pack(pady=50)

        self.leaderboard.save_score(self.player)

        tk.Button(self.root, text="Play Again 🔄", font=("Arial", 14, "bold"),
                  bg="#27ae60", fg="white", command=self.setup_start_screen).pack(pady=20)

        tk.Button(self.root, text="View Leaderboard 🏆", font=("Arial", 14, "bold"),
                  bg="#2980b9", fg="white", command=self.show_leaderboard).pack(pady=10)

        logging.info(f"Player: {self.player.name}, Score: {self.player.score}")

    def show_leaderboard(self):
        self.clear_screen()

        tk.Label(self.root, text="🏆 Leaderboard 🏆",
                 font=("Arial", 22, "bold"), bg="#f3e6f9", fg="#2c3e50").pack(pady=20)

        scores = self.leaderboard.get_top_scores()

        if not scores:
            tk.Label(self.root, text="No scores yet!", font=("Arial", 16),
                     bg="#f3e6f9", fg="#34495e").pack(pady=10)
        else:
            for i, entry in enumerate(scores, 1):
                tk.Label(self.root, text=f"{i}. {entry['name']} - {entry['score']}",
                         font=("Arial", 16), bg="#f3e6f9", fg="#34495e").pack(pady=5)

        tk.Button(self.root, text="Back to Menu", font=("Arial", 14, "bold"),
                  bg="#2980b9", fg="white", command=self.setup_start_screen).pack(pady=20)


# ----------------- Run -----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
