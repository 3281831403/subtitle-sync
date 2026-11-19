"""字幕同步：时间轴、换行与样式。"""


def shift_time(timestamp, offset):
    """整体平移时间戳。"""
    return timestamp + offset


def fps_convert(timestamp, from_fps, to_fps):
    """按帧率比例换算时间戳。"""
    return timestamp * to_fps / from_fps


def overlaps(a_start, a_end, b_start, b_end):
    """两个 cue 时间区间是否重叠。"""
    return a_start < b_end and b_start < a_end


def wrap_lines(text, width):
    """按显示宽度换行。"""
    return [text[i:i + width] for i in range(0, len(text), width)]


def strip_bom(data):
    """剥离 UTF-8 BOM。"""
    return data.lstrip('﻿')


def resolve_style(child, parent):
    """字幕样式按父子继承合并。"""
    merged = dict(parent)
    merged.update(child)
    return merged


def karaoke_progress(start, end, now):
    """卡拉 OK 进度钳制到 0–1。"""
    if end <= start:
        return 1.0 if now >= end else 0.0
    return min(1.0, max(0.0, (now - start) / (end - start)))


def fallback_language(language, available, default):
    """语言不可用时回退到默认字幕。"""
    return language if language in available else default


def clip_cue(start, end, segment_start, segment_end):
    """把 cue 裁剪到片段边界。"""
    return [max(start, segment_start), min(end, segment_end)]


def commit_export(results):
    """批量导出全部成功才提交。"""
    return all(results)
