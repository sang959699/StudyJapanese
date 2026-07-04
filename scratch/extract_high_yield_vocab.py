# -*- coding: utf-8 -*-
import re
import os

vocab_file_path = r"D:\StudyJapanese\3_N2_Vocabulary_Bank_and_Verbs.md"
adverb_file_path = r"D:\StudyJapanese\4_N2_Adverbs_and_Conjunctions.md"
review_file_path = r"D:\StudyJapanese\N2_Kanji_Vocabulary_Final_Review.md"

def extract_red_rows_from_table(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    extracted_rows = []
    headers = []
    in_table = False
    
    for line in lines:
        line_str = line.strip()
        if "|" in line_str:
            # Check if this is a table separator line (e.g. | :--- | :--- |)
            if re.match(r"^\|\s*[:\-]+\s*\|", line_str):
                continue
            
            # Split cells
            cells = [c.strip() for c in line_str.split("|")[1:-1]]
            
            # Check if headers
            if "漢字" in cells or "自動詞" in cells or "接續詞" in cells or "副詞" in cells:
                headers = cells
                in_table = True
                continue
            
            # If in table, check if any cell contains the red circle 🔴
            # (sometimes it's at the beginning of a cell like "🔴 **長引く**" or "**🔴 長引く**")
            has_red = False
            for cell in cells:
                if "🔴" in cell:
                    has_red = True
                    break
            
            if has_red:
                extracted_rows.append((headers, cells))
        else:
            in_table = False
            
    return extracted_rows

# Extract
red_vocab = extract_red_rows_from_table(vocab_file_path)
red_adverbs = extract_red_rows_from_table(adverb_file_path)

print(f"Extracted {len(red_vocab)} high-frequency vocabulary rows.")
print(f"Extracted {len(red_adverbs)} high-frequency adverb/conjunction rows.")

# Let's group red_vocab into:
# - Transitive/Intransitive pairs (where header is "自動詞（表示狀態/自然改變）" or similar)
# - Regular vocabulary (where header is "漢字" / "讀音" / "中文釋義" / "記憶要點 / 例句")
trans_intra_pairs = []
regular_vocab = []

for headers, cells in red_vocab:
    is_trans_intra = False
    if headers:
        if "自動詞（表示狀態/自然改變）" in headers or "自動詞" in headers:
            is_trans_intra = True
        elif len(cells) == 3 and len(headers) >= 3 and "画面" in headers[2]:
            is_trans_intra = True
            
    if is_trans_intra:
        trans_intra_pairs.append(cells)
    else:
        regular_vocab.append(cells)

# Format to markdown
output_content = """# 🏆 JLPT N2 考前最後衝刺：核心漢字與詞彙秒殺清單 (高頻大詞庫版)

親愛的同學，明天就是 JLPT 日檢考試了！這份複習清單已為你從厚重的筆記中，**自動篩選並提取出所有標註為高頻（🔴 紅圈）的核心自他動詞、高頻單字、副詞與接續詞**。

這是一份「純乾貨」的高 yield 衝刺清單，考前最後一晚，利用這張表快速瀏覽「漢字視覺畫面」與「秒殺考點」，祝你明天順利合格！🏆🌸

---

## 🎯 一、 考前最常考：自他動詞高頻對比表 (🔴)

在 N2 的詞彙與聽力中，**自動詞表示狀態或自然發生（主語用 が），他動詞表示人有意施加的動作（賓語用 を）**。以下為你篩選出筆記中最常考的自他動詞對應：

| 自動詞 (が ＋ 狀態/自然改變) | 他動詞 (を ＋ 人為施加動作) | 核心畫面與記憶要點 |
| :--- | :--- | :--- |
"""

for cells in trans_intra_pairs:
    if len(cells) >= 3:
        # Clean markdown formatting (like replacing newlines in cell with <br> for table layout)
        auto_v = cells[0].replace("\n", "<br>")
        trans_v = cells[1].replace("\n", "<br>")
        memo = cells[2].replace("\n", "<br>")
        output_content += f"| {auto_v} | {trans_v} | {memo} |\n"

output_content += """
---

## 📚 二、 分類核心高頻單字表 (🔴)

以下為你整理出筆記中所有標註為 **🔴 高頻** 的核心動詞、名詞與形容詞，按場景與語意進行複習：

| 漢字 | 讀音 | 中文釋義 | 記憶要點 / 例句 |
| :--- | :--- | :--- | :--- |
"""

for cells in regular_vocab:
    if len(cells) >= 4:
        kanji = cells[0].replace("\n", "<br>")
        reading = cells[1].replace("\n", "<br>")
        meaning = cells[2].replace("\n", "<br>")
        memo = cells[3].replace("\n", "<br>")
        output_content += f"| {kanji} | {reading} | {meaning} | {memo} |\n"

output_content += """
---

## 📢 三、 考前必背：高頻副詞與接續詞呼應表 (🔴)

副詞與接續詞是日檢的「秒殺送分題」。看到副詞要直接聯想後方的句尾搭配（例如：看到 `必ずしも` 找 `とは限らない`）！

| 副詞 / 接續詞 | 讀音 | 中文釋義 | 記憶要點 / 核心語意 / 例句 |
| :--- | :--- | :--- | :--- |
"""

for headers, cells in red_adverbs:
    if len(cells) >= 4:
        word = cells[0].replace("\n", "<br>")
        reading = cells[1].replace("\n", "<br>")
        meaning = cells[2].replace("\n", "<br>")
        memo = cells[3].replace("\n", "<br>")
        output_content += f"| {word} | {reading} | {meaning} | {memo} |\n"

output_content += """
---

## 📝 考前心態與答題秒殺技巧

1. **同音異義字快速漢字分工**：
   * **掛 / 架** ➔ 物理吊掛、蓋被子、澆醬汁、乘法、架橋。
   * **懸** ➔ 賭上生命、名譽等「無形物」 (`命を懸ける`、`にかけては`)。
   * **賭** ➔ 賭博「有形金錢、資產」 (`お金を賭ける`)。
   * **駆** ➔ 騰空飛奔、跑步 (`草原を駆ける`)。
   * **整う / 整える** ➔ `準備が整う` (準備好) / `息を整える` (調整呼吸)。
   * **配る** ➔ `気を配る` (細心體貼) / `目を配る` (看守)。

2. **冷靜看字源**：遇到不會的單字，閉上眼睛想一下它的**「大和語讀音（和語）」**。
   * 例如：`かける` ➔ 畫面是「懸空、吊掛、跨越」。
   * `はる` ➔ 畫面是「撐開、拉平、張網」。
   * `ぬく` ➔ 畫面是「穿透、拔出、越過」。
   運用大和語的核心物理畫面，去對推漢字的意思，正確率會極高！

**放鬆心情，正常發揮！明天你一定可以順利合格！加油！🏆🌸**
"""

with open(review_file_path, "w", encoding="utf-8") as f:
    f.write(output_content.replace("\n", "\r\n"))

print("Successfully compiled and updated review sheet!")
