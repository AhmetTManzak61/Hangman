import tkinter as tk
import random

countries = ["france", "germany", "italy", "spain", "japan", "china", "brazil", "canada", "india", "australia",
             "turkey", "argentina", "greece", "usa", "russia", "england", "scotland", "hungary", "iran", "croatia",
             "portugal", "serbia", "slovenia", "egypt", "nigeria", "ghana", "venezuela", "colombia", "cameroon",
             "mexico", "morocco", "poland", "switzerland", "bulgaria", "denmark", "norway", "sweden", "netherlands",
             "kenya", "belgium", "peru"]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack()

        self.word_to_guess = random.choice(countries)  # Change this to a random word from your list

        self.guessed_letters = set()
        self.attempts = 6

        self.display_word = self.get_display_word()
        self.canvas.create_text(200, 200, text=self.display_word, font=("Arial", 24))

        self.input_label = tk.Label(self.root, text="Guess a letter:")
        self.input_label.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.submit_button = tk.Button(self.root, text="Submit", command=self.make_guess)
        self.submit_button.pack()

        self.incorrect_guess_label = tk.Label(self.root, text="")
        self.incorrect_guess_label.pack()

    def get_display_word(self):
        display = ""
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_ "
        return display

    def make_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if guess in self.guessed_letters:
            return  # Don't process repeated guesses

        self.guessed_letters.add(guess)

        if guess not in self.word_to_guess:
            self.attempts -= 1

        self.display_word = self.get_display_word()
        self.canvas.delete("all")
        self.canvas.create_text(200, 200, text=self.display_word, font=("Arial", 24))

        if self.display_word == self.word_to_guess:
            self.game_over("You won! The word was: " + self.word_to_guess)
        elif self.attempts == 0:
            self.game_over("Game over! The word was: " + self.word_to_guess)

        self.incorrect_guess_label.config(text=f"Incorrect Guesses: {' '.join(self.guessed_letters - set(self.word_to_guess))}")





    def game_over(self, message):
        self.submit_button.config(state=tk.DISABLED)
        self.incorrect_guess_label.config(text="")
        self.canvas.delete("all")
        self.canvas.create_text(300, 150, text=message, font=("Arial", 20))

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
