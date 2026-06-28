# -*- coding: utf-8 -*-
import os

file_path = r"D:\StudyJapanese\1_N2_Study_Strategy_and_Grammar.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Normalize line endings to LF
content_normalized = content.replace("\r\n", "\n")

# 1. Update Table of Contents
old_toc_line = "  - [40. 🔴 N2 核心辨析：上に vs 上で vs 上は vs の上では（加上去 vs 做好再做/在……方面 vs 既然……就 vs 表面文獻上）](#40-n2-核心辨析上に-vs-上で-vs-上は-vs-の上では加上去-vs-做好再做在方面-vs-既然就-vs-表面文獻上)"
new_toc_line = old_toc_line + "\n  - [41. 🔴 N2 核心文法與接續：～による vs ～により / ～によって（名詞修飾型 vs 中頓修飾動詞型）](#41-n2-核心文法與接續による-vs-により-によって名詞修飾型-vs-中頓修飾動詞型)"

if old_toc_line in content_normalized:
    content_normalized = content_normalized.replace(old_toc_line, new_toc_line)
    print("TOC line updated for Section 41.")
else:
    print("Error: TOC line not found in normalized content.")

# 2. Section 41 content
section_41_content = """

---

### <a id="41-n2-核心文法與接續による-vs-により-によって名詞修飾型-vs-中頓修飾動詞型"></a>41. 🔴 N2 核心文法與接續：～による vs ～により / ～によって（名詞修飾型 vs 中頓修飾動詞型）

這兩個句型都源自動詞「依る（yoru - 依據、起因）」，在語意上完全相通（皆可代表：原因、手段、依據、區分）。但它們在**詞性接續（形容詞修飾名詞 vs. 副詞修飾動詞/中頓句）**上有著絕對的差別，這是日檢排列組合與語意選擇的必考細節。

---

### 🔍 1. 核心四大語意（溫故知新）

在討論文法差別前，必須先掌握 `よる` 的四大核心含意：
1.  **原因 / 起因（由於/因為）**：`台風による被害` (由於颱風造成的災情)。
2.  **手段 / 方法（通過/經由/由某人）**：`話し合いによる解決` (通過討論解決) / `漱石によって書かれた` (由漱石所寫)。
3.  **依據 / 根源（根據）**：`天気予報によると` (根據天氣預報，常呼應 ➔ ～そうだ)。
4.  **區分 / 取決於（因……而異）**：`人によって考え方が違う` (想法因人而異)。

---

### 💡 2. 「による」 vs 「により / によって」的文法接續差異

它們的差異純粹是**詞性分工**：

#### 🔴 A. ～による ➔ 【形容詞型：後面必須直接修飾名詞】
*   **文法結構**：**`名詞 A ＋ による ＋ 名詞 B`**
*   **功能**：`による` 是動詞連體形（Dictionary form），在此充當形容詞，用來修飾後方的「名詞 B」。
*   *例句*：
    *   `不注意（名詞A）**による**事故（名詞B）が多発している。`
        (由粗心大意**引起的**事故頻繁發生。➔ `による` 修飾 `事故`)。
    *   `地震**による**被害は甚大だ。`
        (因地震**造成的**災情非常慘重。➔ `による` 修飾 `被害`)。

#### 🔴 B. ～により / ～によって ➔ 【副詞中頓型：後面接動詞或句子】
*   **文法結構**：**`名詞 A ＋ により / によって ＋ 句子/動詞`**
*   **功能**：`により` 是ます形中頓，`によって` 是て形連接。兩者在此充當副詞，修飾後方的動詞，或作為分句的連接。
*   **書面語感**：`により` 偏向嚴謹的書面語；`によって` 則是口語與書面通用的標準型。
*   *例句*：
    *   `台風**により**、電車が運転を見合わせている。`
        (因颱風之故，電車暫停行駛。➔ 修飾後方的句子/動詞 `見合わせている`。)
    *   `インターネット**によって**、世界中の情報がすぐに手に入る。`
        (經由網路，全世界的資訊立刻唾手可得。➔ 修飾動詞 `手に入る`。)
    *   `国**によって**、習慣が異なります。`
        (習慣因國家而異。➔ 修飾動詞 `異なります`。)

---

#### 🌟 專項練習：排列組合星星題 (Scrambled/Star Questions)

*   `大雨に [よる] [土砂崩れで] [★道路が] [通行止めになった]` (因為大雨引起的土石流，道路被禁止通行了。➔ 名詞修飾 `大雨による土砂崩れ`)
*   `話し合いに [より] [問題を] [★無事に] [解決することができた]` (通過談判，成功平安地解決了問題。➔ 修飾動詞 `解決することができた`)
*   `このビルは [有名な] [建築家に] [★よって] [設計された]` (這棟大樓是由著名的建築師所設計的。➔ 被動句行為者 `によって`)
"""

# Strip trailing spaces/newlines and append
content_normalized = content_normalized.rstrip() + section_41_content

# Save with newline="" to prevent duplicate carriage returns on Windows
with open(file_path, "w", newline="", encoding="utf-8") as f:
    f.write(content_normalized.replace("\n", "\r\n"))
print("Section 41 appended successfully.")
