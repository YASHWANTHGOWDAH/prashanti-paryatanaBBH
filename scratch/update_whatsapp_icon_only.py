import glob
import os

files = glob.glob(r'C:\Users\yashw\Desktop\TASN  PP\TASN\*.html')

for fpath in files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Contact.html WhatsApp button: replace with round icon button
    old_contact_wa = '''<div>
                <a href="https://wa.me/919980239643?text=Namaskaram!%20I%20would%20like%20to%20enquire%20about%20a%20pilgrimage%20with%20Prashanti%20Paryatana." target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 0.5rem; background: #25D366; color: #fff; padding: 0.45rem 1rem; border-radius: 999px; text-decoration: none; font-size: 0.85rem; font-weight: 700; box-shadow: 0 4px 12px rgba(37, 211, 102, 0.35); transition: transform 0.2s ease;">
                  <i class="fa-brands fa-whatsapp" style="font-size: 1.1rem;"></i> Chat on WhatsApp (99802 39643)
                </a>
              </div>'''
    new_contact_wa = '''<div>
                <a href="https://wa.me/919980239643?text=Namaskaram!%20I%20would%20like%20to%20enquire%20about%20a%20pilgrimage%20with%20Prashanti%20Paryatana." target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; justify-content: center; width: 42px; height: 42px; background: #25D366; color: #fff; border-radius: 50%; text-decoration: none; font-size: 1.4rem; box-shadow: 0 4px 12px rgba(37, 211, 102, 0.35); transition: transform 0.2s ease;" title="Chat on WhatsApp" aria-label="Chat on WhatsApp">
                  <i class="fa-brands fa-whatsapp"></i>
                </a>
              </div>'''
    if old_contact_wa in content:
        content = content.replace(old_contact_wa, new_contact_wa)

    # 2. Package-detail.html sidebar: replace with round icon button
    old_pkg_wa = '''<div style="margin-bottom: 0.4rem;">
              <a href="https://wa.me/919980239643?text=Namaskaram!%20I%20would%20like%20to%20enquire%20about%20a%20yatra%20package." target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 0.4rem; background: #25D366; color: #fff; padding: 0.35rem 0.85rem; border-radius: 999px; text-decoration: none; font-size: 0.8rem; font-weight: 700; box-shadow: 0 3px 8px rgba(37, 211, 102, 0.3);">
                <i class="fa-brands fa-whatsapp"></i> Chat on WhatsApp (99802 39643)
              </a>
            </div>'''
    new_pkg_wa = '''<div style="margin-bottom: 0.4rem;">
              <a href="https://wa.me/919980239643?text=Namaskaram!%20I%20would%20like%20to%20enquire%20about%20a%20yatra%20package." target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; justify-content: center; width: 38px; height: 38px; background: #25D366; color: #fff; border-radius: 50%; text-decoration: none; font-size: 1.25rem; box-shadow: 0 3px 8px rgba(37, 211, 102, 0.3); transition: transform 0.2s ease;" title="Chat on WhatsApp" aria-label="Chat on WhatsApp">
                <i class="fa-brands fa-whatsapp"></i>
              </a>
            </div>'''
    if old_pkg_wa in content:
        content = content.replace(old_pkg_wa, new_pkg_wa)

    # 3. Index.html helpline strip: replace with round icon button
    old_index_strip = '''<a href="https://wa.me/919980239643?text=Namaskaram!%20I%20would%20like%20to%20plan%20a%20sacred%20yatra%20with%20Prashanti%20Paryatana." target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 0.4rem; background: #25D366; color: #fff; padding: 0.35rem 0.85rem; border-radius: 999px; text-decoration: none; font-size: 0.82rem; font-weight: 700; box-shadow: 0 2px 8px rgba(37, 211, 102, 0.35);">
              <i class="fa-brands fa-whatsapp"></i> WhatsApp 99802 39643
            </a>'''
    new_index_strip = '''<a href="https://wa.me/919980239643?text=Namaskaram!%20I%20would%20like%20to%20plan%20a%20sacred%20yatra%20with%20Prashanti%20Paryatana." target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; justify-content: center; width: 34px; height: 34px; background: #25D366; color: #fff; border-radius: 50%; text-decoration: none; font-size: 1.15rem; box-shadow: 0 2px 8px rgba(37, 211, 102, 0.35); transition: transform 0.2s ease;" title="Chat on WhatsApp" aria-label="Chat on WhatsApp">
              <i class="fa-brands fa-whatsapp"></i>
            </a>'''
    if old_index_strip in content:
        content = content.replace(old_index_strip, new_index_strip)

    # 4. Footer in secondary pages:
    old_footer_secondary = '''<a href="https://wa.me/919980239643?text=Namaskaram!%20I%20would%20like%20to%20enquire%20about%20a%20yatra." target="_blank" rel="noopener noreferrer" style="color: #25D366; text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; gap: 0.35rem; margin-top: 0.35rem;">
                <i class="fa-brands fa-whatsapp"></i> WhatsApp 99802 39643
              </a>'''
    new_footer_secondary = '''<a href="https://wa.me/919980239643?text=Namaskaram!%20I%20would%20like%20to%20enquire%20about%20a%20yatra." target="_blank" rel="noopener noreferrer" style="color: #25D366; text-decoration: none; font-size: 1.35rem; display: inline-flex; align-items: center; margin-top: 0.35rem; transition: transform 0.2s ease;" title="Chat on WhatsApp" aria-label="Chat on WhatsApp">
                <i class="fa-brands fa-whatsapp"></i>
              </a>'''
    if old_footer_secondary in content:
        content = content.replace(old_footer_secondary, new_footer_secondary)

    # 5. Footer in index.html (same link):
    if old_footer_secondary in content:
        content = content.replace(old_footer_secondary, new_footer_secondary)

    # 6. Modal quick contact pill in all pages:
    old_modal = '''<a href="https://wa.me/919980239643?text=Namaskaram!%20I%20have%20an%20enquiry%20regarding%20pilgrimage." target="_blank" rel="noopener noreferrer" style="color: #25D366; font-weight: 700; text-decoration: none; display: inline-flex; align-items: center; gap: 0.3rem;">
              <i class="fa-brands fa-whatsapp"></i> WhatsApp 99802 39643
            </a>'''
    new_modal = '''<a href="https://wa.me/919980239643?text=Namaskaram!%20I%20have%20an%20enquiry%20regarding%20pilgrimage." target="_blank" rel="noopener noreferrer" style="color: #25D366; text-decoration: none; display: inline-flex; align-items: center; font-size: 1.25rem; transition: transform 0.2s ease;" title="Chat on WhatsApp" aria-label="Chat on WhatsApp">
              <i class="fa-brands fa-whatsapp"></i>
            </a>'''
    if old_modal in content:
        content = content.replace(old_modal, new_modal)

    # Clean any other remaining exact occurrences of the number beside the whatsapp icon text:
    content = content.replace('WhatsApp 99802 39643', '')
    content = content.replace('Chat on WhatsApp (99802 39643)', '')
    content = content.replace('WhatsApp: 99802 39643', '')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Processed: {os.path.basename(fpath)}')

print('Completed updating all HTML files!')
