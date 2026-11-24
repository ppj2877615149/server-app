# 服务器

一个原生 iOS 应用（Capacitor + WKWebView），在局域网内远程操控一台 Android 手机的桌面。

## 它做什么

应用打开即全屏加载局域网内的手机投屏页面（ws-scrcpy）：

- 地址：`http://192.168.0.171:8000`（仅局域网，不走公网、不走 VPN）
- 视频：手机桌面 1080x2400 原分辨率全屏显示
- 控制：点按、滑动直接透传到手机
- 声音：页面内音频正常播放

## 技术

- Capacitor 8（WKWebView 壳，不重写 scrcpy 协议）
- 应用名：服务器，Bundle ID：`com.ppj.fuwuqi`
- 图标：纯色深蓝底 + 服务器机柜图形（`scripts/make_icons.py` 生成，无手机图案）
- 明文 HTTP 仅放行局域网：`Info.plist` 里 `NSAllowsLocalNetworking`，不放行任意外网

## 构建（GitHub Actions）

推送到 `main` 即在 macOS runner 上构建未签名 IPA：

1. `npm ci`
2. `npx cap sync ios`
3. `python3 scripts/make_icons.py`（生成图标与启动图）
4. `xcodebuild`（`CODE_SIGNING_ALLOWED=NO`，不签名）
5. 打包 `Payload/App.app` 为 `服务器-unsigned.ipa`，作为构建产物上传

## 安装

IPA 是未签名的，用自己的签名工具签名后安装到 iPhone 即可（无需 Apple 开发者账号）。
安装后确保 iPhone 与被控手机在同一局域网（酒店 WiFi），打开 App 即可控制。
