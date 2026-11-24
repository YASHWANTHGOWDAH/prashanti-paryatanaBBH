import glob

old_footer_secondary = '''          <div class="footer-contact-item">
            <i class="fa-solid fa-phone"></i>
            <div>
              <a href="tel:+919482162213" style="color: inherit; text-decoration: none;">+91 94821 62213</a><br />
              <a href="tel:+919980239643" style="color: inherit; text-decoration: none;">+91 99802 39643</a>
            </div>
          </div>'''

new_footer_secondary = '''          <div class="footer-contact-item">
            <i class="fa-solid fa-phone"></i>
            <div>
              <a href="tel:+919482162213" style="color: inherit; text-decoration: none;">+91 94821 62213</a><br />
              <a href="tel:+919980239643" style="color: inherit; text-decoration: none;">+91 99802 39643</a><br />
              <a href="https://wa.me/919980239643?text=Namaskaram!%20I%20would%20like%20to%20enquire%20about%20a%20yatra." target="_blank" rel="noopener noreferrer" style="color: #25D366; text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; gap: 0.35rem; margin-top: 0.35rem;">
                <i class="fa-brands fa-whatsapp"></i> WhatsApp 99802 39643
              </a>
            </div>
          </div>'''

old_footer_index = '''          <div class="footer-contact-item">
            <i class="fa-solid fa-phone"></i>
            <div>
              <strong>Direct Yatra Lines:</strong><br />
              <a href="tel:+919482162213" style="color: inherit; text-decoration: none;">+91 94821 62213</a> / 
              <a href="tel:+919980239643" style="color: inherit; text-decoration: none;">+91 99802 39643</a>
            </div>
          </div>'''

new_footer_index = '''          <div class="footer-contact-item">
            <i class="fa-solid fa-phone"></i>
            <div>
              <strong>Direct Yatra Lines:</strong><br />
              <a href="tel:+919482162213" style="color: inherit; text-decoration: none;">+91 94821 62213</a> / 
              <a href="tel:+919980239643" style="color: inherit; text-decoration: none;">+91 99802 39643</a><br />
              <a href="https://wa.me/919980239643?text=Namaskaram!%20I%20would%20like%20to%20enquire%20about%20a%20yatra." target="_blank" rel="noopener noreferrer" style="color: #25D366; text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; gap: 0.35rem; margin-top: 0.35rem;">
                <i class="fa-brands fa-whatsapp"></i> WhatsApp 99802 39643
              </a>
            </div>
          </div>'''

old_modal = '''        <!-- Direct Quick Contact Pill -->
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
        </div>'''

new_modal = '''        <!-- Direct Quick Contact Pill -->
        <div class="modal-quick-contact" style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem; background: var(--color-sandalwood-light); border: 1px solid var(--color-gold); border-radius: var(--radius-sm); padding: 0.6rem 0.9rem; margin-bottom: 1.2rem; font-size: 0.82rem;">
          <div style="display: flex; align-items: center; gap: 0.4rem;">
            <i class="fa-solid fa-phone" style="color: var(--color-saffron);"></i>
            <span style="font-weight: 600; color: var(--color-maroon);">Call:</span>
            <a href="tel:+919482162213" style="color: var(--color-maroon); font-weight: 700; text-decoration: none;">+91 94821 62213</a>
            <span style="opacity: 0.5;">/</span>
            <a href="tel:+919980239643" style="color: var(--color-maroon); font-weight: 700; text-decoration: none;">+91 99802 39643</a>
          </div>
          <div style="display: flex; align-items: center; gap: 0.6rem;">
            <a href="https://wa.me/919980239643?text=Namaskaram!%20I%20have%20an%20enquiry%20regarding%20pilgrimage." target="_blank" rel="noopener noreferrer" style="color: #25D366; font-weight: 700; text-decoration: none; display: inline-flex; align-items: center; gap: 0.3rem;">
              <i class="fa-brands fa-whatsapp"></i> WhatsApp 99802 39643
            </a>
            <span style="opacity: 0.4;">|</span>
            <a href="mailto:prashantiparyatana26@gmail.com" style="color: var(--color-maroon); font-weight: 600; text-decoration: none;">prashantiparyatana26@gmail.com</a>
          </div>
        </div>'''

for fpath in glob.glob('C:/Users/yashw/Desktop/TASN  PP/TASN/*.html'):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    modified = False
    if old_footer_secondary in content:
        content = content.replace(old_footer_secondary, new_footer_secondary)
        modified = True
    if old_footer_index in content:
        content = content.replace(old_footer_index, new_footer_index)
        modified = True
    if old_modal in content:
        content = content.replace(old_modal, new_modal)
        modified = True

    if modified:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated footer/modal WhatsApp in: {fpath}")

print("WhatsApp updates complete!")
