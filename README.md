## Project Title: Knights and Knaves Logic Puzzle Solver

### Project Description

This project involves developing a Python program to solve Knights and Knaves logic puzzles using propositional logic and model-checking algorithms. Inspired by Raymond Smullyan's puzzles, the challenge is to determine the truthfulness of characters (knights always tell the truth, knaves always lie) based on their statements. The project requires encoding logical sentences and leveraging a model-checking algorithm to deduce solutions for given puzzles.

### Background

Knights and Knaves puzzles feature characters who either always tell the truth (knights) or always lie (knaves). The task is to use propositional logic to analyze statements and determine the nature of each character.

### Files and Structure

- `logic.py`: Defines classes for logical connectives and the `model_check` function.
- `puzzle.py`: Contains knowledge bases and propositional symbols for characters A, B, and C.

### Tasks

1. **Puzzle 0**: Single character A says “I am both a knight and a knave.”
2. **Puzzle 1**: Two characters, A and B. A says “We are both knaves.” B says nothing.
3. **Puzzle 2**: Two characters, A and B. A says “We are the same kind.” B says “We are of different kinds.”
4. **Puzzle 3**: Three characters, A, B, and C. 
   - A says either “I am a knight.” or “I am a knave.”, but you don’t know which.
   - B says “A said 'I am a knave.'”
   - B then says “C is a knave.”
   - C says “A is a knight.”

### How to Run

1. Download and unzip the distribution code.
2. Complete the knowledge bases for each puzzle in `puzzle.py`.
3. Run `python puzzle.py` to solve the puzzles.
