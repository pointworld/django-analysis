## 根据命令行参数创建一个 Django 项目目录结构

from django.core.management.templates import TemplateCommand

from ..utils import get_random_secret_key


class Command(TemplateCommand):
    help = (
        "Creates a Django project directory structure for the given project "
        "name in the current directory or optionally in the given directory."
    )
    missing_args_message = "You must provide a project name."

    def handle(self, **options):
        ## 项目名
        project_name = options.pop('name')
        ## 项目目录
        target = options.pop('directory')

        # Create a random SECRET_KEY to put it in the main settings.
        ## 创建一个随机密钥，用于放入主 settings 中
        options['secret_key'] = get_random_secret_key()

        super().handle('project', project_name, target, **options)
