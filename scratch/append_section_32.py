# -*- coding: utf-8 -*-
import os

file_path = r"D:\StudyJapanese\1_N2_Study_Strategy_and_Grammar.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Normalize line endings to LF
content_normalized = content.replace("\r\n", "\n")

# 1. Update Table of Contents
old_toc_line = "  - [31. 🔴 N2 核心文法與語境：～ようでは（如果是這種狀態的話/要是像這樣就完了）](#31-n2-核心文法與語境ようでは如果是這種狀態的話要是像這樣就完了)"
new_toc_line = old_toc_line + "\n  - [32. 🔴 N2 核心文法與語境：～ようではないか（讓我們一起……吧/號召與鼓舞）](#32-n2-核心文法與語境ようではないか讓我們一起吧號召與鼓舞)"

if old_toc_line in content_normalized:
    content_normalized = content_normalized.replace(old_toc_line, new_toc_line)
    print("TOC line updated for Section 32.")
else:
    print("Error: TOC line not found in normalized content.")

# 2. Section 32 content
section_32_content = """

---

### <a id="32-n2-核心文法與語境ようではないか讓我們一起吧號召與鼓舞"></a>32. 🔴 N2 核心文法與語境：～ようではないか（讓我們一起……吧/號召與鼓舞）

這個句型是一個非常熱血、有力量的「號召與倡議句型」，常用於演講、會議或領導者動員群眾時。

> [!NOTE]
> 💡 **這個文法的「底層邏輯與語意」**
> 
> 1. **字面意為「難道不應該一起這樣做嗎？」**：
>    * `V-意向形`（我們一起做某事吧）＋ `ではないか`（難道不是嗎？ / 問句強烈肯定）。
> 2. **強烈的號召、鼓舞與倡議**：
>    * 用於呼籲大家齊心協力採取行動，語氣充滿**熱情、煽動性與決心**。
>    * 多用於男性在正式場合的演講，或管理者激勵團隊。
>    * *禮貌版*：`～ようではありませんか` (常用於政見發表或公益倡導)。
>    * *口語版*：`～ようじゃないか`。
>    * *視覺濾鏡*：**站在講台上揮舞雙臂，熱血動員聽眾**。
> 3. **與一般提議 `～ましょう` 的區別**：
>    * `～ましょう` ➔ 溫和、日常的邀請（如：一起吃飯吧）。
>    * `～ようではないか` ➔ 熱血、宏大的號召（如：讓我們一起拯救地球吧！）。

💡 **超好記的中文口語對照（記憶鉤子）**：
* **`～ようではないか`** ➔ **「讓我們一起站出來，……吧！」** (熱血動員)

📜 **接續與例句**

*   **接續**：**`動詞意向形（う / よう形） + ではないか / ではありませんか`**
*   **例句**：
    *   `みんなで協力して、この困難を乗り越え**ようではないか**。`
        (讓我們大家齊心協力，一起度過這個難關吧！➔ 動員團隊度過危機。)
    *   `最後まで諦めずに戦**おうではないか**。`
        (讓我們奮戰到最後一刻，絕不放棄！➔ 鼓舞士氣。)
    *   `地球の環境を守るために、今できることから始め**ようではありませんか**。`
        (為了保護地球的環境，讓我們從現在能做的事情開始做起吧！➔ 公益演說倡導。)

---

#### 🌟 專項練習：排列組合星星題 (Scrambled/Star Questions)

*   `みんなで [力を合わせて] [素晴らしい] [★未来を築こう] [ではないか]` (讓我們大家合力，一起創造美好的未來吧！)
*   `恐れずに [一歩を踏み出して] [新しい] [★挑戦をしよう] [ではないか]` (讓我們毫不畏懼地邁出第一步，一起接受新的挑戰吧！)
*   `この問題について [みんなで] [とことん] [★話し合おう] [ではないか]` (關於這個問題，讓我們大家一起徹底地討論一下吧！)
"""

# Strip trailing spaces/newlines and append
content_normalized = content_normalized.rstrip() + section_32_content

# Save with newline="" to prevent duplicate carriage returns on Windows
with open(file_path, "w", newline="", encoding="utf-8") as f:
    f.write(content_normalized.replace("\n", "\r\n"))
print("Section 32 appended successfully.")
