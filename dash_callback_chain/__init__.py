import os as _os
import dash as _dash
import sys as _sys
from .version import __version__

_current_path = _os.path.dirname(_os.path.abspath(__file__))

_components = _dash.development.component_loader.load_components(
    _os.path.join(_current_path, 'metadata.json'),
    'dash_callback_chain'
)

_this_module = _sys.modules[__name__]


_js_dist = [
    {
        "relative_package_path": "bundle.js",
        "external_url": (
            "https://unpkg.com/dash-callback-chain@{}"
            "/dash_callback_chain/bundle.js"
        ).format(__version__),
        "namespace": "dash_callback_chain"
    }
]

_css_dist = []


for _component in _components:
    setattr(_this_module, _component.__name__, _component)
    setattr(_component, '_js_dist', _js_dist)
    setattr(_component, '_css_dist', _css_dist)


from collections import defaultdict
def dot_chain(app, excluded_callbacks = []):
    output_list = []
    clusters = defaultdict(set)

    for callback_id, callback in app.callback_map.items():
        wrapped_func = callback['callback'].__wrapped__
        callback_name = wrapped_func.__name__
        if callback_name in excluded_callbacks: continue
        split_list = callback_id.split(".")
        for output, output_prop in zip(split_list[0::2], split_list[1::2]):
            if output != "" and output_prop != "":
                clusters[output].add(output_prop)
                output_list.append('"%s" [shape=octagon];' % callback_name)
                output_list.append('"%s" -> "%s.%s";' %
                    (callback_name, output, output_prop))
        for i in callback['inputs']:
            clusters[i['id']].add(i['property'])
            output_list.append('"%s.%s" -> "%s";' %
                (i['id'], i['property'], callback_name))

    for i, c in enumerate(clusters):
        output_list.append('subgraph cluster_%s {' %i)
        output_list.append('  label = "%s";' % c)
        for p in clusters[c]:
            output_list.append('  "%s.%s" [label = "%s"];' % (c,p,p))
        output_list.append('};')

    return "\n".join(output_list)
