import glob
import os

files = glob.glob(r'C:\Users\yashw\Desktop\TASN  PP\TASN\*.html')
print(f'Total HTML files: {len(files)}')

for f in sorted(files):
    fname = os.path.basename(f)
    text = open(f, 'r', encoding='utf-8').read()
    has_nav = 'href="bike-rides.html"' in text and 'category-link' in text
    has_drawer = 'href="bike-rides.html"' in text and 'mobile-nav-item' in text
    has_footer = 'href="bike-rides.html"' in text and 'footer-links-list' in text
    has_modal = 'value="bike"' in text and 'enqCategorySelect' in text
    print(f'{fname:24s} | nav: {str(has_nav):5s} | drawer: {str(has_drawer):5s} | footer: {str(has_footer):5s} | modal: {str(has_modal):5s}')
