# input potencial solution to get potencial solution signature
def get_sentance_signature(line: str): 
    words = line.split()
    result = []
    for word in words:
        result.append(len(word))
    return result 

# input puzzle input to get puzzle signature 
def get_puzzle_signature(line: str): 
    new_line = line.replace("\n"," ") # remove new line
    new_line = line.replace("_ ","_") # remove spaces between
    words = new_line.split()
    result = []
    for word in words:
        result.append(len(word))
    return result 

# take puzzle input and potencial solution, see if thier signatures match, return bool
def compare(solution_test: str, puzzle_input: str):
    puzzle_signature = get_puzzle_signature(puzzle_input)
    solution_test = get_sentance_signature(solution_test)

    if (solution_test == puzzle_signature):
        return True
    return False

# paste the hangman input below
puzzle_input = """_ _ _   _ _ _ _ _   _ _ _   _ _ _ _ _   _ _ _ _ _ _ _   _ _ _ _ _
_ _ _   _ _ _   _ _ _ _   _ _   _ _ _ _ _ _ _ _"""

txt = open("solutions.txt")
for lines in txt:
    if compare(lines, puzzle_input):
        print(lines)