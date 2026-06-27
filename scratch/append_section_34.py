# -*- coding: utf-8 -*-
import os

file_path = r"D:\StudyJapanese\1_N2_Study_Strategy_and_Grammar.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Normalize line endings to LF
content_normalized = content.replace("\r\n", "\n")

# 1. Update Table of Contents
old_toc_line = "  - [33. 🔴 N2 核心文法與接續：～ようか～まいか（要不要……的內心糾結與猶豫）](#33-n2-核心文法與接續ようかまいか要不要的內心糾結與猶豫)"
new_toc_line = old_toc_line + "\n  - [34. 🔴 N2 核心辨析：許されない vs 許されぬ vs 許されざる（現代否定 vs 古文終止 vs 古文連體）](#34-n2-核心辨析許されない-vs-許されぬ-vs-許されざる現代否定-vs-古文終止-vs-古文連體)"

if old_toc_line in content_normalized:
    content_normalized = content_normalized.replace(old_toc_line, new_toc_line)
    print("TOC line updated for Section 34.")
else:
    print("Error: TOC line not found in normalized content.")

# 2. Section 34 content
section_34_content = """

---

### <a id="34-n2-核心辨析許されない-vs-許されぬ-vs-許されざる現代否定-vs-古文終止-vs-古文連體"></a>34. 🔴 N2 核心辨析：許されない vs 許されぬ vs 許されざる（現代否定 vs 古文終止 vs 古文連體）

這三個詞都是動詞「許す（yurusu - 寬恕/允許）」的被動否定形式，在中文裡都翻成「不被允許 / 無法寬恕 / 禁忌的」。但它們在**古今文法角色（現代否定 vs. 古文結尾 vs. 古文修飾名詞）**以及語氣上有著非常明確的分工。

> [!NOTE]
> 💡 **這三個詞的「底層邏輯與文意分工」**
> 
> 1. **`許されない`（現代標準否定：不被允許）**：
>    * **文法角色**：現代日語的標準否定型（被動 `許される` ＋ 否定 `ない`）。
>    * **語境**：用於最普通的口語、公文、新聞，客觀地說明某事不被法規或大眾允許。
>    * *例*：`カンニングは絶対に許されない。` (作弊是絕對不被允許的。)
> 2. **`許されぬ`（古文/書面終止形：決不被允許）**：
>    * **文法角色**：文語（古文）的否定終止形（`ぬ` ➔ 用於**句尾結尾**，相當於 `ない`）。
>    * **語境**：帶有**莊嚴、冷酷、文學或戲劇化**的強烈否定氣勢。常用於座右銘、小說台詞或嚴肅規章的警告。
>    * *例*：`これ以上の妥協は許されぬ。` (絕不允許再有任何妥協。➔ 語氣極為剛硬。)
> 3. **`許されざる`（古文連體形：無法寬恕的…… / 禁忌的……）**：
>    * **文法角色**：文語（古文）的否定連體形（`ざる` ➔ **後面必須直接修飾名詞**）。絕對不能放在句尾結尾！
>    * **語境**：用來將後方的名詞定性為「極具罪惡、不可饒恕的」。語感非常文雅、戲劇化。
>    * *例*：`許されざる行為` (不可饒恕的行為)、`許されざる者` (無法被原諒的人 / 經典電影《不可饒恕》片名)。

💡 **超簡單秒殺法則**：
* **`～ない`** ➔ **現代文通用**（句尾或修飾皆可）。
* **`～ぬ`** ➔ **古風/硬派結尾**（放在句尾 `。` 前面）。
* **`～ざる`** ➔ **古風修飾名詞**（後面必須直接加名詞，如 `～ざる者` / `～ざる行為`）。

---

### 🔍 延伸：日檢中常見的「～ざる」與「～ぬ」經典組合

古文否定助動詞 `ず` 的變化在現代日語中已經「化石化」為許多固定詞彙，必須特別注意：

#### 1. 常見的 `～ざる ＋ 名詞` 組合
*   `許されざる**者**` (不可饒恕之人 / 叛徒)
*   `知るざる**事実**` ➔ ⚠️ 現代通常說 `知られざる事実` (不為人知的真實)
*   `持たざる**者**` (一無所有的人 / 弱勢群體)
*   `意図せざる**結果**` (非意圖/意料之外的結果)

#### 2. 常見的 `～ぬ` 結尾
*   `言うに言え**ぬ**秘密` (說不出口的秘密。➔ 這裡的 `ぬ` 是修飾秘密，古文連體形亦可為 `ぬ`，但在現代多做固定片語。)

---

#### 🌟 專項練習：排列組合星星題 (Scrambled/Star Questions)

*   `このような [不正は] [社会的に] [★絶対に] [許されない]` (這種舞弊在社會上是絕對不被允許的。➔ 現代否定)
*   `いかなる [理由が] [あろうとも] [★妥協は] [許されぬ]` (不管有什麼理由，絕不允許任何妥協。➔ 古風結尾)
*   `彼は [組織にとって] [許されざる] [★行為を] [行ってしまった]` (他做出了對組織而言不可饒恕的行為。➔ 古風修飾 `行為`)
"""

# Strip trailing spaces/newlines and append
content_normalized = content_normalized.rstrip() + section_34_content

# Save with newline="" to prevent duplicate carriage returns on Windows
with open(file_path, "w", newline="", encoding="utf-8") as f:
    f.write(content_normalized.replace("\n", "\r\n"))
print("Section 34 appended successfully.")
