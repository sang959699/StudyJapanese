# -*- coding: utf-8 -*-
import os

file_path = r"D:\StudyJapanese\1_N2_Study_Strategy_and_Grammar.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Normalize line endings to LF
content_normalized = content.replace("\r\n", "\n")

# 1. Update Table of Contents
old_toc_line = "  - [44. 🔴 N2 核心辨析：ことから vs のことだから（由客觀事實/起源導出 vs 了解某人性格做出的推測預料）](#44-n2-核心辨析ことから-vs-のことだから由客觀事實起源導出-vs-了解某人性格做出的推測預料)"
new_toc_line = old_toc_line + "\n  - [45. 🔴 N2 核心文法：～だけましだ（好歹還……/光是……就該慶幸了的妥協語境）](#45-n2-核心文法だけましだ好歹還光是就該慶幸了的妥協語境)"

if old_toc_line in content_normalized:
    content_normalized = content_normalized.replace(old_toc_line, new_toc_line)
    print("TOC line updated for Section 45.")
else:
    print("Error: TOC line not found in normalized content.")

# 2. Section 45 content
section_45_content = """

---

### <a id="45-n2-核心文法だけましだ好歹還光是就該慶幸了的妥協語境"></a>45. 🔴 N2 核心文法：～だけましだ（好歹還……/光是……就該慶幸了的妥協語境）

這個文法在日檢語意與閱讀中極常出現。它核心代表著**「妥協與慶幸」**的情感色彩：雖然目前的處境很不理想，但好歹還有 A 這點好處，比起最糟糕的情況（A 也不存在）已經算是不幸中的大幸了。

> [!NOTE]
> 💡 **這型文法的「底層邏輯與語意」**
> 
> * **核心字義**：**`まし（増し）`** 在日文裡是「更好、更合適、稍微強一點」的意思。
> * **文法本意**：`～だけましだ` ➔ **「光是……這點就已經算是好的了（知足吧/該慶幸了）。」**
> * **語境限制**：前半句通常會先抱怨一個「糟糕的現狀」（如：薪水低、受傷、失敗），後半句則拋出一個「不幸中的大幸」來做心理安慰。
> * *例*：`給料は安いが、仕事がある**だけましだ**。` (雖然薪水很低，但光是還有工作就該慶幸了。➔ 沒有工作會更慘。)

💡 **超直覺秒殺法則**：
* **`～だけましだ`** ➔ **「比上不足，比下有餘的『妥協安慰劑』。」** (好歹還……)

---

### 🔍 語意與接續詳解

*   **接續**：**`動詞・形容詞普通形 / 名詞 + である ＋ だけましだ`**
*   **例句**：
    *   `ボーナスが減ったけれど、もらえる**だけましだ**。` (雖然獎金變少了，但光是拿得到就該慶幸了。➔ 總比沒有好。)
    *   `転んで怪我をしたが、骨折しなかった**だけましだ**。` (摔倒受傷了，但好歹沒骨折，算是不幸中的大幸。)
    *   `今回の家賃は少し高いが、駅から近い**だけましだ**。` (這次的房租雖然有點貴，但好歹離車站近，還算過得去。)
    *   `私の部屋は狭いけれど、個室である**だけましだ**。` (我的房間雖然很窄，但好歹是個獨立的單人房，算不錯了。)

---

#### 🌟 專項練習：排列組合星星題 (Scrambled/Star Questions)

*   `給料が [下がったけれど] [会社を] [★首にならなかった] [だけましだ]` (雖然薪水降了，但好歹沒被公司解雇，已經算慶幸了。➔ 妥協慶幸)
*   `風邪を [ひいてしまったが] [旅行に行く] [★前でなかった] [だけましだ]` (雖然感冒了，但好歹不是在去旅行之前感冒，算是不幸中的大幸。)
*   `文句を [言われながらも] [手伝って] [★もらえる] [だけましだ]` (雖然一邊被抱怨，但好歹人家還願意幫忙，已經該知足了。)
"""

# Strip trailing spaces/newlines and append
content_normalized = content_normalized.rstrip() + section_45_content

# Save with newline="" to prevent duplicate carriage returns on Windows
with open(file_path, "w", newline="", encoding="utf-8") as f:
    f.write(content_normalized.replace("\n", "\r\n"))
print("Section 45 appended successfully.")
