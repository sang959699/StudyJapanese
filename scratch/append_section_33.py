# -*- coding: utf-8 -*-
import os

file_path = r"D:\StudyJapanese\1_N2_Study_Strategy_and_Grammar.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Normalize line endings to LF
content_normalized = content.replace("\r\n", "\n")

# 1. Update Table of Contents
old_toc_line = "  - [32. 🔴 N2 核心文法與語境：～ようではないか（讓我們一起……吧/號召與鼓舞）](#32-n2-核心文法與語境ようではないか讓我們一起吧號召與鼓舞)"
new_toc_line = old_toc_line + "\n  - [33. 🔴 N2 核心文法與接續：～ようか～まいか（要不要……的內心糾結與猶豫）](#33-n2-核心文法與接續ようかまいか要不要的內心糾結與猶豫)"

if old_toc_line in content_normalized:
    content_normalized = content_normalized.replace(old_toc_line, new_toc_line)
    print("TOC line updated for Section 33.")
else:
    print("Error: TOC line not found in normalized content.")

# 2. Section 33 content
section_33_content = """

---

### <a id="33-n2-核心文法與接續ようかまいか要不要的內心糾結與猶豫"></a>33. 🔴 N2 核心文法與接續：～ようか～まいか（要不要……的內心糾結與猶豫）

這個句型用來表示某人在面對某個行動時，內心產生的「做還是不做」的強烈糾結、猶豫或迷茫。

> [!NOTE]
> 💡 **這個文法的「底層邏輯與語意」**
> 
> 1. **字面意為「要這樣做呢？還是不要呢？」**：
>    * `V-意向形 + か`（要這樣做嗎？） ＋ `V-まい + か`（不要這樣做嗎？）。
>    * `まい` 是古日語的「否定推測/否定意志」助動詞，在現代日語中相當於 `～ないだろう / ～ないつもりだ`（打算不……）。
> 2. **強烈的內心衝突（糾結）**：
>    * 句型中前後使用的**必須是同一個動詞**。
>    * 後方常呼應：迷う（猶豫）、悩む（苦惱）、考える（考慮）。
>    * *視覺濾鏡*：**雙手抱頭，在天平兩端左右搖擺**。
> 3. **與 `～るか～ないか` 的區別**：
>    * `～るか～ないか` ➔ 一般的事實詢問（如：去還是不去請告訴我）。
>    * `～ようか～まいか` ➔ 專門用於描述**當事人「內心的意志掙扎」**（到底該不該做這個動作）。

💡 **接續的特殊變化（まい 的接續是 N2 考試重點！）**
*   **五段動詞（Group 1）**：**`辭書形 + まい`**
    *   *例*：`言うまい` (不說)、`買うまい` (不買)、`行くまい` (不去)。
*   **一段動詞（Group 2）**：**`辭書形 + まい`** 或 **`去ます形 + まい`** (去ます形更常用)
    *   *例*：`食べるまい / 食べまい`、`信じるまい / 信じまい`。
*   **不規則動詞**：
    *   **する** ➔ `するまい` / `すまい` / `しまい`
    *   **来る** ➔ `来るまい` / `来まい（こまい）`

📜 **例句**

*   `本当のことを彼に言**おうか**言**うまいか**、ずっと迷っている。`
    (要不要把真相告訴他，我一直都在猶豫。➔ 同一個動詞 言う 的意志糾結。)
*   `新しいスマホを買**おうか**買**うまいか**、毎日悩んでいます。`
    (買不買新手機，我每天都在苦惱。)
*   `雨が降りそうなので、傘を持ってい**こうか**持ってい**まいか**考えている。`
    (因為好像要下雨了，正在考慮要不要帶傘。)

---

#### 🌟 專項練習：排列組合星星題 (Scrambled/Star Questions)

*   `真実を [話そうか] [話すまいか] [★悩んだ末に] [沈黙を守ることにした]` (在糾結要不要說出真相的最後，他決定保持沉默。)
*   `この服を [買おうか] [買うまいか] [★迷っている] [うちに売れてしまった]` (在猶豫要不要買這件衣服的時候，它就被賣掉了。)
*   `会社を [辞めようか] [辞めまいか] [★一人で] [ずいぶん悩んだ]` (要不要辭職，我一個人苦惱了很久。)
"""

# Strip trailing spaces/newlines and append
content_normalized = content_normalized.rstrip() + section_33_content

# Save with newline="" to prevent duplicate carriage returns on Windows
with open(file_path, "w", newline="", encoding="utf-8") as f:
    f.write(content_normalized.replace("\n", "\r\n"))
print("Section 33 appended successfully.")
