# -*- coding: utf-8 -*-
import os

file_path = r"D:\StudyJapanese\1_N2_Study_Strategy_and_Grammar.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Normalize line endings to LF
content_normalized = content.replace("\r\n", "\n")

# 1. Update Table of Contents
old_toc_line = "  - [25. 🔴 N2 核心文法與語境：～のももっともだ（也是理所當然的/合乎情理）](#25-n2-核心文法與語境のももっともだ也是理所當然的合乎情理)"
new_toc_line = old_toc_line + "\n  - [26. 🔴 N2 核心辨析：～工程の下で（のしたで） vs ～のもとで（の下で/の元で/の本で）](#26-n2-核心辨析の下でのしたで-vs-のもとでの下での元での本で)"
# Wait, let's make sure there is no typo in new_toc_line. Let's make it:
new_toc_line = old_toc_line + "\n  - [26. 🔴 N2 核心辨析：～の下で（のした為） vs ～のもとで（の下で/の元で/の本で）](#26-n2-核心辨析の下でのしたで-vs-のもとでの下での元での本で)"
# Wait, let's write it cleanly:
new_toc_line = old_toc_line + "\n  - [26. 🔴 N2 核心辨析：～の下で（のしたで） vs ～のもとで（の下で/の元で/の本で）](#26-n2-核心辨析の下でのしたで-vs-のもとでの下での元での本で)"

if old_toc_line in content_normalized:
    content_normalized = content_normalized.replace(old_toc_line, new_toc_line)
    print("TOC line updated for Section 26.")
else:
    print("Error: TOC line not found in normalized content.")

# 2. Section 26 content
section_26_content = """

---

### <a id="26-n2-核心辨析の下でのしたで-vs-のもとでの下での元での本で"></a>26. 🔴 N2 核心辨析：～の下で（のしたで） vs ～のもとで（の下で/の元為/の本で）

這組語法的混淆主要來自於：同一個漢字「下」有兩種讀音（`した` 與 `もと`），且「もと」在日文中可以用「下」、「元」、「本」三種漢字表示。

> [!NOTE]
> 💡 **這兩個文法的「底層邏輯與語境差異」**
> 
> 1. **`～の下で`（讀作：のしたで） ➔ 物理空間的「下方」**：
>    * **邏輯**：`下（した）` 指實體空間的「下面、底下」。
>    * **語境**：只用於**物理的、肉眼可見的實體陰影或遮蔽物下方**。
>    * *例*：机の下（桌子下）、木の下（樹下）、青空の下（藍天下）。
> 2. **`～のもとで`（讀作：のもとで） ➔ 抽象概念的「在……指導/影響/條件之下」**：
>    * **邏輯**：`もと` 寫成「下、元、本」，本意是「根源、基礎」。
>    * **語境**：指在某種**抽象的環境、條件、影響力、名義或人的指導保護**之下。
>    * *例*：先生の指導のもとで（在老師的指導下）、両親の愛情のもとで（在父母的愛護下）。

---

### 🔍 漢字寫法「下」、「元」、「本」的微妙區別（皆讀作 もと）

當語法讀作 `のもとで` 時，選用的漢字會帶有不同的側重點：

#### 1. 寫作「下（もと）」 ➔ 側重於：條件、規章、名義、支配
用於抽象的環境或規則約束之下。
*   `厳しい規則の**下で**生活する。` (在嚴格的規則之下生活。)
*   `開発的名目の**下で**自然が破壊される。` (在開發的名義之下自然被破壞。)

#### 2. 寫作「元（もと）」 ➔ 側重於：人、指導、保護、身邊
用於受到某個「具體的人」的影響或教導。
*   `名医の**元で**修業を積む。` (在名醫的門下/身邊累積修行。)
*   `親の**元を**離れて一人暮らしを始める。` (離開父母的身邊開始獨自生活。)

#### 3. 寫作「本（もと）」 ➔ 側重於：根源、根本
在現代文法書中，為了避免與「書籍（ほん）」混淆，通常**直接寫作平假名 `のもとで`**，極少直接用漢字「本」來寫這個文法。
*   `両親の愛情**のもとで**育つ。` (在父母的愛護之下長大。)

---

#### 🌟 專項練習：排列組合星星題 (Scrambled/Star Questions)

*   `暑いので [桜の] [木の下で] [★お冷やを] [飲んで休憩した]` ➔ `暑いので [桜の] [木の下で] [★休む] [ことにした]` (因為很熱，決定在櫻花樹下休息。➔ 物理的 `した`)
*   `厳しい [先生の] [指導の] [★もとで] [修行に励んだ]` (在嚴格的老師指導之下努力修行。➔ 抽象的 `もと`)
*   `親の [保護の] [下で] [★何不自由なく] [暮らしている]` (在父母的保護之下無憂無慮地生活著。)
*   `青空の [下で] [みんなで] [★お弁当を] [食べた]` (在藍天之下，大家一起吃了便當。)
"""

# Strip trailing spaces/newlines and append
content_normalized = content_normalized.rstrip() + section_26_content

# Cleanup typo artifacts
content_normalized = content_normalized.replace("の元為", "の元で")
content_normalized = content_normalized.replace("～工程の下で", "～の下で")
content_normalized = content_normalized.replace("のした為", "のしたで")

# Save with newline="" to prevent duplicate carriage returns on Windows
with open(file_path, "w", newline="", encoding="utf-8") as f:
    f.write(content_normalized.replace("\n", "\r\n"))
print("Section 26 appended successfully.")
