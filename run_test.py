import pytest


# 启动文件
if __name__ == '__main__':
    pytest.main(['-s', './script/test_login.py', '--html=./report/report.html'])
