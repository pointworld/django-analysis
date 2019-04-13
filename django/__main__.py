"""
Invokes django-admin when the django module is run as a script.
## 当 django 模块被作为一个脚本执行时，调用 django-admin 命令

Example: python -m django check
"""
from django.core import management

if __name__ == "__main__":
    ## 从命令行执行
    management.execute_from_command_line()
