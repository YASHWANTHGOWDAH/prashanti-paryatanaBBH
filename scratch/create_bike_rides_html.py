import os
import glob
import re

# 1. Create bike-rides.html based on bus-tours.html
bus_path = r'C:\Users\yashw\Desktop\TASN  PP\TASN\bus-tours.html'
bike_path = r'C:\Users\yashw\Desktop\TASN  PP\TASN\bike-rides.html'

with open(bus_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace titles, categories, hero
content = content.replace('<title>Bus Tours | Prashanti Paryatana</title>', '<title>Bike Rides & Motorcycle Expeditions | Prashanti Paryatana</title>')
content = content.replace('Explore sacred bus tours and luxury coach pilgrimages across ancient temple circuits in Karnataka, Tamil Nadu, Maharashtra, and Andhra Pradesh.', 'Explore sacred motorcycle expeditions and guided bike rides across high Himalayan passes, Western Ghats hairpins, and holy river confluences with full mechanic backup.')
content = content.replace('<body data-page="bus" data-page-category="bus">', '<body data-page="bike" data-page-category="bike">')

# Hero section replacement
old_hero = '''  <!-- Category Hero -->
  <section class="category-hero" style="background: linear-gradient(135deg, #3C1A0E 0%, #170E0A 100%);">
    <div class="container category-hero-content">
      <span class="section-eyebrow" style="color: var(--color-gold-bright);">Travel Category 01</span>
      <h1>Sacred Bus Tours & Coach Pilgrimages</h1>
      <p>
        Experience regional temple clusters in unmatched comfort aboard our deluxe air-suspension coaches. Designed for families and senior pilgrims seeking unhurried darshans, serene Western Ghats routes, and guided architectural commentary.
      </p>
    </div>
  </section>'''

new_hero = '''  <!-- Category Hero -->
  <section class="category-hero" style="background: linear-gradient(135deg, #2A1708 0%, #170E0A 100%);">
    <div class="container category-hero-content">
      <span class="section-eyebrow" style="color: var(--color-gold-bright);">Travel Category 06</span>
      <h1>Spiritual Bike Rides & Motorcycle Expeditions</h1>
      <p>
        Experience the open road and sacred mountain passes on two wheels. Guided pilgrimage motorcycle rides designed for enthusiastic riders seeking sacred ghats, Himalayan river confluences, and ancient temple highways with dedicated pilot marshals, luggage vans, and mechanical backup.
      </p>
    </div>
  </section>'''

content = content.replace(old_hero, new_hero)

# Filter button replacement
content = content.replace('<button type="button" class="filter-pill active" data-category="bus">All Bus Tours</button>', '<button type="button" class="filter-pill active" data-category="bike">All Bike Rides</button>')

# CTA button
content = content.replace("openEnquiryModal('', 'Bus Tour Enquiry', 'bus')", "openEnquiryModal('', 'Bike Ride Enquiry', 'bike')")

# Write bike-rides.html
with open(bike_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Created bike-rides.html successfully!")
