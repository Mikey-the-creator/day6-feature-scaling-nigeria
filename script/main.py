import numpy as np
import pandas as pd
data = pd.read_csv("../data/nigerian_states.csv")
population = data["Population_Estimate_2022"]
pop = np.array(population)
print(pop)
scaled_population = (pop - pop.min()) / (pop.max() - pop.min())
print(scaled_population)
temperature = data["Average_Temperature_Celsius"]
tem = np.array(temperature)
scaled_temperature = (tem - tem.min()) / (tem.max() - tem.min())
print(scaled_temperature)
data["Scaled_Temperature"] = scaled_temperature
data["Scaled_Population"] = scaled_population
data.to_csv("NIgerian_states_with_Scaled_population_and_temperature", index=False)