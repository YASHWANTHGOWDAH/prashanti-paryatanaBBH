import re
import glob

# 1. Clean top-bar: remove phone number item so only the sacred motto is left
phone_top_bar_pattern = re.compile(
    r'\s*<div class="top-bar-item">\s*<i class="fa-solid fa-phone"></i>\s*<a href="tel:\+?91\d+">[^<]+</a>\s*</div>',
    re.DOTALL
)

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

# 4. contact.html contact block
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

# 5. Modal quick contact bar
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

# 6. Mobile Drawer Contacts
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

# 7. Homepage enquiry banner in index.html
old_home_enquiry_head = '''          <p>
            Share your preferred destination, travel mode, and pilgrim requirements. Our counselors will prepare a tailored itinerary adhering to temple timings and authentic traditions.
          </p>
        </div>

        <form id="homeEnquiryForm" onsubmit="handleHomepageEnquiry(event)">'''

new_home_enquiry_head = '''          <p>
            Share your preferred destination, travel mode, and pilgrim requirements. Our counselors will prepare a tailored itinerary adhering to temple timings and authentic traditions.
          </p>
        </div>

        <!-- Direct Pilgrimage Helpdesk Quick Strip -->
        <div class="enquiry-helpdesk-strip" style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; background: var(--color-sandalwood-card, #FFFDF9); border: 1px solid var(--color-gold); border-radius: var(--radius-md); padding: 1rem 1.4rem; margin-bottom: 2rem;">
          <div style="display: flex; align-items: center; gap: 0.8rem;">
            <div class="why-us-icon" style="width: 40px; height: 40px; font-size: 1rem; margin: 0; flex-shrink: 0;"><i class="fa-solid fa-headset"></i></div>
            <div>
              <div style="font-family: var(--font-heading); font-size: 0.95rem; font-weight: 700; color: var(--color-maroon);">Speak Directly With Our Pilgrimage Counselors</div>
              <div style="font-size: 0.82rem; color: var(--text-secondary);">Direct phone lines & sacred email guidance available daily</div>
            </div>
          </div>
          <div style="display: flex; align-items: center; gap: 1.2rem; flex-wrap: wrap; font-size: 0.9rem;">
            <div>
              <i class="fa-solid fa-phone" style="color: var(--color-saffron); margin-right: 0.35rem;"></i>
              <a href="tel:+919482162213" style="color: var(--color-maroon); font-weight: 700; text-decoration: none;">+91 94821 62213</a>
              <span style="color: var(--text-muted); margin: 0 4px;">/</span>
              <a href="tel:+919980239643" style="color: var(--color-maroon); font-weight: 700; text-decoration: none;">+91 99802 39643</a>
            </div>
            <div>
              <i class="fa-solid fa-envelope" style="color: var(--color-saffron); margin-right: 0.35rem;"></i>
              <a href="mailto:prashantiparyatana26@gmail.com" style="color: var(--color-maroon); font-weight: 700; text-decoration: none;">prashantiparyatana26@gmail.com</a>
            </div>
          </div>
        </div>

        <form id="homeEnquiryForm" onsubmit="handleHomepageEnquiry(event)">'''

# 8. Package detail quick counselor
old_pkg_guarantee = '''          <div class="sanatana-guarantee">
            <i class="fa-solid fa-om" style="font-size: 1.1rem;"></i>
            <span>Sattvic food, elder-friendly pacing & authentic Vedic guidance guaranteed.</span>
          </div>
        </div>'''

new_pkg_guarantee = '''          <div class="sanatana-guarantee">
            <i class="fa-solid fa-om" style="font-size: 1.1rem;"></i>
            <span>Sattvic food, elder-friendly pacing & authentic Vedic guidance guaranteed.</span>
          </div>

          <!-- Quick Counselor Contact Block -->
          <div style="margin-top: 1.2rem; padding-top: 1rem; border-top: 1px dashed var(--color-sandalwood-border); text-align: center; font-size: 0.8rem;">
            <div style="font-family: var(--font-heading); font-weight: 700; color: var(--color-maroon); margin-bottom: 0.35rem;">
              <i class="fa-solid fa-headset" style="color: var(--color-saffron); margin-right: 0.25rem;"></i> Immediate Counselor Support
            </div>
            <div style="margin-bottom: 0.35rem;">
              <a href="tel:+919482162213" style="color: var(--color-saffron); font-weight: 700; text-decoration: none;">+91 94821 62213</a>
              <span style="color: var(--text-muted); margin: 0 4px;">/</span>
              <a href="tel:+919980239643" style="color: var(--color-saffron); font-weight: 700; text-decoration: none;">+91 99802 39643</a>
            </div>
            <div>
              <a href="mailto:prashantiparyatana26@gmail.com" style="color: var(--color-maroon); font-weight: 600; text-decoration: none; word-break: break-all;">prashantiparyatana26@gmail.com</a>
            </div>
          </div>
        </div>'''

for fpath in glob.glob('C:/Users/yashw/Desktop/TASN  PP/TASN/*.html'):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Clean top-bar: remove phone item from top-bar so top-bar has NO phone or email
    content = phone_top_bar_pattern.sub('', content)

    # 2. Footers in secondary pages
    if old_footer_helpdesk in content:
        content = content.replace(old_footer_helpdesk, new_footer_helpdesk)

    # 3. Footer in index.html
    if old_index_footer in content:
        content = content.replace(old_index_footer, new_index_footer)

    # 4. contact.html contact block
    if orig_contact_section in content:
        content = content.replace(orig_contact_section, new_contact_section)

    # 5. Modal quick contact pill
    if old_modal_target in content and 'modal-quick-contact' not in content:
        content = content.replace(old_modal_target, new_modal_replacement)

    # 6. Mobile Drawer Contacts
    if 'mobile-drawer-contact' not in content:
        m = re.search(r'(<button type="button" class="btn-plan-journey"[^>]*>.*?</button>\s*</div>\s*</div>)', content, re.DOTALL)
        if m:
            old_block = m.group(1)
            new_block = re.sub(r'(\s*</div>\s*</div>)$', '\n' + drawer_contact + r'\1', old_block)
            content = content.replace(old_block, new_block, 1)

    # 7. Homepage enquiry strip
    if old_home_enquiry_head in content:
        content = content.replace(old_home_enquiry_head, new_home_enquiry_head)

    # 8. Package detail sidebar quick counselor
    if old_pkg_guarantee in content:
        content = content.replace(old_pkg_guarantee, new_pkg_guarantee)

    # Placeholder updates
    content = content.replace('placeholder="+91 98450 12345"', 'placeholder="+91 94821 62213 / 9980239643"')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated: {fpath}")

# Update app.js WhatsApp
with open('C:/Users/yashw/Desktop/TASN  PP/TASN/js/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()
app_js = app_js.replace('https://wa.me/919845012345?text=', 'https://wa.me/919482162213?text=')
with open('C:/Users/yashw/Desktop/TASN  PP/TASN/js/app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)
print("Updated: js/app.js WhatsApp link")

# Update data.js
with open('C:/Users/yashw/Desktop/TASN  PP/TASN/js/data.js', 'r', encoding='utf-8') as f:
    data_js = f.read()
data_js = data_js.replace("phone: '+91 98450 12345'", "phone: '+91 94821 62213'")
with open('C:/Users/yashw/Desktop/TASN  PP/TASN/js/data.js', 'w', encoding='utf-8') as f:
    f.write(data_js)
print("Updated: js/data.js sample phone")

print("All updates applied cleanly!")
