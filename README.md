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
将映射的盘符如`A`、`B`、`C`部分，修改为你的实际盘符。

### 3. 插件配置
在 `config.json` 文件中添加以下配置：
```
"plugins": [
  {
    "name": "nas_search",
    "command": ["搜索NAS：", "查找NAS："],
    "drives": {
      "A": "映射的文件夹名称",
      "B": "映射的文件夹名称",
      "C": "映射的文件夹名称"
    },
    "base_path": "\\\\你的IP地址，输出的可以直接通过资源管理器访问\\"
  }
]
```
