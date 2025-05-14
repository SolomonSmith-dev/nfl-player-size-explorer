import pandas as pd
import plotly.express as px
import preswald

df = pd.read_csv('data/Basic_Stats.csv')

# Filter to active players only
df = df[df["Current Status"] == "Active"]

# Keep only relevant columns
columns_to_keep = ["Name", "Position", "Height (inches)", "Weight (lbs)", "Current Team"]
df = df[columns_to_keep]

# Create scatter plot
fig = px.scatter(df,
                 x="Height (inches)",
                 y="Weight (lbs)",
                 color="Position",
                 title="Active Player Height vs Weight",
                 labels={"Height (inches)": "Height", "Weight (lbs)": "Weight"})

fig.update_layout(template="plotly_white")

# Preswald Display
preswald.text("# NFL Player Size Explorer")
preswald.text("Visualizing height and weight of active NFL players by position.")
preswald.plotly(fig)
preswald.table(df)

