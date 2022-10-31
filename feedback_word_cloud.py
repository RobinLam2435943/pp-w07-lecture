# Word cloud of mid-semester feedback responses.

# 1. Read the data
# 2. Make 4 large strings (4 word clouds, 1 for each response)
# 3. Make the 4 word clouds, and display them

# Read the data
with open('data/mid_semester_feedback.csv', 'r') as f:
    contents = f.readlines()

# print(contents[6].split(',')[1])
# print(contents)
# print(contents[77])

# Remove the blank lines
contents = [i for i in contents if i != '\n']

# Clean the data:
# sort out entries which have more than 4 commas and treat them separately.

# First response: lecture/course materials positives
# Make a list of all responses to the first question
lect_pos = []
for i in range(1, len(contents)):
    all_answers = contents[i].split(',')
    if len(all_answers) >= 4:
        lect_pos.append(all_answers[1])

# Get rid of the empty answers.
lect_pos = [i for i in lect_pos if i != '-']
# print(lect_pos)

# Combine answers back into one big string
lect_pos_all = ' '.join(lect_pos)
# print(lect_pos_all)

# my_string = 'aaa'
# my_list = ['A', 'B', 'C']
# print(' IS FOLLOWED BY '.join(my_list))

# Create the word cloud
# Adapted from: https://amueller.github.io/word_cloud/auto_examples/simple.html#sphx-glr-auto-examples-simple-py
from wordcloud import WordCloud

wc_lect_pos = WordCloud(background_color="white").generate(lect_pos_all)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.imshow(wc_lect_pos, interpolation='bilinear')
ax.axis("off")
plt.show()