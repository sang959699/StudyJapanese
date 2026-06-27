# -*- coding: utf-8 -*-
import os

file_path = r"D:\StudyJapanese\1_N2_Study_Strategy_and_Grammar.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Normalize line endings to LF
content_normalized = content.replace("\r\n", "\n")

# 1. Update Table of Contents
old_toc_line = "  - [30. 🔴 N2 核心文法與辨析：～よりほかない vs ～せざるを得ない（只能……之外別無他法 vs 不得不……）](#30-n2-核心文法與辨析よりほかない-vs-せざるを得ない只能之外別無他法-vs-不得不)"
new_toc_line = old_toc_line + "\n  - [31. 🔴 N2 核心文法與語境：～ようでは（如果是這種狀態的話/要是像這樣就完了）](#31-n2-核心文法與語境ようでは如果是這種狀態的話要是像這樣就完了)"

if old_toc_line in content_normalized:
    content_normalized = content_normalized.replace(old_toc_line, new_toc_line)
    print("TOC line updated for Section 31.")
else:
    print("Error: TOC line not found in normalized content.")

# 2. Section 31 content
section_31_content = """

---

### <a id="31-n2-核心文法與語境ようでは如果是這種狀態的話要是像這樣就完了"></a>31. 🔴 N2 核心文法與語境：～ようでは（如果是這種狀態的話/要是像這樣就完了）

這個句型用來表示一種「消極、批判性的假設」。說話者指出對方目前「不及格、糟糕的狀態」，並斷言「如果維持這種狀態，未來絕對得不到好結果」。

> [!NOTE]
> 💡 **這個文法的「底層邏輯與語意」**
> 
> 1. **字面意為「以……的樣子/狀態的話」**：
>    * `よう`（樣子、狀態）+ `では`（條件：如果是這樣的話）。
> 2. **強烈的批評、警告或嘆息**：
>    * 說話者對前方的狀態感到非常無奈或不滿。
>    * 後半句**百分之百接否定、批評或失敗的評估**（例如：だめだ、合格は無理だ、信用されない）。
>    * *視覺濾鏡*：**搖頭嘆氣、嚴厲指責**。
> 3. **與一般條件句 `～たら / ～なら` 的區別**：
>    * `～たら / ～なら` ➔ 中性的假設，後方可接好結果或壞結果。
>    * `～ようでは` ➔ 專門用來假設**「極為不及格、糟糕的現狀」**，且後半句**只能是壞結果**。

💡 **超好記的中文口語對照（記憶鉤子）**：
* **`～ようでは`** ➔ **「如果連這種（不及格的）狀態都持續下去，那未來就完蛋了。」**

📜 **接續與例句**

*   **接續**：**`名詞修飾形（普通形） + ようでは`** (名詞 + であるようでは, な形容詞 + な/であるようでは)
*   **例句**：
    *   `こんな簡単な漢字が書けない**ようでは**、N2合格は無理だ。`
        (如果連這麼簡單的漢字都寫不出來，那想要考過 N2 是不可能的。➔ 批評寫不出漢字的狀態。)
    *   `少しの熱で仕事を休む**ようでは**、社会人として失格だ。`
        (如果稍微發燒就請假不上班，作為社會人是不及格的。➔ 指責工作態度。)
    *   `自分で決めたルールを守れない**ようでは**、誰からも信用されない。`
        (如果連自己決定的規則都守不住，是不會得到任何人的信任的。➔ 警告後果。)

---

#### 🌟 專項練習：排列組合星星題 (Scrambled/Star Questions)

*   `こんな簡単な [問題が] [解けない] [★ようでは] [合格は望めない]` (如果連這麼簡單的問題都解不開，合格是無望的。)
*   `相手の [話を聞かない] [ようでは] [★コミュニケーションは] [成り立たない]` (如果連對方的話都不聽，是無法進行溝通的。)
*   `この程度の [失敗で] [諦める] [★ようでは] [何をやっても成功しない]` (如果因為這種程度的失敗就放棄，那做什麼都不會成功的。)
"""

# Strip trailing spaces/newlines and append
content_normalized = content_normalized.rstrip() + section_31_content

# Save with newline="" to prevent duplicate carriage returns on Windows
with open(file_path, "w", newline="", encoding="utf-8") as f:
    f.write(content_normalized.replace("\n", "\r\n"))
print("Section 31 appended successfully.")
