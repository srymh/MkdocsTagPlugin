from mkdocs.plugins import BasePlugin
from mkdocs.config.config_options import Type
# from mkdocs.utils import string_types // Deprecated
import os
import json
import urllib.parse

def _extract_meta(meta_data, data_name):
    if data_name in meta_data:
        return meta_data[data_name]
    else:
        return []


def _retrievetags(page, config):
    if config['site_url'] is None:
        url = '/' + page.file.url
    else:
        url = urllib.parse.urljoin(config['site_url'], page.file.url)
    data = {
        'title': page.title,
        'file_name': page.file.name,
        'url': url,
        'tags': _extract_meta(page.meta, 'tags'),
        'description': _extract_meta(page.meta, 'description')
    }
    return data


def _make_new_json(filepath):
    data_template = []
    with open(filepath, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(data_template, ensure_ascii=False, indent=2))


def _add_data_to(filepath, additional_data):
    if not os.path.isfile(filepath):
        _make_new_json(filepath)

    with open(filepath, mode='r', encoding='utf-8') as f:
        data = json.load(f)

    with open(filepath, mode='w', encoding='utf-8') as f:
        data.append(additional_data)
        f.write(json.dumps(data, ensure_ascii=False, indent=2))


class TagPlugin(BasePlugin):
    config_scheme = (
        ('tagpage_dir', Type(str, default='tags')),
        ('data_filename', Type(str, default='tags.json'))
    )

    def on_page_markdown(self, markdown, **kwargs):
        config = kwargs.get('config')
        page = kwargs.get('page')

        data = _retrievetags(page, config)
        filepath = os.path.join(
            config['site_dir'], self.config['data_filename'])
        _add_data_to(filepath, data)

        return markdown
