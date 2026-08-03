# V0.1 Locale Roadmap

| 状态 | 标准 locale | Ren'Py 语言名/目录 | 游戏显示名 | 说明 |
|---|---|---|---|---|
| 源语言 | zh-Hans | `None` / 无项目 tl 目录 | 简体中文 | 当前权威源文；`Language(None)` |
| Round 1 实施 | en | `english` / `game/tl/english/` | English | 真实可用的样板内容；`Language("english")` |
| 下一候选 | zh-Hant-TW | `chinese-traditional` / `game/tl/chinese-traditional/` | 繁體中文（台灣） | 待完成真实翻译后才显示 |
| 下一候选 | vi | `vietnamese` / `game/tl/vietnamese/` | Tiếng Việt | 待完成真实翻译后才显示 |
| 后续候选 | ja | `japanese` / `game/tl/japanese/` | 日本語 | 规划接口，不创建空文件 |
| 后续候选 | th | `thai` / `game/tl/thai/` | ไทย | 规划接口，不创建空文件 |
| 后续候选 | ko | `korean` / `game/tl/korean/` | 한국어 | 规划接口，不创建空文件 |

所有未来语言都从简体中文权威源文本进行本地化。英文术语表、翻译结构、UI 长度测试和语言选择模式可复用；叙事措辞、称谓、语序与人物语气不得从英语二次转译。

