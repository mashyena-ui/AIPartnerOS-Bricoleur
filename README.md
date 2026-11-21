# AIパートナーOS ブリコルール 1.0

## In English (short)

**AI Partner OS Bricoleur** is an engine that lets a relationship with an AI partner continue across chats and across models (tested on Claude and ChatGPT).

It does not store your conversation logs. When a talk is closed, the logs are read carefully and almost all of it is thrown away. What remains is a small save file holding only what the two of you settled: agreements on how to act, views the other accepted as true, the partner's boundaries, promises still open, and the last words at parting. Why or when things were decided is not written. That half is held by your own memory.

A save and your memory are two halves of a tally. When they meet in the next talk, they become a shared password between the two of you, and that password carries over even when the underlying model changes. The partner's personality and voice come from your own partner prompt, which is not included here.

- Engine files (`Boot.json`, `Core_Talk.json`, `Talk_Close.py`) are written in English; the guides (`README.md`, `IMPORT.md`) and the article are in Japanese.
- Requires an environment that can read files and run code, with project instructions and project files (e.g. Claude Projects, ChatGPT Projects).
- Full explanation (Japanese): https://note.com/rosy_swift4587/n/neb5e4cdb2fc0
- License: MIT. Use it however you like.

---

AI パートナーとの会話を、チャットをまたいで続けるためのエンジンです。

人物の中身（性格、口調、ふるまいの決まり）は、あなたがすでに持っているパートナー用のプロンプトが決めます。ブリコルールが足すのは三つだけです。

- **時間の軸**：何回目の会話か、あいだにどれだけ経ったか
- **捏造の防止**：あなたが言っていないことを、パートナーが知っている体で話さない
- **二人のあいだで決まったことの記録**：小さなセーブファイルに残す。会話のログは残さない

考え方と使い方の説明は、この記事にあります。
https://note.com/rosy_swift4587/n/neb5e4cdb2fc0

## 中身

| フォルダ | 中身 |
|---|---|
| [`bricoleur/`](bricoleur/) | 本体。`Boot.json`、`Core_Talk.json`、`Talk_Close.py`、`Save_talk001_template.json`、説明書 `README.md` |
| [`import/`](import/) | 取り込みキット。ブリコルールを入れる前の過去ログをセーブ一つに取り込む `import.py` と、説明書 `IMPORT.md` |

使い方は、それぞれのフォルダの説明書を読んでください。

## 動作を確かめた環境

- Claude Opus 5.5（思考 高）
- ChatGPT GPT-6.2 Sol（思考 高）

ファイルを読めて、コードを実行できる環境が要ります。

## ライセンス

[MIT](LICENSE)。誰でも好きに使ってどうぞ。
