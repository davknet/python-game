hangman_stages = [
    r"""
       +----+
       |   ||
           ||
           ||
           ||
           ||
    =========
    """,
    r"""
       +----+
       |   ||
       O   ||
           ||
           ||
           ||
    =========
    """,
    r"""
       +----+
       |   ||
       O   ||
       |   ||
           ||
           ||
    =========
    """,
    r"""
       +----+
       |   ||
       O   ||
      /|   ||
           ||
           ||
    =========
    """,
    r"""
       +----+
       |   ||
       O   ||
      /|\  ||
           ||
           ||
    =========
    """,
    r"""
       +----+
       |   ||
       O   ||
      /|\  ||
      /    ||
           ||
    =========
    """,
    r"""
       +----+
       |   ||
       O   ||
      /|\  ||
      / \  ||
           ||
    =========
    """
]

def print_hangman(mistakes):
    print( hangman_stages[mistakes])


def main():
   
   for i in range(len(hangman_stages)):
        print(f"Mistakes: {i}")
        print_hangman(i)
        print("\n")

if __name__ == "__main__":
    main()
    