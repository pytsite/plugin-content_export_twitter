"""PytSite Twitter Content Export Plugin
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load():
    from pytsite import lang
    from plugins import content_export
    from . import _driver

    # Resources
    lang.register_package(__name__)

    # Content export driver
    content_export.register_driver(_driver.Driver())
