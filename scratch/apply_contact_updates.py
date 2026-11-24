import re
import glob

# 1. Top Bar Phone & Email Replacement
old_top_bar = '''        <div class="top-bar-item">
          <i class="fa-solid fa-phone"></i>
          <a href="tel:+919845012345">+91 98450 12345</a>
        </div>'''

new_top_bar = '''        <div class="top-bar-item">
          <i class="fa-solid fa-phone"></i>
          <a href="tel:+919482162213">+91 94821 62213</a>
          <span style="opacity: 0.6; margin: 0 4px;">/</span>
          <a href="tel:+919980239643">+91 99802 39643</a>
        </div>
        <div class="top-bar-item">
          <i class="fa-solid fa-envelope"></i>
          <a href="mailto:prashantiparyatana26@gmail.com">prashantiparyatana26@gmail.com</a>
        </div>'''

# 2. Footers in secondary pages
old_footer_helpdesk = '''          <div class="footer-contact-item">
            <i class="fa-solid fa-phone"></i>
            <div>+91 98450 12345 / +91 80 2345 6789</div>
          </div>
          <div class="footer-contact-item">
            <i class="fa-solid fa-envelope"></i>
            <div>yatra@prashantiparyatana.org</div>
          </div>'''

new_footer_helpdesk = '''          <div class="footer-contact-item">
            <i class="fa-solid fa-phone"></i>
            <div>
              <a href="tel:+919482162213" style="color: inherit; text-decoration: none;">+91 94821 62213</a><br />
              <a href="tel:+919980239643" style="color: inherit; text-decoration: none;">+91 99802 39643</a>
            </div>
          </div>
          <div class="footer-contact-item">
            <i class="fa-solid fa-envelope"></i>
            <div>
              <a href="mailto:prashantiparyatana26@gmail.com" style="color: inherit; text-decoration: none;">prashantiparyatana26@gmail.com</a>
            </div>
          </div>'''

# 3. Footer in index.html
old_index_footer = '''          <div class="footer-contact-item">
            <i class="fa-solid fa-phone"></i>
            <div>
              <strong>Direct Yatra Line:</strong><br />
              +91 98450 12345 / +91 80 2345 6789
            </div>
          </div>
          <div class="footer-contact-item">
            <i class="fa-solid fa-envelope"></i>
            <div>
              <strong>Sacred Inquiries:</strong><br />
              yatra@prashantiparyatana.org
            </div>
          </div>'''

new_index_footer = '''          <div class="footer-contact-item">
            <i class="fa-solid fa-phone"></i>
            <div>
              <strong>Direct Yatra Lines:</strong><br />
              <a href="tel:+919482162213" style="color: inherit; text-decoration: none;">+91 94821 62213</a> / 
              <a href="tel:+919980239643" style="color: inherit; text-decoration: none;">+91 99802 39643</a>
            </div>
          </div>
          <div class="footer-contact-item">
            <i class="fa-solid fa-envelope"></i>
            <div>
              <strong>Sacred Inquiries:</strong><br />
              <a href="mailto:prashantiparyatana26@gmail.com" style="color: inherit; text-decoration: none;">prashantiparyatana26@gmail.com</a>
            </div>
          </div>'''

# 4. Modal Contact Bar (added to modal-body right above the form container)
old_modal_target = '''      <div class="modal-body">
        <div id="enquiryFormContainer">'''

new_modal_replacement = '''      <div class="modal-body">
        <!-- Direct Quick Contact Pill -->
        <div class="modal-quick-contact" style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem; background: var(--color-sandalwood-light); border: 1px solid var(--color-gold); border-radius: var(--radius-sm); padding: 0.6rem 0.9rem; margin-bottom: 1.2rem; font-size: 0.82rem;">
          <div style="display: flex; align-items: center; gap: 0.4rem;">
            <i class="fa-solid fa-phone" style="color: var(--color-saffron);"></i>
            <span style="font-weight: 600; color: var(--color-maroon);">Call:</span>
            <a href="tel:+919482162213" style="color: var(--color-maroon); font-weight: 700; text-decoration: none;">+91 94821 62213</a>
            <span style="opacity: 0.5;">/</span>
            <a href="tel:+919980239643" style="color: var(--color-maroon); font-weight: 700; text-decoration: none;">+91 99802 39643</a>
          </div>
          <div style="display: flex; align-items: center; gap: 0.4rem;">
            <i class="fa-solid fa-envelope" style="color: var(--color-saffron);"></i>
            <a href="mailto:prashantiparyatana26@gmail.com" style="color: var(--color-maroon); font-weight: 600; text-decoration: none;">prashantiparyatana26@gmail.com</a>
          </div>
        </div>
        <div id="enquiryFormContainer">'''

# Process all HTML files
html_files = glob.glob('C:/Users/yashw/Desktop/TASN  PP/TASN/*.html')
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    modified = False

    # Top bar
    if old_top_bar in content:
        content = content.replace(old_top_bar, new_top_bar)
        modified = True
    
    # Secondary footers
    if old_footer_helpdesk in content:
        content = content.replace(old_footer_helpdesk, new_footer_helpdesk)
        modified = True

    # Index footer
    if old_index_footer in content:
        content = content.replace(old_index_footer, new_index_footer)
        modified = True

    # Modal contact pill
    if old_modal_target in content and 'modal-quick-contact' not in content:
        content = content.replace(old_modal_target, new_modal_replacement)
        modified = True

    # Replace old placeholder +91 98450 12345 in phone inputs
    if 'placeholder="+91 98450 12345"' in content:
        content = content.replace('placeholder="+91 98450 12345"', 'placeholder="+91 94821 62213 / 9980239643"')
        modified = True

    if modified:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {fpath}")

print("HTML batch updates complete!")
