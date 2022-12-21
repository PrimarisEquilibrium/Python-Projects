from string import whitespace
import matplotlib.pyplot as plt

class BarChart:

    def __init__(self, document):
        """Assigns the read document to an instance variable."""
        self._document = self.read_document(document)
    
    def __len__(self):
        """Returns the len of the document."""
        return len(self._document)

    def unique_letters(self):
        """Handles the creation of a dictionary containing the frequency of letters."""
        letter_dict = {}
        for i in range(len(self)):
            letter = self._document[i]
            if letter in whitespace: continue

            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
        sorted_letter_dict = reversed(sorted(letter_dict.items(), key=lambda x:x[1])) # Sorts dict
        return dict(sorted_letter_dict)
    
    def read_document(self, file_path):
        """Reads the document from the given file path."""
        try:
            with open(file_path, "r") as f:
                contents = f.read()
                return contents
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
    
    def create_barchart(self):
        """Initializes a barchart"""
        letter_dict = self.unique_letters()
        letters = list(letter_dict.keys())[:10]
        values = list(letter_dict.values())[:10]

        plt.bar(letters, values, color="purple")
        plt.title("Average Frequency of Letters")
        plt.xlabel("Letters")
        plt.ylabel("Number of Letters")
        plt.show()

if __name__ == "__main__":
    document = BarChart("document.txt")
    document.create_barchart()