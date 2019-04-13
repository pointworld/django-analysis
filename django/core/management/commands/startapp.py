## 根据命令行给定的参数创建一个 Django 应用目录结构

from django.core.management.templates import TemplateCommand


class Command(TemplateCommand):
    help = (
        "Creates a Django app directory structure for the given app name in "
        "the current directory or optionally in the given directory."
    )
    missing_args_message = "You must provide an application name."

    def handle(self, **options):
        ## 应用名
        app_name = options.pop('name')
        ## 存放目录
        target = options.pop('directory')
        super().handle('app', app_name, target, **options)
