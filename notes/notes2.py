import pandas as pd 
data = {"name": ["sally", "dave", "john"], "age": [50,35,40]}
df = pd.DataFrame(data) 
print(df) 
print(df.query('age>35'))