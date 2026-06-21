# -*- coding: utf-8 -*-
import os
import re

file_path = r"D:\StudyJapanese\1_N2_Study_Strategy_and_Grammar.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Normalize to LF first
content_lf = content.replace("\r\n", "\n")

# Compress 3 or more consecutive newlines to exactly 2 newlines (which is 1 blank line)
# In markdown, 1 blank line is the standard spacing.
content_compressed = re.sub(r'\n{3,}', '\n\n', content_lf)

# Save with newline="" to prevent duplicate carriage returns on Windows
with open(file_path, "w", newline="", encoding="utf-8") as f:
    f.write(content_compressed.replace("\n", "\r\n"))

print("Consecutive blank lines compressed successfully!")
