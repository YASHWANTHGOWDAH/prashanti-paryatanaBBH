import glob
import re

for fpath in glob.glob('C:/Users/yashw/Desktop/TASN  PP/TASN/*.html'):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. In contact.html and package-detail: 'Chat on WhatsApp (99802 39643)' -> 'Chat on WhatsApp'
    content = content.replace('Chat on WhatsApp (99802 39643)', 'Chat on WhatsApp')

    # 2. In footer and modal: 'WhatsApp 99802 39643' -> 'WhatsApp'
    content = content.replace('WhatsApp 99802 39643', 'WhatsApp')

    # 3. In homepage enquiry strip: 'WhatsApp 99802 39643' -> 'WhatsApp'
    content = content.replace('WhatsApp: 99802 39643', 'WhatsApp')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated WhatsApp icon in: {fpath}")

print("All WhatsApp number texts removed beside icons!")
