# get GUI with tk + validate natural words with nltk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

import nltk
from nltk.corpus import words
nltk.download("words")

import re

class SpellingChecker:

    def __init__(self):
        # basic GUI
        self.root = tk.Tk()
        self.root.geometry("600x500")
        self.text = ScrolledText(self.root, font=("American Typewriter", 18))

        # when key released check function triggered
        self.text.bind("<KeyRelease>", self.check)
        self.text.pack()

        self.root.mainloop()

    def check(self, event):
        content = self.text.get("1.0", tk.END) # includes full content of text box
        space_count = content.count (" ")      # counts number of white space
        
        self.og_spaces = 0
        if space_count != self.og_spaces:
            self.og_spaces = space_count

            for tag in self.text.tag_names():  
                self.text.tag_delete(tag)

            # re : everything that is not a character(special char) is replaced by nothing 
            # if word not in nltk add a tag (tag position then specified)
            for word in content.split(" "):
                if re.sub(r"[^\w]", "", word.lower()) not in words.words():
                    position = content.find(word)
                    self.text.tag_add(word, f"1.{position}", f"1.{position+ len(word)}")
                    self.text.tag_config(word, foreground="light blue")

SpellingChecker()
