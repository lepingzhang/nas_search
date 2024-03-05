# wechat-gptbot 搜索NAS插件

本项目作为 `wechat-gptbot` 插件，可以根据关键字查找NAS文件。

## 安装指南

### 1. 添加插件源
在 `plugins/source.json` 文件中添加以下配置：
```
{
  "news_hub": {
    "repo": "https://github.com/lepingzhang/nas_search.git",
    "desc": "发送特定关键词查找NAS文件"
  }
}
```

### 2. Windows建立NAS映射
将映射的盘符如`A`、`B`、`C`填入`config`中。

### 3. 插件配置
在 `config.json` 文件中添加以下配置：
```
"plugins": [
  {
    "name": "nas_search",
    "command": ["搜索nas", "查找nas"],
    "drives": {
      "D": "盘符名称"
    },
    "base_path": "\\\\192.168.50.147\\"
  }
]
```
