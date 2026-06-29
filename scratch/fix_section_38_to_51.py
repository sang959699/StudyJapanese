# -*- coding: utf-8 -*-
import os

file_path = r"D:\StudyJapanese\1_N2_Study_Strategy_and_Grammar.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Normalize line endings to LF
content_normalized = content.replace("\r\n", "\n")

# 1. Remove the misplaced Section 38 entry in TOC
old_toc_entry = "  - [38. 🔴 N2 核心辨析與字源：～にかけては vs ～について vs ～に関して（在……方面/最拿手 vs 關於……）](#38-n2-核心辨析與字源にかけては-vs-について-vs-に関して在方面最拿手-vs-關於)\n"
if old_toc_entry in content_normalized:
    content_normalized = content_normalized.replace(old_toc_entry, "")
    print("Removed misplaced Section 38 entry from TOC.")
else:
    # Try without newline
    old_toc_entry_no_nl = "  - [38. 🔴 N2 核心辨析與字源：～にかけては vs ～について vs ～に関して（在……方面/最拿手 vs 關於……）](#38-n2-核心辨析與字源にかけては-vs-について-vs-に関して在方面最拿手-vs-關於)"
    if old_toc_entry_no_nl in content_normalized:
        content_normalized = content_normalized.replace(old_toc_entry_no_nl + "\n", "")
        print("Removed misplaced Section 38 entry from TOC (fallback).")
    else:
        print("Misplaced TOC entry not found.")

# 2. Add Section 51 entry in TOC under Section 50
section_50_toc = "  - [50. 🔴 N2 核心文法：～折には / ～折に（值此之際/……的時候之商務敬語優雅表達）](#50-n2-核心文法折には-vs-折に值此之際的時候之商務敬語優雅表達)"
section_51_toc = section_50_toc + "\n  - [51. 🔴 N2 核心辨析與字源：～にかけては vs ～について vs ～に関して（在……方面/最拿手 vs 關於……）](#51-n2-核心辨析與字源にかけては-vs-について-vs-に関して在方面最拿手-vs-關於)"

if section_50_toc in content_normalized:
    content_normalized = content_normalized.replace(section_50_toc, section_51_toc)
    print("Added Section 51 entry to TOC.")
else:
    print("Section 50 TOC entry not found.")

# 3. Update the heading and anchor tag at the bottom of the file
old_heading = '### <a id="38-n2-核心辨析與字源にかけては-vs-について-vs-に関して在方面最拿手-vs-關於"></a>38. 🔴 N2 核心辨析與字源：～にかけては vs ～について vs ～に関して（在……方面/最拿手 vs 關於……）'
new_heading = '### <a id="51-n2-核心辨析與字源にかけては-vs-について-vs-に関して在方面最拿手-vs-關於"></a>51. 🔴 N2 核心辨析與字源：～にかけては vs ～について vs ～に関して（在……方面/最拿手 vs 關於……）'

if old_heading in content_normalized:
    content_normalized = content_normalized.replace(old_heading, new_heading)
    print("Updated section heading to Section 51 at the bottom.")
else:
    print("Section 38 heading at the bottom not found.")

# Save with CRLF on Windows
with open(file_path, "w", newline="", encoding="utf-8") as f:
    f.write(content_normalized.replace("\n", "\r\n"))
print("File updated successfully.")
