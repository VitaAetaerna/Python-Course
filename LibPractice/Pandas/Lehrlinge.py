import pandas
import pandas as pd


dataset = {
    "Name": ["Leon", "Lukas", "Andraz", "Alex", "Jakob"],
    "Nachname": ["S", "T", "R", "W", "W"],
    "Gruppe": ["R", "S", "S", "R", "S"],
    "Lehrjahr": ["2", "1", "1", "2", "1"]
}


dataset_panda = pandas.DataFrame(dataset)
print(dataset_panda)