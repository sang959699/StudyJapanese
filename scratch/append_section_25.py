# -*- coding: utf-8 -*-
import os

file_path = r"D:\StudyJapanese\1_N2_Study_Strategy_and_Grammar.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Normalize line endings to LF
content_normalized = content.replace("\r\n", "\n")

# 1. Update Table of Contents
old_toc_line = "  - [24. 🔴 N2 核心辨析：～にも拘わらず vs ～に関わらず（儘管……卻 vs 不論……都）](#24-n2-核心辨析にも拘わらず-vs-に関わらず儘管卻-vs-不論都)"
new_toc_line = old_toc_line + "\n  - [25. 🔴 N2 核心文法與語境：～のももっともだ（也是理所當然的/合乎情理）](#25-n2-核心文法與語境のももっともだ也是理所當然的合乎情理)"

if old_toc_line in content_normalized:
    content_normalized = content_normalized.replace(old_toc_line, new_toc_line)
    print("TOC line updated for Section 25.")
else:
    print("Error: TOC line not found in normalized content.")

# 2. Section 25 content
section_25_content = """

---

### <a id="25-n2-核心文法與語境のももっともだ也是理所當然的合乎情理"></a>25. 🔴 N2 核心文法與語境：～のももっともだ（也是理所當然的/合乎情理）

這個句型用來表示說話者對某人的反應或行為表示「非常理解、認同，認為那是合乎情理的」。

> [!NOTE]
> 💡 **這個文法的「底層邏輯與語意」**
> 
> 1. **字源與本意**：
>    * `もっとも` 寫成漢字是 **「尤も」**，意為「合理的、對的、理所當然的」。
>    * 當我們用 `A のももっともだ` 時，字面意思是「做 A 這件事，也是非常合乎道理的」。
> 2. **強烈的同理心與認同感**：
>    * 說話者並非在做冷冰冰的邏輯推理，而是**站在對方的立場，對其情緒反應（如生氣、悲傷、驚訝等）表示同情與高度理解**（「換作是我也會這樣」）。
>    * *視覺濾鏡*：**點頭如搗蒜，深表同理**。
> 3. **與 `～わけだ / ～当然だ` 的區別**：
>    * `～のももっともだ` ➔ 側重於對他人**主觀情緒反應**的「同理與合情合理化」。
>    * `～わけだ` ➔ 側重於「因為 A 原因，所以得出 B 結果」的**客觀邏輯推導（難怪）**。不能用於同理情緒。
>      * *例*：`エアコンが切れている。暑いわけだ。` (冷氣關了。難怪這麼熱。➔ 客觀邏輯。不能用 `暑いのももっともだ` ❌。)
>    * `～のは当然だ / 当たり前だ` ➔ 語氣非常強硬、直接（本來就該這樣）。而 `もっともだ` 語氣則較溫和、客觀，帶有「入情入理」的體貼感。

💡 **超好記的中文口語對照（記憶鉤子）**：
* **`～のももっともだ`** ➔ **「在這種情況下，他會這樣反應『也是非常合乎情理的』。」**

📜 **接續與例句**

*   **接續**：**`動詞・形容詞普通形 + のももっともだ`** (名詞 + な/である + のももっともだ)
*   **例句**：
    *   `あんなにひどいことを言われたのだから、彼女が怒る**のももっともだ**。`
        (被說了那麼過分的話，她會生氣也是理所當然的。➔ 同理她的生氣。)
    *   `これまでずっと準備してきたのだから、不合格になってがっかりする**のももっともだ**。`
        (一直以來準備了這麼久，沒考上而感到沮喪也是很合乎情理的。➔ 同理他的沮喪。)
    *   `一流のプロが作った料理なのだから、美味しい**のももっともだ**。`
        (既然是一流廚師做的料理，美味也是理所當然的。)

---

#### 🌟 專項練習：排列組合星星題 (Scrambled/Star Questions)

*   `あんなにひどい [ことを] [言われたのだから] [★彼女が怒る] [のももっともだ]` (被說了那麼過分的話，她會生氣也是理所當然的。)
*   `これまで [ずっと] [準備してきたのだから] [★がっかりする] [のももっともだ]` (準備了這麼久，感到沮喪也是合乎情理的。)
*   `高い [給料を] [もらっているのだから] [★彼がよく働く] [のももっともだ]` (既然拿了高薪，他努力工作也是理所當然的。)
*   `初めての [海外旅行] [なのだから] [★緊張する] [のももっともだ]` (因為是第一次出國旅遊，感到緊張也是很正常的。)
"""

# Strip trailing spaces/newlines and append
content_normalized = content_normalized.rstrip() + section_25_content

# Save with newline="" to prevent duplicate carriage returns on Windows
with open(file_path, "w", newline="", encoding="utf-8") as f:
    f.write(content_normalized.replace("\n", "\r\n"))
print("Section 25 appended successfully.")
