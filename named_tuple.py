#This is an example to showcase named tuples

import pandas as pd
from collections import namedtuple

# 1. Define the namedtuple structure
Player = namedtuple('Player', ['name', 'team', 'position', 'age'])

# 2. Create a list of Player instances
player_data = [
    Player(name='Lionel Messi', team='Inter Miami', position='Forward', age=38),
    Player(name='Cristiano Ronaldo', team='Al Nassr', position='Forward', age=40),
    Player(name='Kevin De Bruyne', team='Manchester City', position='Midfielder', age=34)
]

# 3. Create the DataFrame directly from the list
df = pd.DataFrame(player_data)

# 4. Display the DataFrame
print(df)

#------------------------------------------------------2nd Example----------------------------------------------------------------

# Define the structure of our function's return value
TextStats = namedtuple('TextStats', ['word_count', 'char_count', 'num_lines'])

def analyze_text(text):
    """Analyzes a block of text and returns statistics."""
    lines = text.split('\n')
    num_lines = len(lines)
    char_count = len(text)
    word_count = len(text.split())
    return TextStats(word_count=word_count, char_count=char_count, num_lines=num_lines)

# --- Using the function ---
document = "Named tuples are great.\nThey improve code readability."
stats = analyze_text(document)

# Accessing results is explicit and easy to understand
print(f"The document has {stats.word_count} words and {stats.num_lines} lines.")
