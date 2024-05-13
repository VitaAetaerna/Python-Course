import pandas
import pandas as pd


dataset = {
    "Name": ["Thomas", "Patrick"],
    "Nachname": ["A", "T"],
    "Jahr": ["2024", "2024"],
}


dataset_panda = pandas.DataFrame(dataset)
print(dataset_panda)