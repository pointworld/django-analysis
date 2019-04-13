# Django 源码解读

## 项目结构

```text
.
├── __init__.py
├── __main__.py
├── apps
│   ├── __init__.py
│   ├── config.py
│   └── registry.py
├── bin
│   └── django-admin.py
├── conf                                    ## 配置
│   ├── __init__.py
│   ├── app_template
│   ├── global_settings.py                  ## Django 默认全局配置
│   ├── locale
│   ├── project_template
│   └── urls
├── contrib
│   ├── __init__.py
│   ├── admin                               ## 管理员站点
│   ├── admindocs
│   ├── auth                                ## 认证授权系统
│   ├── contenttypes                        ## 内容类型框架
│   ├── flatpages
│   ├── gis
│   ├── humanize
│   ├── messages                            ## 消息框架
│   ├── postgres
│   ├── redirects
│   ├── sessions                            ## 会话框架    
│   ├── sitemaps
│   ├── sites
│   ├── staticfiles                         ## 管理静态文件的框架
│   └── syndication
├── core
│   ├── __init__.py
│   ├── cache
│   ├── checks
│   ├── exceptions.py
│   ├── files
│   ├── handlers
│   ├── mail
│   ├── management
│   ├── paginator.py
│   ├── serializers
│   ├── servers
│   ├── signals.py
│   ├── signing.py
│   ├── validators.py
│   └── wsgi.py
├── db
│   ├── __init__.py
│   ├── backends
│   ├── migrations
│   ├── models
│   ├── transaction.py
│   └── utils.py
├── dispatch
│   ├── __init__.py
│   ├── dispatcher.py
│   └── license.txt
├── forms
│   ├── __init__.py
│   ├── boundfield.py
│   ├── fields.py
│   ├── forms.py
│   ├── formsets.py
│   ├── jinja2
│   ├── models.py
│   ├── renderers.py
│   ├── templates
│   ├── utils.py
│   └── widgets.py
├── http
│   ├── __init__.py
│   ├── cookie.py
│   ├── multipartparser.py
│   ├── request.py
│   └── response.py
├── middleware
│   ├── __init__.py
│   ├── cache.py
│   ├── clickjacking.py
│   ├── common.py
│   ├── csrf.py
│   ├── gzip.py
│   ├── http.py
│   ├── locale.py
│   └── security.py
├── shortcuts.py
├── template
│   ├── __init__.py
│   ├── backends
│   ├── base.py
│   ├── context.py
│   ├── context_processors.py
│   ├── defaultfilters.py
│   ├── defaulttags.py
│   ├── engine.py
│   ├── exceptions.py
│   ├── library.py
│   ├── loader.py
│   ├── loader_tags.py
│   ├── loaders
│   ├── response.py
│   ├── smartif.py
│   └── utils.py
├── templatetags
│   ├── __init__.py
│   ├── cache.py
│   ├── i18n.py
│   ├── l10n.py
│   ├── static.py
│   └── tz.py
├── test
│   ├── __init__.py
│   ├── client.py
│   ├── html.py
│   ├── runner.py
│   ├── selenium.py
│   ├── signals.py
│   ├── testcases.py
│   └── utils.py
├── urls
│   ├── __init__.py
│   ├── base.py
│   ├── conf.py
│   ├── converters.py
│   ├── exceptions.py
│   ├── resolvers.py
│   └── utils.py
├── utils
│   ├── __init__.py
│   ├── _os.py
│   ├── archive.py
│   ├── autoreload.py
│   ├── baseconv.py
│   ├── cache.py
│   ├── crypto.py
│   ├── datastructures.py
│   ├── dateformat.py
│   ├── dateparse.py
│   ├── dates.py
│   ├── datetime_safe.py
│   ├── deconstruct.py
│   ├── decorators.py
│   ├── deprecation.py
│   ├── duration.py
│   ├── encoding.py
│   ├── feedgenerator.py
│   ├── formats.py
│   ├── functional.py
│   ├── hashable.py
│   ├── html.py
│   ├── http.py
│   ├── inspect.py
│   ├── ipv6.py
│   ├── itercompat.py
│   ├── jslex.py
│   ├── log.py
│   ├── lorem_ipsum.py
│   ├── module_loading.py
│   ├── numberformat.py
│   ├── regex_helper.py
│   ├── safestring.py
│   ├── termcolors.py
│   ├── text.py
│   ├── timesince.py
│   ├── timezone.py
│   ├── topological_sort.py
│   ├── translation
│   ├── tree.py
│   ├── version.py
│   └── xmlutils.py
└── views
    ├── __init__.py
    ├── csrf.py
    ├── debug.py
    ├── decorators
    ├── defaults.py
    ├── generic
    ├── i18n.py
    ├── static.py
    └── templates
```
