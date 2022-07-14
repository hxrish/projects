from Movies_library import fantastic, harry_potter, story
import random
if __name__ == "__main__":
    m = random.choice([harry_potter, fantastic, story])
    m.library()