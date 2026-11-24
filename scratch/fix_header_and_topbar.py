import re
import glob

# Pattern to remove mobile-drawer-contact from nav-actions
nav_action_contact_pattern = re.compile(
    r'\s*<div class="mobile-drawer-contact".*?</div>(?=\s*</div>\s*</div>\s*</header>)',
    re.DOTALL
)

# New clean horizontal top-bar-left
clean_top_bar_left = '''      <div class="top-bar-left">
        <div class="top-bar-item">
          <i class="fa-solid fa-om"></i>
          <span class="font-sanskrit-style">॥ सनातन संस्कृति यात्रा ॥</span>
        </div>
        <div class="top-bar-item">
          <i class="fa-solid fa-phone"></i>
          <a href="tel:+919482162213" style="color: inherit; text-decoration: none; font-weight: 600;">+91 94821 62213</a>
          <span style="opacity: 0.5; margin: 0 4px;">/</span>
          <a href="tel:+919980239643" style="color: inherit; text-decoration: none; font-weight: 600;">+91 99802 39643</a>
        </div>
        <div class="top-bar-item">
          <i class="fa-solid fa-envelope"></i>
          <a href="mailto:prashantiparyatana26@gmail.com" style="color: inherit; text-decoration: none;">prashantiparyatana26@gmail.com</a>
        </div>
      </div>'''

# Match whatever top-bar-left currently has
current_top_bar_left_pattern = re.compile(
    r'\s*<div class="top-bar-left">.*?</div>\s*(?=<div class="top-bar-right">)',
    re.DOTALL
)

for fpath in glob.glob('C:/Users/yashw/Desktop/TASN  PP/TASN/*.html'):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Remove marked part from main header (nav-actions)
    content = nav_action_contact_pattern.sub('', content)

    # 2. Update top-bar-left to clean horizontal contact bar
    if current_top_bar_left_pattern.search(content):
        content = current_top_bar_left_pattern.sub('\n' + clean_top_bar_left + '\n      ', content)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed: {fpath}")

print("All headers and top bars updated!")
