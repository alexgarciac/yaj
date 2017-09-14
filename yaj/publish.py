from misaka import Markdown, HtmlRenderer
from urllib.parse import urlparse
from pygit2 import Repository

from yaj.config import YAJ_DIR, YAJ_GIT
import yaj.kjson as kjson
import yaj.uri as uri
import yaj.fetch as fetch

def story_metadata(id):
    return kjson.loadf(YAJ_DIR+"/doc/"+id+".jsonld")

def story(content_uri):
    """Return the text referenced by content_uri. If uri can not be
    resolved it is returned as is. Current allowed scheme is 'git'. The
    netloc 'yaj-dir' resolves to the local source tree.

    """
    fullpath = uri.resolve_to_path(content_uri)
    buf = fetch.read(fullpath)
    rndr = HtmlRenderer()
    md = Markdown(rndr)
    return md(buf)
