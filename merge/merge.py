import glob2
from datetime import datetime

def merge():
    files = glob2.glob("*.txt")
    print(files)
    filename = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt"
    with open(filename, "w") as myfile:
      for document in files:
        with open(document, "r") as content:
          myfile.write(content.read() + "\n")



merge()

