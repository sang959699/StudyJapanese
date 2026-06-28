# -*- coding: utf-8 -*-
import os

file_path = r"D:\StudyJapanese\1_N2_Study_Strategy_and_Grammar.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Normalize line endings to LF
content_normalized = content.replace("\r\n", "\n")

# 1. Update Table of Contents
old_toc_line = "  - [49. 🔴 N2 核心文法：～ようがない / ～ようもない（無法/無從……的接續與修飾限制）](#49-n2-核心文法ようがない-vs-ようもない無法無從的接續與修飾限制)"
new_toc_line = old_toc_line + "\n  - [50. 🔴 N2 核心文法：～折には / ～折に（值此之際/……的時候之商務敬語優雅表達）](#50-n2-核心文法折には-vs-折に值此之際的時候之商務敬語優雅表達)"

if old_toc_line in content_normalized:
    content_normalized = content_normalized.replace(old_toc_line, new_toc_line)
    print("TOC line updated for Section 50.")
else:
    print("Error: TOC line not found in normalized content.")

# 2. Section 50 content
section_50_content = """

---

### <a id="50-n2-核心文法折には-vs-折に值此之際的時候之商務敬語優雅表達"></a>50. 🔴 N2 核心文法：～折には / ～折に（值此之際/……的時候之商務敬語優雅表達）

這是商務書信、電子郵件以及正式敬語社交中極其高頻的**優雅替代語**。它的功能與普通的「時（とき）」相同，但具有非常強烈的「尊重與鄭重」語氣。

> [!NOTE]
> 💡 **這型文法的「底層邏輯與語源」**
> 
> * **漢字與語源**：寫作 **「折（おり）」**。字源來自 `折る` (折斷/折疊)。古代日本人會透過「折斷樹枝、或摺疊紙張」來記錄某個特定的**季節、契機、或值得紀念的事件時刻**。因此，`折` 被用來代表「時刻、機會、時候」。
> * **文法語意**：`～折には` ➔ **「在……的時候 / 值此……之際 / 趁著……的機會」**。
> * **語境分工**：
>   * `～のとき` ➔ 口語、中性、日常通用。
>   * `～折（には/に）` ➔ 專門用於**極度正式、對客戶或長輩**的商務敬語書信中。常用於美好的重逢或期待。
>   * `～の際（には）` ➔ 同樣表示「在……的時候」，但 `際` 偏向客觀說明、公告或指示（如：緊急之際、退房時），較少用於人情社交。

💡 **超簡單秒殺法則**：
* **`～折には`** ➔ **「在……的優雅時機點（帶有期待與人情關懷）。」** (例：來日之際、見面之時)
* **`～の際には`** ➔ **「客觀條件被觸發的時候（偏公告/規則說明）。」** (例：避難之時、填寫時)

---

### 🔍 語意與接續詳解

*   **接續**：**`名詞 + の ＋ 折には / 折に`** 或 **`動詞普通形（多為る形或た形） + 折に`**
*   **例句**：
    *   `今度、来日の**折には**、ぜひ弊社にもお立ち寄りください。` (下次您來日本之際，請務必也順道來我們公司坐坐。➔ 經典商務客套。)
    *   `先月、京都へ行った**折に**、古い友人に会った。` (上個月去京都的時候，順道見了一位老朋友。➔ 用 `折に` 顯得比 `とき` 更有生活情調與雅致。)
    *   `次の機会の**折には**、よろしくお願いいたします。` (值此下次機會之際，還請多多指教。)

---

#### 🌟 專項練習：排列組合星星題 (Scrambled/Star Questions)

*   `近くに [お越しの] [折には] [★ぜひ弊社に] [お立ち寄りください]` (當您來到這附近之際，請務必順道來我們公司一趟。➔ 商務敬語客套)
*   `先日 [お会いした] [折に] [★お聞きした] [お話が忘れられません]` (前幾天與您見面之時所聽到的話，我至今仍難以忘懷。➔ 見面之時)
*   `緊急の [際には] [エレベーターを] [★使わずに] [非常口から避難してください]` (緊急之際，請不要搭乘電梯，請從緊急出口進行避難。➔ 公告規則 `の際には` 與 `ずに` 聯動)
"""

# Strip trailing spaces/newlines and append
content_normalized = content_normalized.rstrip() + section_50_content

# Save with newline="" to prevent duplicate carriage returns on Windows
with open(file_path, "w", newline="", encoding="utf-8") as f:
    f.write(content_normalized.replace("\n", "\r\n"))
print("Section 50 appended successfully.")
