from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('jasny_bootstrap', 'resources')

# Define the resources in the library like this.
# For options and examples, see the fanstatic documentation.
# resource1 = Resource(library, 'style.css')

jasny_bootstrap = Resource(
    library, 'js/jasny-bootstrap.js',
    depends=[jquery],
    minified='js/jasny-bootstrap.min.js'
)
