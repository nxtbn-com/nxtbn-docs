import os
from lxml import etree

def remove_html_extension(sitemap_path, base_url):
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(sitemap_path, parser)
    root = tree.getroot()
    
    for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
        loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
        if loc is not None:
            # Remove the '/en' prefix if present
            loc.text = loc.text.replace(base_url + 'en/', base_url + '/')
            # Adjust the home page URL
            if loc.text.endswith('/index.html'):
                loc.text = base_url  # Set to base URL for home page
            elif loc.text.endswith('.html'):
                loc.text = loc.text[:-5]  # Remove the '.html' extension

    tree.write(sitemap_path, pretty_print=True, xml_declaration=True, encoding='UTF-8')

def setup(app):
    app.connect('build-finished', lambda app, exception: remove_html_extension(
        os.path.join(app.outdir, 'sitemap.xml'), 
        app.config.html_baseurl
    ))
