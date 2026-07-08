'''Store programming languages and print them exactly in the order they were first added. Ignore duplicates.'''
from typing import List

programming_languages = ["C", "C++", "Java", "Ruby", "Python", "C", "JavaScript", "Ruby"]
sorted_programming_languages = []

for lan in programming_languages:
    if lan not in sorted_programming_languages:
        sorted_programming_languages.append(lan)
print(sorted_programming_languages)
