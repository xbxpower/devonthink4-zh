#!/usr/bin/env python3
"""DEVONthink 简体中文语言包：提取、构建、生成安装脚本。

目录结构
  source/<模块>/<表>.json        从 DEVONthink.app 提取的英文原表（键 = 内部键，值 = 英文）
  translations/<模块>/<表>.json  中文译文（键 = 内部键，值 = 中文）
  out/<模块>/zh-Hans.lproj/      生成的 .strings，安装脚本把它们复制到各模块里

规则
  - 同一张表里缺的键会自动填英文原文：DEVONthink 对缺键会直接显示内部键名（如 "openDatabases"），
    所以每张表都要完整。
  - %@ %d 等占位符必须与英文一致，不一致的条目会被跳过并报告。

用法
  python3 build.py extract   提取英文原表到 source/
  python3 build.py           构建到 out/ 并重新生成 安装语言包.command
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
APP = "/Applications/DEVONthink.app/Contents"

# 模块 id → 该模块 en.lproj 相对 Contents 的路径
MODULES = {
    "app": "Resources",
    "appkit": "Frameworks/DEVONappkit.framework/Versions/A/Resources",
    "pdfkit": "Frameworks/DEVONpdfkit.framework/Versions/A/Resources",
    "webkit": "Frameworks/DEVONwebkit.framework/Versions/A/Resources",
    "scanner": "PlugIns/DTScannerPlugin.bundle/Contents/Resources",
    "sync-pane": "PlugIns/Cloudy.prefPane/Contents/Resources",
    "sync-bundle": "PlugIns/Cloudy.bundle/Contents/Resources",
    "ocr-pane": "PlugIns/DTOCRPrefPane.prefPane/Contents/Resources",
    "ocr-plugin": "PlugIns/DTOCRPlugin.bundle/Contents/Resources",
    "mail": "PlugIns/MailImport4.bundle/Contents/Resources",
    "capture-bundle": "PlugIns/DTUnifiedCapture.bundle/Contents/Resources",
    "capture-pane": "PlugIns/DTUCPrefPane.prefPane/Contents/Resources",
    "widgets": "PlugIns/DEVONthinkWidgetsExtension.appex/Contents/Resources",
    "imprinter-pane": "PlugIns/Imprinter.prefPane/Contents/Resources",
    "imprinter": "PlugIns/Imprinter.bundle/Contents/Resources",
    "addressbook": "PlugIns/ImportAddressbook.bundle/Contents/Resources",
    "mcp": "Library/LoginItems/DEVONthink MCP.app/Contents/Resources",
    "sharing": "PlugIns/DEVONthink Sharing.appex/Contents/Resources",
    "webserver": "PlugIns/WebServer4.bundle/Contents/Resources",
    "sharebymail": "PlugIns/ShareByMail.bundle/Contents/Resources",
    "exportsite": "PlugIns/ExportSite.bundle/Contents/Resources",
    "exportfiles": "PlugIns/ExportFiles.bundle/Contents/Resources",
    "importdata": "PlugIns/ImportData.bundle/Contents/Resources",
    "scansnap": "PlugIns/DTScansnap.bundle/Contents/Resources",
    "scansnap-support": "PlugIns/ScanSnapSupport.bundle/Contents/Resources",
    "get-xpc": "XPCServices/com.devon-technologies.get.xpc/Contents/Resources",
    "spotlight": "Library/Spotlight/DEVONthink Spotter.mdimporter/Contents/Resources",
}
# 纯语言/国家名列表，暂不翻译
SKIP_TABLES = {"Languages", "Countries", "OCRLanguages"}

PLACEHOLDER = re.compile(r"%(\d+\$)?(l{1,2}|h|z|q)?[@dDiuUxXoOfeEgGcCsSpaAF]|%\.\d+[fg]")


def read_strings(path):
    out = subprocess.run(["plutil", "-convert", "json", "-o", "-", path], capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\t", "\\t")


def extract():
    total = 0
    for mod, rel in MODULES.items():
        en_dir = os.path.join(APP, rel, "en.lproj")
        if not os.path.isdir(en_dir):
            continue
        for f in sorted(os.listdir(en_dir)):
            if not f.endswith(".strings") or f[:-8] in SKIP_TABLES:
                continue
            data = read_strings(os.path.join(en_dir, f))
            if not data:
                continue
            dest = os.path.join(HERE, "source", mod)
            os.makedirs(dest, exist_ok=True)
            with open(os.path.join(dest, f[:-8] + ".json"), "w", encoding="utf-8") as o:
                json.dump(data, o, ensure_ascii=False, indent=1)
            print(f"{mod}/{f}: {len(data)}")
            total += len(data)
    print(f"共 {total} 条")


def build():
    out_root = os.path.join(HERE, "out")
    total = translated = problems = 0
    for mod in MODULES:
        src_dir = os.path.join(HERE, "source", mod)
        if not os.path.isdir(src_dir):
            continue
        out_dir = os.path.join(out_root, mod, "zh-Hans.lproj")
        os.makedirs(out_dir, exist_ok=True)
        for f in sorted(os.listdir(src_dir)):
            table = f[:-5]
            en = json.load(open(os.path.join(src_dir, f), encoding="utf-8"))
            zh_path = os.path.join(HERE, "translations", mod, f)
            zh = json.load(open(zh_path, encoding="utf-8")) if os.path.exists(zh_path) else {}
            lines, done = [], 0
            for key, en_value in en.items():
                value = zh.get(key)
                if value is None or not str(value).strip():
                    value = en_value
                elif sorted(PLACEHOLDER.findall(en_value)) != sorted(PLACEHOLDER.findall(value)):
                    print(f"[{mod}/{table}] 占位符不一致，改用英文：{key!r} -> {value!r}")
                    problems += 1
                    value = en_value
                else:
                    done += 1
                lines.append(f'"{escape(key)}" = "{escape(value)}";')
            for key in zh:
                if key not in en:
                    print(f"[{mod}/{table}] 译文里有英文表没有的键，已忽略：{key!r}")
                    problems += 1
            path = os.path.join(out_dir, table + ".strings")
            with open(path, "w", encoding="utf-8") as o:
                o.write("\n".join(lines) + "\n")
            subprocess.run(["plutil", "-lint", path], check=True, capture_output=True)
            total += len(en)
            translated += done
            if done < len(en):
                print(f"{mod}/{table}: {done}/{len(en)} 已翻译")
    print(f"共 {total} 条，已翻译 {translated} 条（{translated * 100 // max(total, 1)}%），问题 {problems} 处")
    write_installer()


def write_installer():
    lines = ["#!/bin/zsh",
             "# 双击运行：把中文语言包装进 DEVONthink 的各个模块，并重新启动 DEVONthink。",
             "# DEVONthink 自动更新后语言包会被覆盖，再双击一次即可。由 build.py 生成。",
             'cd "$(dirname "$0")"',
             'APP="/Applications/DEVONthink.app/Contents"',
             "ok=0; fail=0",
             "install() {",
             '  if [ -d "out/$1/zh-Hans.lproj" ] && [ -d "$APP/$2" ]; then',
             '    rm -rf "$APP/$2/zh-Hans.lproj"',
             '    if cp -R "out/$1/zh-Hans.lproj" "$APP/$2/zh-Hans.lproj"; then ok=$((ok+1)); else fail=$((fail+1)); fi',
             "  fi",
             "}"]
    for mod, rel in MODULES.items():
        lines.append(f'install "{mod}" "{rel}"')
    lines += ["echo",
              'echo "✅ 已安装 $ok 个模块的语言包"',
              '[ $fail -gt 0 ] && echo "❌ $fail 个模块复制失败。若提示 Operation not permitted：打开 系统设置 ▸ 隐私与安全性 ▸ App 管理，允许“终端”，再双击本脚本。"',
              "defaults write com.devon-technologies.think AppleLanguages -array zh-Hans en",
              "if pgrep -xq DEVONthink; then",
              '  echo "正在退出 DEVONthink …"',
              "  osascript -e 'tell application id \"com.devon-technologies.think\" to quit' >/dev/null 2>&1",
              "  for i in {1..30}; do pgrep -xq DEVONthink || break; sleep 1; done",
              "fi",
              'open "/Applications/DEVONthink.app"',
              'read -k 1 "?完成。按任意键关闭此窗口…"']
    path = os.path.join(HERE, "安装语言包.command")
    with open(path, "w", encoding="utf-8") as o:
        o.write("\n".join(lines) + "\n")
    os.chmod(path, 0o755)


if __name__ == "__main__":
    if "extract" in sys.argv:
        extract()
    else:
        build()
