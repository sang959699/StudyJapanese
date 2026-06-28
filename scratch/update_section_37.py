# -*- coding: utf-8 -*-
import os

file_path = r"D:\StudyJapanese\1_N2_Study_Strategy_and_Grammar.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Normalize line endings to LF
content_normalized = content.replace("\r\n", "\n")

# 1. Update Table of Contents
old_toc_line = "  - [37. 🔴 N2 核心辨析：～に反して vs ～反面（與預測期待相反 vs 同一事物的正反兩面性）](#37-n2-核心辨析に反して-vs-反面與預測期待相反-vs-同一事物的正反兩面性)"
new_toc_line = "  - [37. 🔴 N2 核心辨析：～に反して vs ～反面 vs ～一方で（與預測相反 vs 同一事物兩面性 vs 兩主體對比或平行狀態）](#37-n2-核心辨析に反して-vs-反面與預測期待相反-vs-同一事物的正反兩面性)"

if old_toc_line in content_normalized:
    content_normalized = content_normalized.replace(old_toc_line, new_toc_line)
    print("TOC line updated for Section 37.")
else:
    print("Warning: TOC line not found in normalized content.")

# 2. Update Section 37 Body
old_section_header = "### <a id=\"37-n2-核心辨析に反して-vs-反面與預測期待相反-vs-同一事物的正反兩面性\"></a>37. 🔴 N2 核心辨析：～に反して vs ～反面（與預測期待相反 vs 同一事物的正反兩面性）"

new_section_content = """### <a id="37-n2-核心辨析に反して-vs-反面與預測期待相反-vs-同一事物的正反兩面性"></a>37. 🔴 N2 核心辨析：～に反して vs ～反面 vs ～一方で（與預測相反 vs 同一事物兩面性 vs 兩主體對比或平行狀態）

這三個句型都包含「相反、反面、另一面」的概念，但它們在**對比的對象（與外部指標相反 vs. 同一主體內部一好一壞 vs. 兩個不同主體或平行狀態對比）**上有著截然不同的文法限制。

> [!NOTE]
> 💡 **這三個文法的「底層邏輯與語意差異」**
> 
> 1. **`～に反して`（與預期/規則相違背：與……相反）**：
>    * **邏輯**：結果與先前的**預測、期待、意圖或法規**完全相反或相違背。
>    * **特徵**：通常接在名詞後（如：予想に反して、期待に反して）。
> 2. **`～反面`（同一主體的一好一壞：另一方面 / 相反地）**：
>    * **邏輯**：指**同一個主體**，同時具備「正面（好處）」與「反面（壞處）」兩種對立的特質。
> 3. **`～一方で`（多主體對比或平行狀態：一方面……另一方面……）**：
>    * **邏輯**：除了可以用於同一個主體的正反面外，還具備兩個 `反面` 所沒有的獨特考點：
>      * **獨特考點一：可以對比「兩個不同的主體」**（例如：哥哥很外向，相反地弟弟很內向。➔ 不能用 `反面`）。
>      * **獨特考點二：可以並列「兩個不對立的平行角色/行為」**（例如：他同時是社長，也是作家。➔ 不能用 `反面`）。

💡 **超直覺秒殺法則**：
* **`～に反して`** ➔ **「結果跟先前的『預期/期待』唱反調。」**
* **`～反面`** ➔ **「同一個硬幣的正反兩面（一好一壞對立）。」**
* **`～一方で`** ➔ **「兩個不同人事物的對比」** 或 **「同時並存的平行角色/狀態」**。

---

### 🔍 語意與接續詳解

#### 💡 1. ～に反して ➔ 【與預測/期待相反（違背）】
*   **接續**：**`名詞 ＋ に反して`**
*   **例句**：
    *   `親の期待**に反して**、彼は大学に進学せず就職した。` (與父母的期待相反，他沒有升學而是去工作了。)

#### 💡 2. ～反面 ➔ 【同主體的一好一壞（正反兩面）】
*   **接續**：**`動詞・形容詞普通形 ＋ 反面`** (名詞 ＋ である反面 / な形 ＋ な・である反面)
*   **例句**：
    *   `一人暮らしは自由な**反面**、寂しさを感じることもある。` (獨居很自由，但另一方面，有時也會感到寂寞。➔ 同一個主體「獨自生活」的正反面。)

#### 💡 3. ～一方で ➔ 【對比不同主體 / 平行不對立狀態】
*   **接續**：**`動詞・形容詞普通形 ＋ 一方で`** (名詞 ＋ である一方で / な形 ＋ な・引である一方で)
*   **例句**：
    *   `兄が社交的である**一方で**、弟は人見知りで大人しい。` (哥哥很社交外向，另一方面，弟弟怕生又內向。➔ 兩個不同主體對比，此處絕對不能用 `反面` ❌。)
    *   `彼は会社を経営する**一方で**、ボランティア活動も行っている。` (他一邊經營公司，另一方面也進行志工活動。➔ 兩個平行不對立的角色，此處絕對不能用 `反面` ❌。)

---

#### 🌟 專項練習：排列組合星星題 (Scrambled/Star Questions)

*   `大方の [予想に] [反して] [★彼は] [選挙で大勝利を収めた]` (與大多數人的預測相反，他在選舉中贏得了大勝。)
*   `このアパートは [家賃が] [安い反面] [★駅から] [遠くて不便だ]` (這間公寓房租便宜，但另一方面，離車站遠很不方便。➔ 同一間公寓的兩面性)
*   `都会の人口が [増える一方で] [地方では] [★過疎化が] [深刻な問題になっている]` (都市人口不斷增加，但另一方面，地方上的過疏化正成為嚴重問題。➔ 兩個不同地區現象對比，不能用 `反面` ❌)
*   `彼は一流の [研究者である] [一方で] [★小説家としての] [才能も発揮している]` (他是一流研究者的同時，也發揮著小說家的才能。➔ 平行不對立角色，不能用 `反面` ❌)"""

if old_section_header in content_normalized:
    # We want to replace everything from old_section_header to the end of the file
    parts = content_normalized.split(old_section_header)
    content_normalized = parts[0] + new_section_content
    print("Section 37 body updated successfully.")
else:
    print("Error: Section 37 header not found in normalized content.")

# Save with newline="" to prevent duplicate carriage returns on Windows
with open(file_path, "w", newline="", encoding="utf-8") as f:
    f.write(content_normalized.replace("\n", "\r\n"))
print("Done.")
