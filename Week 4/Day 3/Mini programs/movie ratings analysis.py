import numpy as np
import pandas as pd

movies = ["Movie1", "Movie2", "Movie3", "Movie4"]
ratings = np.random.randint(1, 6, size=(4, 3))  # Ratings 1–5

df = pd.DataFrame(ratings, columns=["User1", "User2", "User3"], index=movies)
df["Avg_Rating"] = np.mean(ratings, axis=1)

print(df)
