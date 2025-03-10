# Wordle - Python Terminal Game 🎮

A short implementation of the popular game **Wordle** in Python. 

## 📌 How It Works
1. The secret **5-letter** word is randomly selected from an English word list.
2. The player has **6 attempts** to guess the correct word.
3. After each attempt, a hint will be displayed in the terminal:
   - 🟩 **Green** → The letter is **correct** and in the **right position**.
   - 🟨 **Yellow** → The letter **exists** in the word but is in the **wrong position**.
   - ⬜ **Grey** → The letter **does not exist** in the word.
   
## ▶️ Running the Game
Run the script in your terminal:
```bash
python main.py
