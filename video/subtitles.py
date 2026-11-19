"""字幕同步：时间轴、换行与样式：待实现的核心模块。"""


def shift_time(timestamp, offset):
    """整体平移时间戳。"""
    raise NotImplementedError

def fps_convert(timestamp, from_fps, to_fps):
    """按帧率比例换算时间戳。"""
    raise NotImplementedError

def overlaps(a_start, a_end, b_start, b_end):
    """两个 cue 时间区间是否重叠。"""
    raise NotImplementedError

def wrap_lines(text, width):
    """按显示宽度换行。"""
    raise NotImplementedError

def strip_bom(data):
    """剥离 UTF-8 BOM。"""
    raise NotImplementedError

def resolve_style(child, parent):
    """字幕样式按父子继承合并。"""
    raise NotImplementedError

def karaoke_progress(start, end, now):
    """卡拉 OK 进度钳制到 0–1。"""
    raise NotImplementedError

def fallback_language(language, available, default):
    """语言不可用时回退到默认字幕。"""
    raise NotImplementedError

def clip_cue(start, end, segment_start, segment_end):
    """把 cue 裁剪到片段边界。"""
    raise NotImplementedError

def commit_export(results):
    """批量导出全部成功才提交。"""
    raise NotImplementedError
