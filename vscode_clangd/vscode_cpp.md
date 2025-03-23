# vscode+clangd 代码补全、语法检查、调试、跳转教程
## 安装 clangd
```bash
apt-get install clangd

## 或者下载安装
wget -c https://github.com/clangd/clangd/releases/download/20.1.0/clangd-linux-20.1.0.zip
```


## 扩展设置中添加选项
```bash
--compile-commands-dir=${workspaceFolder}/build

# 或者在 vscode 中 settings.json 中添加
{
    "clangd.path": "/usr/bin/clangd",
    "clangd.arguments": [
        "--compile-commands-dir=${workspaceFolder}/command.json_path/",
        "--background-index",
        "--completion-style=detailed",
        "--header-insertion=never",
        "--log=info",
        "--pretty"
    ],
}
```
设置clangd path

```