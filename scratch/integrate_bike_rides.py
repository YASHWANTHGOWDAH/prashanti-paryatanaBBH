import glob
import os
import re

# 1. Update css/components.css
css_path = r'C:\Users\yashw\Desktop\TASN  PP\TASN\css\components.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_text = f.read()

if '.cat-bike' not in css_text:
    css_text = css_text.replace(
        '.package-card-badge.cat-cultural { border-color: #E74C3C; color: #FDFEFE; }',
        '.package-card-badge.cat-cultural { border-color: #E74C3C; color: #FDFEFE; }\n.package-card-badge.cat-bike { border-color: #D35400; color: #FDFEFE; }'
    )
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_text)
    print("Added .cat-bike to components.css")

# 2. Update HTML files
files = glob.glob(r'C:\Users\yashw\Desktop\TASN  PP\TASN\*.html')

for fpath in files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- A. Navigation Category Link ---
    # In bike-rides.html, the active link is bike-rides
    # In other pages, regular category-link
    if fname == 'bike-rides.html':
        target_nav_item = '''        <a href="bike-rides.html" class="category-link active">
          <i class="fa-solid fa-motorcycle"></i>
          <span>Bike Rides</span>
        </a>'''
    else:
        target_nav_item = '''        <a href="bike-rides.html" class="category-link">
          <i class="fa-solid fa-motorcycle"></i>
          <span>Bike Rides</span>
        </a>'''

    # Ensure bike-rides.html doesn't have bus-tours.html active
    if fname == 'bike-rides.html':
        content = content.replace('href="bus-tours.html" class="category-link active"', 'href="bus-tours.html" class="category-link"')
        content = content.replace('href="bus-tours.html" class="mobile-nav-item active"', 'href="bus-tours.html" class="mobile-nav-item"')

    # Insert before </nav> in .categories-nav if not already present
    if 'href="bike-rides.html"' not in content:
        # Match cultural category link in categories-nav
        cultural_nav_pattern = r'(<a href="cultural\.html" class="category-link[^"]*">\s*<i class="fa-solid fa-drum"></i>\s*<span>Cultural Travel</span>\s*</a>)'
        if re.search(cultural_nav_pattern, content):
            content = re.sub(
                cultural_nav_pattern,
                r'\1\n' + target_nav_item,
                content,
                count=1
            )
            print(f"[{fname}] Added Bike Rides to categories-nav")

    # --- B. Mobile Drawer Links ---
    if fname == 'bike-rides.html':
        target_drawer_item = '<a href="bike-rides.html" class="mobile-nav-item active"><i class="fa-solid fa-motorcycle"></i> Bike Rides</a>'
    else:
        target_drawer_item = '<a href="bike-rides.html" class="mobile-nav-item"><i class="fa-solid fa-motorcycle"></i> Bike Rides</a>'

    if target_drawer_item not in content:
        drawer_pattern = r'(<a href="cultural\.html" class="mobile-nav-item[^"]*"><i class="fa-solid fa-drum"></i>\s*(?:<span>)?Cultural Travel(?:</span>)?</a>)'
        if re.search(drawer_pattern, content):
            content = re.sub(drawer_pattern, r'\1\n        ' + target_drawer_item, content, count=1)
            print(f"[{fname}] Added Bike Rides to mobile drawer")

    # --- C. Footer Main Categories ---
    footer_cultural = '<li><a href="cultural.html"><i class="fa-solid fa-drum"></i> Cultural Travel</a></li>'
    footer_bike = '<li><a href="bike-rides.html"><i class="fa-solid fa-motorcycle"></i> Bike Rides</a></li>'
    if footer_bike not in content and footer_cultural in content:
        content = content.replace(footer_cultural, footer_cultural + '\n            ' + footer_bike)
        print(f"[{fname}] Added Bike Rides to footer")

    # --- D. Modal Category Select ---
    modal_cultural = '<option value="cultural">Cultural Travel</option>'
    if fname == 'bike-rides.html':
        modal_bike = '<option value="cultural">Cultural Travel</option>\n                  <option value="bike" selected>Bike Rides</option>'
        content = content.replace('<option value="bus" selected>Bus Tours</option>', '<option value="bus">Bus Tours</option>')
    else:
        modal_bike = '<option value="cultural">Cultural Travel</option>\n                  <option value="bike">Bike Rides</option>'

    if '<option value="bike"' not in content and modal_cultural in content:
        content = content.replace(modal_cultural, modal_bike)
        print(f"[{fname}] Added Bike Rides to enquiry modal")

    # --- E. Specific Page Adjustments ---
    if fname == 'index.html':
        # Hero quick categories
        quick_cultural = '''        <a href="cultural.html" class="quick-cat-btn">
          <i class="fa-solid fa-drum"></i>
          <span>Cultural Travel</span>
        </a>'''
        quick_bike = '''        <a href="cultural.html" class="quick-cat-btn">
          <i class="fa-solid fa-drum"></i>
          <span>Cultural Travel</span>
        </a>
        <a href="bike-rides.html" class="quick-cat-btn">
          <i class="fa-solid fa-motorcycle"></i>
          <span>Bike Rides</span>
        </a>'''
        if 'href="bike-rides.html" class="quick-cat-btn"' not in content and quick_cultural in content:
            content = content.replace(quick_cultural, quick_bike)
            print("[index.html] Added Bike Rides to hero-quick-categories")

        # Categories grid 6th card
        cat_5_end = '''        <!-- 5. Cultural Travel -->
        <a href="cultural.html" class="category-card">
          <img class="category-card-bg" src="assets/cultural/ayodhya-dance.jpg" alt="Classical Indian Dance" />
          <div class="category-card-gradient"></div>
          <div class="category-card-content">
            <span class="category-badge-num">CATEGORY 05</span>
            <h3>Cultural Travel</h3>
            <p>Attend classical Carnatic, Hindustani, Bharatanatyam and Natyanjali festivals, or register as a classical artist for temple performances.</p>
            <div class="category-card-btn">
              <span>Explore Cultural Portal</span>
              <i class="fa-solid fa-arrow-right"></i>
            </div>
          </div>
        </a>'''

        cat_6_card = '''        <!-- 5. Cultural Travel -->
        <a href="cultural.html" class="category-card">
          <img class="category-card-bg" src="assets/cultural/ayodhya-dance.jpg" alt="Classical Indian Dance" />
          <div class="category-card-gradient"></div>
          <div class="category-card-content">
            <span class="category-badge-num">CATEGORY 05</span>
            <h3>Cultural Travel</h3>
            <p>Attend classical Carnatic, Hindustani, Bharatanatyam and Natyanjali festivals, or register as a classical artist for temple performances.</p>
            <div class="category-card-btn">
              <span>Explore Cultural Portal</span>
              <i class="fa-solid fa-arrow-right"></i>
            </div>
          </div>
        </a>

        <!-- 6. Bike Rides -->
        <a href="bike-rides.html" class="category-card">
          <img class="category-card-bg" src="assets/temples/tungnath.jpg" alt="Himalayan Spiritual Bike Ride" />
          <div class="category-card-gradient"></div>
          <div class="category-card-content">
            <span class="category-badge-num">CATEGORY 06</span>
            <h3>Bike Rides</h3>
            <p>Guided pilgrimage motorcycle expeditions across sacred Himalayan passes, Western Ghats hairpins, and holy river confluences with support vehicles.</p>
            <div class="category-card-btn">
              <span>Explore Bike Rides</span>
              <i class="fa-solid fa-arrow-right"></i>
            </div>
          </div>
        </a>'''
        if 'CATEGORY 06' not in content and cat_5_end in content:
            content = content.replace(cat_5_end, cat_6_card)
            print("[index.html] Added Category 06 card to categories-grid")

    elif fname == 'packages.html':
        pill_cultural = '<button type="button" class="filter-pill" data-category="cultural">Cultural Travel</button>'
        pill_bike = '<button type="button" class="filter-pill" data-category="cultural">Cultural Travel</button>\n        <button type="button" class="filter-pill" data-category="bike">Bike Rides</button>'
        if 'data-category="bike"' not in content and pill_cultural in content:
            content = content.replace(pill_cultural, pill_bike)
            print("[packages.html] Added Bike Rides filter pill")

    elif fname == 'admin.html':
        admin_opt_cultural = '<option value="cultural">5. Cultural Travel</option>'
        admin_opt_bike = '<option value="cultural">5. Cultural Travel</option>\n                <option value="bike">6. Bike Rides</option>'
        if 'value="bike"' not in content and admin_opt_cultural in content:
            content = content.replace(admin_opt_cultural, admin_opt_bike)
            print("[admin.html] Added Bike Rides to admin package form")

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("All navigation and integration updates finished!")
