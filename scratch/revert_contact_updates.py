import re
import glob

# 1. Top bar
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

orig_top_bar = '''        <div class="top-bar-item">
          <i class="fa-solid fa-phone"></i>
          <a href="tel:+919845012345">+91 98450 12345</a>
        </div>'''

# 2. Footers in secondary pages
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

orig_footer_helpdesk = '''          <div class="footer-contact-item">
            <i class="fa-solid fa-phone"></i>
            <div>+91 98450 12345 / +91 80 2345 6789</div>
          </div>
          <div class="footer-contact-item">
            <i class="fa-solid fa-envelope"></i>
            <div>yatra@prashantiparyatana.org</div>
          </div>'''

# 3. Footer in index.html
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

orig_index_footer = '''          <div class="footer-contact-item">
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

# 4. contact.html contact block
new_contact_section = '''          <div style="display: flex; gap: 1rem; align-items: flex-start;">
            <div class="why-us-icon" style="width: 44px; height: 44px; font-size: 1.1rem; flex-shrink: 0;"><i class="fa-solid fa-phone"></i></div>
            <div>
              <h4 style="font-size: 1rem; color: var(--color-maroon); margin-bottom: 0.2rem;">Telephone & WhatsApp:</h4>
              <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">
                <strong>Primary Yatra Line:</strong> <a href="tel:+919482162213" style="color: var(--color-saffron); font-weight: 700; text-decoration: none;">+91 94821 62213</a><br />
                <strong>Secondary Support Line:</strong> <a href="tel:+919980239643" style="color: var(--color-saffron); font-weight: 700; text-decoration: none;">+91 99802 39643</a>
              </p>
            </div>
          </div>

          <div style="display: flex; gap: 1rem; align-items: flex-start;">
            <div class="why-us-icon" style="width: 44px; height: 44px; font-size: 1.1rem; flex-shrink: 0;"><i class="fa-solid fa-envelope"></i></div>
            <div>
              <h4 style="font-size: 1rem; color: var(--color-maroon); margin-bottom: 0.2rem;">Email Correspondence:</h4>
              <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">
                <strong>Official Email:</strong> <a href="mailto:prashantiparyatana26@gmail.com" style="color: var(--color-saffron); font-weight: 700; text-decoration: none;">prashantiparyatana26@gmail.com</a>
              </p>
            </div>
          </div>'''

orig_contact_section = '''          <div style="display: flex; gap: 1rem; align-items: flex-start;">
            <div class="why-us-icon" style="width: 44px; height: 44px; font-size: 1.1rem; flex-shrink: 0;"><i class="fa-solid fa-phone"></i></div>
            <div>
              <h4 style="font-size: 1rem; color: var(--color-maroon); margin-bottom: 0.2rem;">Telephone & WhatsApp:</h4>
              <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.5;">
                Yatra Inquiries: <a href="tel:+919845012345" style="color: var(--color-saffron); font-weight: 600;">+91 98450 12345</a><br />
                Office Reception: <a href="tel:+918023456789" style="color: var(--color-saffron);">+91 80 2345 6789</a>
              </p>
            </div>
          </div>

          <div style="display: flex; gap: 1rem; align-items: flex-start;">
            <div class="why-us-icon" style="width: 44px; height: 44px; font-size: 1.1rem; flex-shrink: 0;"><i class="fa-solid fa-envelope"></i></div>
            <div>
              <h4 style="font-size: 1rem; color: var(--color-maroon); margin-bottom: 0.2rem;">Email Correspondence:</h4>
              <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.5;">
                yatra@prashantiparyatana.org<br />
                counselor@prashantiparyatana.org
              </p>
            </div>
          </div>'''

# Regular expression patterns for added blocks
modal_pill_regex = re.compile(r'\s*<!-- Direct Quick Contact Pill -->\s*<div class="modal-quick-contact".*?</div>(?=\s*<div id="enquiryFormContainer">)', re.DOTALL)
drawer_contact_regex = re.compile(r'\s*<div class="mobile-drawer-contact".*?</div>(?=\s*</div>\s*</div>)', re.DOTALL)
helpdesk_strip_regex = re.compile(r'\s*<!-- Direct Pilgrimage Helpdesk Quick Strip -->\s*<div class="enquiry-helpdesk-strip".*?</div>(?=\s*<form id="homeEnquiryForm")', re.DOTALL)
package_sidebar_regex = re.compile(r'\s*<!-- Quick Counselor Contact Block -->\s*<div style="margin-top: 1.2rem;.*?</div>\s*(?=</div>\s*</aside>)', re.DOTALL)

for fpath in glob.glob('C:/Users/yashw/Desktop/TASN  PP/TASN/*.html'):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Revert top bar
    if new_top_bar in content:
        content = content.replace(new_top_bar, orig_top_bar)
    
    # Revert footers
    if new_footer_helpdesk in content:
        content = content.replace(new_footer_helpdesk, orig_footer_helpdesk)
    if new_index_footer in content:
        content = content.replace(new_index_footer, orig_index_footer)

    # Revert contact section in contact.html
    if new_contact_section in content:
        content = content.replace(new_contact_section, orig_contact_section)

    # Revert modal contact pill
    content = modal_pill_regex.sub('', content)

    # Revert mobile drawer contact
    content = drawer_contact_regex.sub('', content)

    # Revert homepage enquiry helpdesk strip
    content = helpdesk_strip_regex.sub('', content)

    # Revert package-detail sidebar contact
    content = package_sidebar_regex.sub('', content)

    # Revert phone placeholders
    content = content.replace('placeholder="+91 94821 62213 / 9980239643"', 'placeholder="+91 98450 12345"')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Reverted: {fpath}")

# Revert app.js
with open('C:/Users/yashw/Desktop/TASN  PP/TASN/js/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()
app_js = app_js.replace('https://wa.me/919482162213?text=', 'https://wa.me/919845012345?text=')
with open('C:/Users/yashw/Desktop/TASN  PP/TASN/js/app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)
print("Reverted: js/app.js")

# Revert data.js
with open('C:/Users/yashw/Desktop/TASN  PP/TASN/js/data.js', 'r', encoding='utf-8') as f:
    data_js = f.read()
data_js = data_js.replace("phone: '+91 94821 62213'", "phone: '+91 98450 12345'")
with open('C:/Users/yashw/Desktop/TASN  PP/TASN/js/data.js', 'w', encoding='utf-8') as f:
    f.write(data_js)
print("Reverted: js/data.js")

print("All reversions completed successfully!")
