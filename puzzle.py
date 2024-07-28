from logic import *


# Define symbols representing whether A, B, and C are knights or knaves
AKnight = Symbol("A is a Knight")
AKnave  = Symbol("A is a Knave")
BKnight = Symbol("B is a Knight")
BKnave  = Symbol("B is a Knave")
CKnight = Symbol("C is a Knight")
CKnave  = Symbol("C is a Knave")


# Create a base knowledge structure with what we know for sure:
knowledge_base = And(
    # Each character is either a knight or a knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    # No character can be both a knight and a knave simultaneously
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
)


# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    knowledge_base,
    # A's statement is a contradiction: A cannot be both a knight and a knave
    Biconditional(AKnight, And(AKnight, AKnave))
)


# Puzzle 1
# A says "We are both knaves." B says nothing.
knowledge1 = And(
    knowledge_base,
    # If A is a knight, then both A and B must be knaves
    Implication(AKnight, And(AKnave, BKnave)),
    # If A is a knave, then A's statement is false, so it is not true that both are knaves
    Implication(AKnave, Not(And(AKnave, BKnave))),
)

# Puzzle 2
# A says "We are the same kind." B says "We are of different kinds."
knowledge2 = And(
    knowledge_base,
    # If A is a knight, A and B are either both knights or both knaves
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # If A is a knave, A and B are of different kinds
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    # If B is a knight, A and B are of different kinds
    Implication(BKnight, Or(And(BKnight, AKnave), And(BKnave, AKnight))),
    # If B is a knave, A and B are not of different kinds
    Implication(BKnave, Not(Or(And(BKnight, AKnave), And(BKnave, AKnight)))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but we don't know which.
# B says "A said 'I am a knave.'" B says "C is a knave." C says "A is a knight."
knowledge3 = And(
    knowledge_base,
    # A says either "I am a knight" or "I am a knave"
    Or(AKnight, AKnave),
    # B's first statement: "A said 'I am a knave.'"
    # If B is a knight, then B's statement must be true
    Biconditional(BKnight, Not(AKnight)),
    # B's second statement: "C is a knave."
    Biconditional(BKnight, Not(CKnight)),
    # C's statement: "A is a knight."
    # If C is a knight, then C's statement must be true
    Implication(Or(CKnight, CKnave), Not(AKnave)),
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")

if __name__ == "__main__":
    main()
