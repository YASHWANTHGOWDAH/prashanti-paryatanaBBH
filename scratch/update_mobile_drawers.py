import re
import glob

drawer_contact = '''      <div class="mobile-drawer-contact" style="margin-top: 1.25rem; padding-top: 1.1rem; border-top: 1px solid var(--color-sandalwood-border); font-size: 0.85rem;">
        <div style="font-weight: 700; color: var(--color-maroon); margin-bottom: 0.4rem; font-family: var(--font-heading); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em;">
          <i class="fa-solid fa-phone" style="color: var(--color-saffron); margin-right: 0.3rem;"></i> Direct Pilgrimage Lines
        </div>
        <div style="display: flex; flex-direction: column; gap: 0.35rem; margin-bottom: 0.75rem;">
          <a href="tel:+919482162213" style="color: var(--color-maroon); font-weight: 700; text-decoration: none;">+91 94821 62213</a>
          <a href="tel:+919980239643" style="color: var(--color-maroon); font-weight: 700; text-decoration: none;">+91 99802 39643</a>
        </div>
        <div style="font-weight: 700; color: var(--color-maroon); margin-bottom: 0.25rem; font-family: var(--font-heading); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em;">
          <i class="fa-solid fa-envelope" style="color: var(--color-saffron); margin-right: 0.3rem;"></i> Email Assistance
        </div>
        <a href="mailto:prashantiparyatana26@gmail.com" style="color: var(--color-saffron); font-weight: 600; text-decoration: none; word-break: break-all;">prashantiparyatana26@gmail.com</a>
      </div>'''

html_files = glob.glob('C:/Users/yashw/Desktop/TASN  PP/TASN/*.html')
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if 'mobile-drawer-contact' in content:
        continue

    # Find the end of mobile drawer content before </div>\n  </div>
    # Pattern: matching the plan journey button in mobile drawer
    m = re.search(r'(<button type="button" class="btn-plan-journey"[^>]*>.*?</button>\s*</div>\s*</div>)', content, re.DOTALL)
    if m:
        old_block = m.group(1)
        # We want to insert drawer_contact right before </div>\s*</div>
        new_block = re.sub(r'(\s*</div>\s*</div>)$', '\n' + drawer_contact + r'\1', old_block)
        content = content.replace(old_block, new_block, 1)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added mobile drawer contact to: {fpath}")

print("Mobile drawer updates complete!")
