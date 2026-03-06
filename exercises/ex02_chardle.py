"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730868127"

def input_word() -> str: #Forgot to add colon after function definition. Code did not run properly, adding colon is very important. 
    """Ask user to enter a five letter word"""
    word: str = input("Enter a 5-character word: ") #Make sure there is a space after the colon in the printed string for better readability. 
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()   
    return word
def input_letter() -> str:
    """Ask the user to input one letter"""
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter
   
def contains_char() -> None:
  """Check to see if the input character matches with any characters in the input word"""
  word: str = input_word()
  letter: str = input_letter()      
  print(f"Searching for {letter} in {word}") #Tried just using print, but that was very inefficient. Using fstring allowed me to print the string much more efficiently. 

  count: int = 0
  # Make sure indentation is correct otherwise code will not run correctly. There was incorrect nested code. 
  if word[0] == letter: #start at 0 as indexing starts at 0
        print(f"{letter} found at index 0")
        count += 1
  
  if word[1] == letter:
        print(f"{letter} found at index 1")
        count += 1


  if word[2] == letter:
        print(f"{letter} found at index 2")
        count += 1 

  if word[3] == letter:
        print(f"{letter} found at index 3")
        count += 1


  if word[4] == letter:
        print(f"{letter} found at index 4")
        count += 1


  if count == 0: #PRacticing using fstrings again to make code more efficient. 
       print(f"No instances of {letter} found in {word}")

  elif count == 1: #Using elif because there is more than one mutually exclusive condition.
       print(f"1 instance of {letter} found in {word}")

  else:
       print(f"{count} instances of {letter} found in {word}")

def main() -> None:
   """Entry point of the Chardle game"""
   contains_char()

if __name__ == "__main__": #Last two lines of code. 
    main()