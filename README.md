# mdoctag

## Get Started

``` bash
$ pipenv install mkdocs
$ pipenv install git+https://github.com/srymh/MkdocsTagPlugin.git#egg=mdoctag
```

add mdoctag to plugins

``` yaml
plugins:
    - mdoctag
```

add meta data 'tags' to your markdown files

```
---
tags:
    - tag1
    - tag2
---

# sample markdown file

hello mkdocs

```

This plugin just make a json file that contains meta data "tags".
To display aggregation of tag, you need to make pages referencing the json file.  
There is example custom theme at [repo]().
You can use this.

make tagpages markdown file

- need to add meta data (key: 'pagetype', value: 'tagpage')
- put on for tagpages directory
    + default: `site_dir/tags/`
    + `site_dir`: config of mkdocs.yml
    + can change directory by option `tagpage_dir`

```
---
pagetype: tagpage
---

# Tag: tag1

```

```
---
pagetype: tagpage
---

# Tag: tag2

```

## Options

### Directory

Select directory to put tag pages

``` yaml
plugins:
    - mdoctag:
        tagpage_dir: 'hoge' # default: 'tags'
```

You need to put tagpages in `site_dir/hoge/` directory

### Json data file name

``` yaml
plugins:
    - mdoctag:
        data_filename: 'foo.json' # default: 'tags.json'
```

`site_dir/foo.json` is genereated

*can't specify directory*

## Custom Theme

To check mdoctag is registerd to plugins in mkdocs.yml, write:

``` html
{% if 'mdoctag' in config.plugins %}
    {% include "tags.html"%}
{% endif %}
```

To get the value of `tagpage_dir`, write:

``` html
{{ config.plugins['mdoctag'].config['tagpage_dir'] }} 
```
