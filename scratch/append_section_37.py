# -*- coding: utf-8 -*-
import os

file_path = r"D:\StudyJapanese\1_N2_Study_Strategy_and_Grammar.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Normalize line endings to LF
content_normalized = content.replace("\r\n", "\n")

# 1. Update Table of Contents
old_toc_line = "  - [36. 🔴 N2 核心辨析：～たとたん vs ～あげく（即時瞬間發生 vs 漫長折騰後的糟糕結果）](#36-n2-核心辨析たとたん-vs-あげく即時瞬間發生-vs-漫長折騰後的糟糕結果)"
new_toc_line = old_toc_line + "\n  - [37. 🔴 N2 核心辨析：～に反して vs ～反面（與預測期待相反 vs 同一事物的正反兩面性）](#37-n2-核心辨析に反して-vs-反面與預測期待相反-vs-同一事物的正反兩面性)"

if old_toc_line in content_normalized:
    content_normalized = content_normalized.replace(old_toc_line, new_toc_line)
    print("TOC line updated for Section 37.")
else:
    print("Error: TOC line not found in normalized content.")

# 2. Section 37 content
section_37_content = """

---

### <a id="37-n2-核心辨析に反して-vs-反面與預測期待相反-vs-同一事物的正反兩面性"></a>37. 🔴 N2 核心辨析：～に反して vs ～反面（與預測期待相反 vs 同一事物的正反兩面性）

這兩個句型在中文裡都會使用到「相反、反面」這類詞，但它們在**對比的對象（與外部指標相反 vs. 同一事物內部的正反面）**上有著截然不同的文法功能。

> [!NOTE]
> 💡 **這兩個文法的「底層邏輯與語意差異」**
> 
> 1. **`～に反して`（與預期/規則相違背：與……相反 / 違反……）**：
>    * **邏輯**：接在表示「預測、期待、規則、意圖」的名詞後面，表示最終結果與這些外部指標**完全相反、或違背了規則**。
>    * **特徵**：常用組合為 `予想に反して` (與預測相反)、`期待に反して` (與期待相反)、`規則に反して` (違反規則)。
>    * *例*：`予想に反して、テストは簡単だった。` (與預測相反，考試很簡單。➔ 結果與先前的預測相反。)
> 2. **`～反面`（同一事物的兩面性：另一方面 / 在……的同時，相反地……）**：
>    * **邏輯**：指**同一個主體/事物**，同時具備「正面（優點/好處）」與「反面（缺點/壞處）」兩種相反的特質。
>    * **特徵**：前後句在進行優缺點的對立呈現。
>    * *例*：`一人暮らしは自由な反面、寂しさを感じることもある。` (獨居很自由，但另一方面，有時也會感到寂寞。➔ 「獨居」這件事同時有自由和寂寞兩面。)

💡 **超直覺秒殺法則**：
* **`～に反して`** ➔ **「結果與『先前的預期/規則』唱反調。」** (違背預測、期待)
* **`～反面`** ➔ **「同一枚硬幣的正反兩面（一好一壞）。」** (優缺點共存)

---

### 🔍 語意與接續詳解

#### 💡 1. ～に反して ➔ 【與預測/期待相反（違背）】
*   **接續**：**`名詞 ＋ に反して`** (亦可做定語修飾名詞：に反する ＋ 名詞)
*   **例句**：
    *   `親の期待**に反して**、彼は大学に進学せず就職した。` (與父母的期待相反，他沒有升學而是去工作了。➔ 違背期待。)
    *   `意図**に反して**、相手を怒らせてしまった。` (與原本的意圖相反，結果惹怒了對方。➔ 違背意圖。)

#### 💡 2. ～反面 ➔ 【事物的一好一壞兩面性（另一面）】
*   **接續**：**`動詞・形容詞普通形 ＋ 反面`** (名詞 ＋ である反面 / な形 ＋ な・である反面)
*   **例句**：
    *   `ネットショッピングは便利な**反面**、買いすぎる危険もある。` (網路購物很便利，但另一方面，也有買過頭的危險。➔ 網購的便利與危險共存。)
    *   `この仕事は給料が良い**反面**、非常に忙しくて休みが少ない。` (這份工作薪水好，但另一方面，非常忙碌且假很少。➔ 薪水高 vs 假少。)

---

#### 🌟 專項練習：排列組合星星題 (Scrambled/Star Questions)

*   `大方の [予想に] [反して] [★彼は] [選挙で大勝利を収めた]` (與大多數人的預測相反，他在選舉中贏得了大勝。➔ 違背預測)
*   `このアパートは [家賃が] [安い反面] [★駅から] [遠くて不便だ]` (這間公寓房租便宜，但另一方面，離車站遠很不方便。➔ 同一間公寓的兩面性)
*   `薬は [病気を治す] [反面] [★副作用が] [出ることもある]` (藥物雖然能治病，但另一方面，有時也會產生副作用。➔ 藥物的兩面性)
"""

# Strip trailing spaces/newlines and append
content_normalized = content_normalized.rstrip() + section_37_content

# Save with newline="" to prevent duplicate carriage returns on Windows
with open(file_path, "w", newline="", encoding="utf-8") as f:
    f.write(content_normalized.replace("\n", "\r\n"))
print("Section 37 appended successfully.")
