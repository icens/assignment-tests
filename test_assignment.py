import pytest
from student_assignment import add  # 假設學生的作業會提交一個 add 函數

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
