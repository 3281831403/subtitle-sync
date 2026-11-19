# 字幕同步：时间轴、换行与样式

字幕在不同片源上越播越偏：时间戳没有整体偏移，帧率转换按秒硬算，重叠 cue 不合并，换行不按宽度，BOM 没剥离，样式继承丢失，卡拉 OK 进度越界，语言回退错，cue 没裁到片段边界，批量导出只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
video/__init__.py
video/subtitles.py
tests/test_subtitles.py
```

## 当前状态

`video/subtitles.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_subtitles.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 时间戳整体偏移
2. 帧率转换按比例换算
3. 重叠 cue 检测与合并
4. 按显示宽度换行
5. 剥离 UTF-8 BOM
6. 字幕样式按父子继承
7. 卡拉 OK 进度钳制
8. 语言回退到可用字幕
9. cue 裁剪到片段边界
10. 批量导出统一提交

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `video/subtitles.py`
后 15 条用例应全部通过。
