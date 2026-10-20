#!/bin/zsh
# 双击运行：把中文语言包装进 DEVONthink 的各个模块，并重新启动 DEVONthink。
# DEVONthink 自动更新后语言包会被覆盖，再双击一次即可。由 build.py 生成。
cd "$(dirname "$0")"
APP="/Applications/DEVONthink.app/Contents"
ok=0; fail=0
install() {
  if [ -d "out/$1/zh-Hans.lproj" ] && [ -d "$APP/$2" ]; then
    rm -rf "$APP/$2/zh-Hans.lproj"
    if cp -R "out/$1/zh-Hans.lproj" "$APP/$2/zh-Hans.lproj"; then ok=$((ok+1)); else fail=$((fail+1)); fi
  fi
}
install "app" "Resources"
install "appkit" "Frameworks/DEVONappkit.framework/Versions/A/Resources"
install "pdfkit" "Frameworks/DEVONpdfkit.framework/Versions/A/Resources"
install "webkit" "Frameworks/DEVONwebkit.framework/Versions/A/Resources"
install "scanner" "PlugIns/DTScannerPlugin.bundle/Contents/Resources"
install "sync-pane" "PlugIns/Cloudy.prefPane/Contents/Resources"
install "sync-bundle" "PlugIns/Cloudy.bundle/Contents/Resources"
install "ocr-pane" "PlugIns/DTOCRPrefPane.prefPane/Contents/Resources"
install "ocr-plugin" "PlugIns/DTOCRPlugin.bundle/Contents/Resources"
install "mail" "PlugIns/MailImport4.bundle/Contents/Resources"
install "capture-bundle" "PlugIns/DTUnifiedCapture.bundle/Contents/Resources"
install "capture-pane" "PlugIns/DTUCPrefPane.prefPane/Contents/Resources"
install "widgets" "PlugIns/DEVONthinkWidgetsExtension.appex/Contents/Resources"
install "imprinter-pane" "PlugIns/Imprinter.prefPane/Contents/Resources"
install "imprinter" "PlugIns/Imprinter.bundle/Contents/Resources"
install "addressbook" "PlugIns/ImportAddressbook.bundle/Contents/Resources"
install "mcp" "Library/LoginItems/DEVONthink MCP.app/Contents/Resources"
install "sharing" "PlugIns/DEVONthink Sharing.appex/Contents/Resources"
install "webserver" "PlugIns/WebServer4.bundle/Contents/Resources"
install "sharebymail" "PlugIns/ShareByMail.bundle/Contents/Resources"
install "exportsite" "PlugIns/ExportSite.bundle/Contents/Resources"
install "exportfiles" "PlugIns/ExportFiles.bundle/Contents/Resources"
install "importdata" "PlugIns/ImportData.bundle/Contents/Resources"
install "scansnap" "PlugIns/DTScansnap.bundle/Contents/Resources"
install "scansnap-support" "PlugIns/ScanSnapSupport.bundle/Contents/Resources"
install "get-xpc" "XPCServices/com.devon-technologies.get.xpc/Contents/Resources"
install "spotlight" "Library/Spotlight/DEVONthink Spotter.mdimporter/Contents/Resources"
echo
echo "✅ 已安装 $ok 个模块的语言包"
[ $fail -gt 0 ] && echo "❌ $fail 个模块复制失败。若提示 Operation not permitted：打开 系统设置 ▸ 隐私与安全性 ▸ App 管理，允许“终端”，再双击本脚本。"
defaults write com.devon-technologies.think AppleLanguages -array zh-Hans en
if pgrep -xq DEVONthink; then
  echo "正在退出 DEVONthink …"
  osascript -e 'tell application id "com.devon-technologies.think" to quit' >/dev/null 2>&1
  for i in {1..30}; do pgrep -xq DEVONthink || break; sleep 1; done
fi
open "/Applications/DEVONthink.app"
read -k 1 "?完成。按任意键关闭此窗口…"
