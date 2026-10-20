# DEVONthink 简体中文术语表与翻译规则

## 文件格式
- `source/<模块>/<表>.json`：英文原表，键是程序内部键，值是英文界面文字。
- `translations/<模块>/<表>.json`：译文。**键必须与原表完全一致、一个不少**，值为中文。
- 只翻译“值”，键原样照抄。值里的 `%@`、`%d`、`%ld`、`%1$@` 等占位符必须原样保留、数量一致、顺序尽量一致；`\n` 保留；HTML 标签保留。
- 产品名、技术名词不翻译：DEVONthink、DEVONagent、DEVONthink To Go、Dropbox、iCloud、CloudKit、WebDAV、Bonjour、Markdown、HTML、PDF、RSS、OCR、OPML、URL、Wi‑Fi、Spotlight（Apple 中文叫“聚焦”，但此处保留 Spotlight）、Finder 写作“访达”、Quick Look 写作“快速查看”。
- 风格：简体中文，macOS 系统应用的措辞；菜单项简短；标点用中文全角（：、，。…）；省略号用“…”；英文与数字前后不加空格的 Apple 惯例可不强求，但不要在中文之间留空格。
- 值本身是空字符串、纯符号、纯数字、文件扩展名、快捷键名的，原样保留。
- 不确定含义时以 DEVONthink 的功能语境判断（文稿管理软件）；宁可直译准确，不要自由发挥。

## 术语
| 英文 | 中文 |
|---|---|
| Database | 数据库 |
| Group | 群组 |
| Smart Group | 智能群组 |
| Smart Rule | 智能规则 |
| Inbox / Inboxes | 收件箱 |
| Global Inbox | 全局收件箱 |
| Globals | 全局 |
| Tag(s) | 标签 |
| Label | 颜色标签 |
| Flag / Flagged / Unflagged | 旗标 / 已加旗标 / 未加旗标 |
| Mark | 标记 |
| Read / Unread | 已读 / 未读 |
| Lock / Locked / Unlocked | 锁定 / 已锁定 / 未锁定 |
| Rating | 评分 |
| Replicant / Replicate | 复制体 / 创建复制体 |
| Duplicate | 副本 / 复制 |
| Instance(s) | 实例（“Move All Instances to Trash”= 将所有复制体移到废纸篓） |
| Index / Indexed | 索引 / 已索引 |
| Import | 导入 |
| Export | 导出 |
| Item(s) / Record(s)（泛指条目） | 项目 |
| Record（表格里的一行） | 记录 |
| Document | 文稿 |
| Sheet | 表格 |
| Column | 列 |
| Formatted Note | 格式化笔记 |
| Rich Text | 富文本 |
| Plain Text | 纯文本 |
| Markdown Text | Markdown 文本 |
| Bookmark | 书签 |
| Feed | 订阅源 |
| Web Archive | 网页归档 |
| Paginated PDF | 分页 PDF |
| Annotation / Annotate | 注释 |
| Reminder | 提醒 |
| Comment（Finder/Spotlight comment） | 备注 |
| Custom Metadata | 自定义元数据 |
| Inspector(s) | 检查器 |
| Sidebar | 侧栏 |
| Navigate / Navigation | 导航 |
| Preview | 预览 |
| Widescreen | 宽屏 |
| Split / Three Panes / Columns / Cover Flow（视图） | 分割 / 三栏 / 分栏 / Cover Flow |
| Classify / Auto Classify | 归类 / 自动归类 |
| See Also | 另见 |
| Concordance | 词频 |
| Sorter | 分拣器 |
| Clip / Clipper | 剪藏 |
| Capture | 截取 |
| Download Manager | 下载管理器 |
| Sync / Sync Store / Location | 同步 / 同步存储 / 位置 |
| Trash / Empty Trash | 废纸篓 / 清空废纸篓 |
| Reading List | 阅读列表 |
| Favorites | 收藏 |
| Workspace | 工作区 |
| Verify & Repair | 校验并修复 |
| Check File Integrity | 检查文件完整性 |
| Backup & Optimize | 备份并优化 |
| Rebuild Database | 重建数据库 |
| Open Database / Close Database | 打开数据库 / 关闭数据库 |
| Database Properties | 数据库属性 |
| Chat / Chat Assistant | 聊天 / 聊天助手 |
| Transcribe / Transcription | 转录 |
| Summarize / Summary | 摘要 |
| Imprint / Imprinter | 印记 / 印记器 |
| Batch Process | 批处理 |
| Highlight | 高亮 |
| Wiki Links | Wiki 链接 |
| Item Link | 项目链接 |
| Table of Contents | 目录 |
| Encrypted Database | 加密数据库 |
| Properties | 属性 |
| Get Info / Info | 显示简介 / 简介 |
| Save / Revert to Saved | 存储 / 恢复到已存储版本 |
| Go | 前往 |
| View（菜单） | 显示 |
| Window | 窗口 |
| Settings / Preferences | 设置 |
| Full Screen | 全屏 |
| Share | 共享 |
| Print / Page Setup | 打印 / 页面设置 |
| Zoom In / Zoom Out / Actual Size | 放大 / 缩小 / 实际大小 |
| Open Externally / Open With | 在外部打开 / 打开方式 |
| Show in Finder / Reveal | 在访达中显示 / 显示 |
| Launch URL | 打开网址 |
| Scan / Scanner | 扫描 / 扫描仪 |
| Convert | 转换 |
| Merge / Split | 合并 / 拆分 |
| Move To / Put Back | 移动到 / 放回原处 |
| Consolidate / Deconsolidate | 整合（移入数据库）/ 解除整合（移出数据库） |
| Pending | 待处理 |
| Thumbnail | 缩略图 |
| Template | 模板 |
| Script | 脚本 |
| Log | 日志 |
| Register / License / Serial number | 注册 / 许可证 / 序列号 |
| Update（软件更新） | 更新 |
