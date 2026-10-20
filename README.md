# DEVONthink 4 汉化

**支持最新的 DEVONthink 4.4 版本。** 为 [DEVONthink](https://www.devontechnologies.com/apps/devonthink) 4 补充的非官方简体中文界面翻译。官方只提供英文和德文。

> 这是个人制作的**非官方**汉化，与 DEVONtechnologies 无关，也未经其认可。
> 仓库只包含译文和构建脚本，不包含 DEVONthink 的程序或资源文件。
> 你需要先安装正版 DEVONthink。

语言包不改动程序本身，只在各模块中加一个 `zh-Hans.lproj` 文件夹，删掉它就能恢复英文。

## 覆盖范围

共 5,928 条界面文字，包括：
- 主菜单、对话框、侧栏、检查器、设置窗口；
- 智能群组、智能规则、批处理、脚本菜单、AI 聊天助手；
- 同步、OCR、邮件导入、剪藏/截取、小组件、印记器等插件。

暂未翻译：帮助文档、模板脚本、语言和国家名称列表，以及第三方框架（如 Sparkle 更新器）。

## 安装

需要 macOS 自带的 Python 3。在「终端」中执行：

```bash
git clone https://github.com/xbxpower/devonthink4-zh.git
cd devonthink4-zh
python3 build.py extract   # 从你电脑上的 DEVONthink 提取英文原表到 source/
python3 build.py           # 校验并生成语言包到 out/，同时生成安装脚本
```

然后双击 `安装语言包.command`。它会把语言包复制进 DEVONthink 的各个模块，把 DEVONthink 的界面语言设为简体中文，然后重新启动 DEVONthink。

- 第一次运行时，macOS 可能会询问是否允许「终端」修改其他 App，选择允许。
- 如果提示 `Operation not permitted`：打开「系统设置 ▸ 隐私与安全性 ▸ App 管理」，允许「终端」，再运行一次。
- DEVONthink 自动更新后语言包会被覆盖，重新双击 `安装语言包.command` 即可。
- 如果更新后的 DEVONthink 新增了界面文字，先重新执行上面两条 `build.py` 命令。新增的文字会暂时显示英文。

## 卸载

```bash
find /Applications/DEVONthink.app -type d -name zh-Hans.lproj -not -path '*ShortcutRecorder*' -exec rm -rf {} +
defaults delete com.devon-technologies.think AppleLanguages
```

## 参与改进译文

- `translations/<模块>/<表>.json`：中文译文。键是程序内部使用的键（通常就是英文原文），只改值即可。
- `GLOSSARY.md`：术语表与翻译规则，用来统一译法。
- 改完运行 `python3 build.py`，它会：
  - 检查 `%@`、`%d` 等占位符是否和英文一致；
  - 对没有翻译的条目自动填入英文原文（DEVONthink 遇到缺失的键会直接显示内部键名，所以每张表都必须完整）。
- 欢迎提交 Issue 或 Pull Request 指出不准确的翻译，最好附上截图。

## 说明

DEVONthink 是 DEVONtechnologies, LLC 的商标。修改已安装的应用包是否符合其许可协议，请自行判断。本项目仅供个人学习和使用。
