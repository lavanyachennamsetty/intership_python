import pandas as pd 
import matplotlib.pyplot as plt
# Load CSV file 
data = pd.read_csv("data.csv") # Display data 
print("Data:\n", data) # Calculate average marks 
average = data["Marks"].mean() 
print("Average Marks :", average) # Bar chart 
plt.bar(data["Name"], data["Marks"]) 
plt.xlabel("Name")
plt.ylabel("Marks") 
plt.title("Marks of the Students ") 
plt.show()
