# -*- coding: utf-8 -*-
import os

file_path = r"D:\StudyJapanese\1_N2_Study_Strategy_and_Grammar.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Normalize line endings to LF
content_normalized = content.replace("\r\n", "\n")

# 1. Update Table of Contents
old_toc_line = "  - [35. 🔴 N2 核心辨析：とともに vs に伴って vs につれて vs にしたがって（隨著/伴隨著的四大「秒殺差異）](#35-n2-核心辨析とともに-vs-に伴って-vs-につれて-vs-にしたがって隨著伴隨的的四大秒殺差異)"
# Wait, let's look at the exact line in Section 35 script. It had:
# "  - [35. 🔴 N2 核心辨析：とともに vs に伴って vs につれて vs にしたがって（隨著/伴隨著的四大「秒殺差異」）](#35-n2-核心辨析とともに-vs-に伴って-vs-につれて-vs-にしたがって隨著伴隨的的四大秒殺差異)"
old_toc_line = "  - [35. 🔴 N2 核心辨析：とともに vs に伴って vs につれて vs にしたがって（隨著/伴隨著的四大「秒殺差異」）](#35-n2-核心辨析とともに-vs-に伴って-vs-につれて-vs-にしたがって隨著伴隨的的四大秒殺差異)"
new_toc_line = old_toc_line + "\n  - [36. 🔴 N2 核心辨析：～たとたん vs ～あげく（即時瞬間發生 vs 漫長折騰後的糟糕結果）](#36-n2-核心辨析たとたん-vs-あげく即時瞬間發生-vs-漫長折騰後的糟糕結果)"

if old_toc_line in content_normalized:
    content_normalized = content_normalized.replace(old_toc_line, new_toc_line)
    print("TOC line updated for Section 36.")
else:
    print("Error: TOC line not found in normalized content.")

# 2. Section 36 content
section_36_content = """

---

### <a id="36-n2-核心辨析たとたん-vs-あげく即時瞬間發生-vs-漫長折騰後的糟糕結果"></a>36. 🔴 N2 核心辨析：～たとたん vs ～あげく（即時瞬間發生 vs 漫長折騰後的糟糕結果）

這兩個句型在時間感上有著極大的反差：一個形容**「0秒發生的瞬間物理反應」**，另一個形容**「經歷了漫長的折騰、苦惱，最後卻落得糟糕下場」**。

> [!NOTE]
> 💡 **這兩個文法的「底層邏輯與語意差異」**
> 
> 1. **`～たとたん（に）`（瞬間即時性：一……就…… / 剛一……的瞬間）**：
>    * **漢字與原意**：`途端` (totan - 剛好的當口、瞬間)。
>    * **語境**：前項動作做完的「那一瞬間」，後項的物理反應、生理反應或突發狀況**立刻**發生。
>    * **規則限制**：後半句不能包含說話者自己的意志、命令或請求（例如：回家後立刻去讀書 ❌）。
>    * *例*：`立ち上がったとたん、めまいがした。` (一站起來的瞬間，就頭暈了。➔ 0秒間隔。)
> 2. **`～あげく（に）`（漫長折騰與壞結局：最後、結果……）**：
>    * **漢字與原意**：`挙げ句` (ageku - 連歌/長詩的最後一聯結尾)。
>    * **語境**：表示經歷了**很長的時間、反覆的糾結、爭吵或重重折騰**之後，終於迎來了一個結局。
>    * **結局特徵**：後半句的結局**幾乎都是不好的、令人遺憾的或令人失望的**（如：沒買、放棄、失敗、吵架）。
>    * *例*：`さんざん悩んだあげく、結局諦めることにした。` (苦惱了老半天，最後決定放棄。➔ 長期內心掙扎，最後消極放棄。)

💡 **超直覺秒殺法則**：
* **`～たとたん`** ➔ **「起步走 ➔ 0秒瞬間摔倒」** (驚人的即時物理/生理反應)
* **`～あげく`** ➔ **「折騰了半天 ➔ 最後卻落得一場空」** (漫長痛苦過程 ＋ 壞結局)

---

### 🔍 語意與接續詳解

#### 💡 1. ～たとたん（に） ➔ 【一……立刻（瞬間突發）】
*   **接續**：**`動詞た形 + とたん（に）`**
*   **例句**：
    *   `窓を開けた**とたん**、冷たい風が入ってきた。` (一打開窗戶，冷風瞬間灌了進來。➔ 物理現象。)
    *   `お酒を一口飲んだ**とたん**、顔が真っ赤になった。` (才剛喝一口酒，臉瞬間就變通紅。➔ 生理反應。)

#### 💡 2. ～あげく（に） ➔ 【費盡心思後卻……（糟糕結局）】
*   **接續**：**`動詞た形 / 名詞 + の + あげく（に）`**
*   **例句**：
    *   `何時間も話し合った**あげく**、結局結論は出なかった。` (討論了好幾個小時，結果還是沒得出結論。➔ 時間浪費了卻沒結果。)
    *   `何度も手術を重ねた**あげく**、その犬は死んでしまった。` (動了幾次手術，那隻狗最終還是死去了。)
    *   `口論の**あげく**、殴り合いの喧嘩になった。` (激烈爭吵的結果，演變成了動手互毆。)

---

#### 🌟 專項練習：排列組合星星題 (Scrambled/Star Questions)

*   `立ち上がった [とたん] [頭が] [★ふらふらして] [倒れそうになった]` (一站起來的瞬間，頭就暈乎乎地差點倒下。➔ 瞬間生理反應)
*   `さんざん [迷った] [あげく] [★何も買わずに] [店を出た]` (糾結了老半天，結果什麼都沒買就走出了店門。➔ 過程折騰 ＋ 壞結局)
*   `犯人は [警察の] [追跡の] [★あげくに] [逮捕された]` (嫌犯在警察的追擊之下，最終被逮捕了。➔ 追逐折騰的結果)
"""

# Strip trailing spaces/newlines and append
content_normalized = content_normalized.rstrip() + section_36_content

# Save with newline="" to prevent duplicate carriage returns on Windows
with open(file_path, "w", newline="", encoding="utf-8") as f:
    f.write(content_normalized.replace("\n", "\r\n"))
print("Section 36 appended successfully.")
