import pytest

from video import subtitles as mod

CASES = [
    ('shift_time', [1.5, 0.25], 1.75, True),
    ('fps_convert', [1.0, 24, 25], 1.0416666666666667, True),
    ('overlaps', [0, 2, 1, 3], True, False),
    ('overlaps', [0, 1, 2, 3], False, False),
    ('wrap_lines', ['abcdef', 3], ['abc', 'def'], False),
    ('wrap_lines', ['', 3], [], False),
    ('strip_bom', ['\ufeffhello'], 'hello', False),
    ('resolve_style', [{'color': 'red'}, {'size': 12, 'color': 'white'}], {'size': 12, 'color': 'red'}, False),
    ('karaoke_progress', [0, 10, 4], 0.4, True),
    ('karaoke_progress', [0, 10, 12], 1.0, True),
    ('fallback_language', ['zh', ['en', 'zh'], 'en'], 'zh', False),
    ('fallback_language', ['fr', ['en', 'zh'], 'en'], 'en', False),
    ('clip_cue', [1, 5, 2, 4], [2, 4], False),
    ('clip_cue', [0, 3, 2, 4], [2, 3], False),
    ('commit_export', [[True, False]], False, False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_subtitles_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
