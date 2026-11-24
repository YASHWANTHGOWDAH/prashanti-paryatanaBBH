import glob
import os
import re

DATA_JS_PATH = r'C:\Users\yashw\Desktop\TASN  PP\TASN\js\data.js'

# 1. Update data.js
with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
    data_content = f.read()

# Update STORAGE_KEYS
data_content = data_content.replace(
    "PACKAGES: 'pp_packages_v2',",
    "PACKAGES: 'pp_packages_v3',"
)

# New Bike Rides packages to append to INITIAL_PACKAGES
bike_packages_code = '''
  // --- 6. BIKE RIDES (MOTORCYCLE EXPEDITIONS) ---
  {
    id: 'bike-kedar-valley-ride',
    name: 'Himalayan Shiva & Kedar Valley Royal Enfield Yatra',
    category: 'bike',
    destination: 'Uttarakhand (Rishikesh, Devprayag, Guptkashi, Chopta, Badrinath)',
    duration: '9 Days / 8 Nights',
    travelMode: 'Royal Enfield Himalayan 450cc Cruiser Caravan with Backup Van',
    startingLocation: 'Rishikesh (Triveni Ghat Base)',
    shortDescription: 'A soul-stirring spiritual motorcycle pilgrimage through the Panch Prayags, high Himalayan passes, and sacred Shiva-Vishnu sanctuaries.',
    image: 'assets/temples/kedarnath.jpg',
    featured: true,
    overview: 'Ride along the roaring holy confluences of the Ganga, Alaknanda, and Mandakini rivers on adventure touring motorcycles. This expedition combines the freedom of mountain riding with sacred temple darshans, morning Rudrabhisheka, evening Ganga Aarti, and serene Himalayan contemplation accompanied by certified ride captains and mobile mechanical backup.',
    historyBackground: 'The Garhwal Himalayas are revered in the Mahabharata as the sacred Devbhoomi where the Pandavas sought Bhagavan Shiva\\'s grace. The mountain roads follow ancient pilgrim trails connecting the Panch Prayags (sacred river confluences) to high sanctums like Tungnath (the highest Shiva temple in the world at 3,680m) and Badrinath Dham, established by Adi Shankaracharya in the 8th century CE.',
    placesCovered: ['Rishikesh', 'Devprayag', 'Rudraprayag', 'Guptkashi', 'Chopta', 'Joshimath', 'Badrinath', 'Mana Village'],
    templeVisits: [
      'Raghunathji Temple, Devprayag (Ancient Rama temple at the Ganga birthplace)',
      'Kashi Vishwanath Temple, Guptkashi',
      'Tungnath Temple, Chopta (Highest Shiva temple on earth)',
      'Badrinath Dham (Sacred Badri Vishal darshan)',
      'Vyasa Gufa & Ganesha Gufa, Mana Village'
    ],
    highlights: [
      'Royal Enfield Himalayan 450cc motorcycles with riding gear assistance',
      'Dedicated backup luggage truck, certified mechanic, and spare parts trailer',
      'Daily satsangs, temple darshans, and evening Ganga Aarti at Rishikesh & Devprayag',
      'High-altitude alpine ride to Chopta and scenic pass crossing',
      'Pure sattvic vegetarian hot meals prepared fresh at every halt'
    ],
    itinerary: [
      { day: 1, title: 'Arrival in Rishikesh & Bike Handover', desc: 'Rider briefing, safety protocol alignment, bike allocation, and sunset Ganga Aarti at Triveni Ghat.' },
      { day: 2, title: 'Rishikesh to Devprayag & Rudraprayag', desc: 'Ride along NH58 hugging the roaring Ganga. Witness the confluence of Bhagirathi and Alaknanda at Devprayag.' },
      { day: 3, title: 'Rudraprayag to Guptkashi', desc: 'Ascend along the Mandakini river into the Kedar valley. Evening darshan at ancient Vishwanath temple.' },
      { day: 4, title: 'Guptkashi to Chopta & Tungnath', desc: 'Ride through pristine rhododendron and deodar forests to the alpine meadow of Chopta. Gentle trek to Tungnath temple.' },
      { day: 5, title: 'Chopta to Joshimath via Mandal Pass', desc: 'Scenic descent through Mandal valley and ascent to Joshimath, seat of Adi Shankara\\'s northern Jyotirmath peetham.' },
      { day: 6, title: 'Joshimath to Badrinath Dham & Mana', desc: 'Ride the dramatic Alaknanda gorge road to Badrinath Dham. Sacred evening darshan and visit to Mana (last Indian village).' },
      { day: 7, title: 'Badrinath to Karnaprayag', desc: 'Morning Brahma Kapal tirth snan, followed by scenic descent through Chamoli to Karnaprayag confluence.' },
      { day: 8, title: 'Karnaprayag to Rishikesh', desc: 'Return ride via Srinagar and Kaudiyala back to Rishikesh. Celebration dinner and group debriefing.' },
      { day: 9, title: 'Departure from Rishikesh', desc: 'Morning Ganga snan, bike return, and onward transit to Dehradun Airport or Haridwar Railway Station.' }
    ],
    priceStandard: '₹42,500 per rider',
    priceDeluxe: '₹54,000 per rider (Twin sharing premium alpine resorts)',
    accommodationDetails: 'Quality mountain cottages, Swiss alpine camps in Chopta, and riverside hotels in Rishikesh and Joshimath.',
    meals: 'Nutritious sattvic vegetarian food with energizing hot herbal teas and refreshments during riding breaks.',
    included: [
      'Royal Enfield motorcycle with fuel & maintenance',
      'Backup support truck with luggage carrier and mechanic',
      'Lead ride captain and emergency first-aid kit with oxygen cylinder',
      '8 nights hotel/camp accommodation on twin sharing',
      'All meals (breakfast, riding snacks, hot dinner)'
    ],
    excluded: [
      'Personal riding jacket/helmet (rental available)',
      'Security deposit for motorcycle (refundable)',
      'Any personal expenses or temple donations'
    ],
    safetyRequirements: 'Valid motorcycle driving licence (with gear) required. Full-face helmet, riding gloves, and knee/elbow guards mandatory.'
  },
  {
    id: 'bike-western-ghats-circuit',
    name: 'Sahyadri Peethams & Western Ghats Temple Ride',
    category: 'bike',
    destination: 'Karnataka (Bengaluru, Belur, Chikmagalur, Sringeri, Agumbe, Murudeshwar)',
    duration: '5 Days / 4 Nights',
    travelMode: 'Cruiser Motorcycles with Ride Captain, Escort & Luggage Support',
    startingLocation: 'Bengaluru (Yeshwantpur Toll Plaza Base)',
    shortDescription: 'Navigate misty ghat curves and coffee hills to seek blessings at Sringeri Sharada Peetham, Horanadu Annapoorneshwari, and coastal Shiva temples.',
    image: 'assets/temples/belur.jpg',
    featured: true,
    overview: 'This route is a rider\\'s paradise through the heart of Karnataka\\'s spiritual heritage. Ascend through the Charmadi and Agumbe rainforest hairpins, immerse in the serene Vedic ambiance of Sringeri on the banks of Tunga river, and ride along the scenic coastal highway to Murudeshwar.',
    historyBackground: 'Weaving through the dense evergreen biodiversity of the Sahyadri mountains, this circuit connects the 12th-century Hoysala temple marvels at Belur and Halebidu with Sringeri Sharada Peetham, consecrated by Adi Shankaracharya over 1,200 years ago. The journey unites architectural wonder, sacred rivers, and the tranquil spiritual power of the Western Ghats.',
    placesCovered: ['Bengaluru', 'Belur', 'Chikmagalur', 'Horanadu', 'Sringeri', 'Agumbe', 'Udupi', 'Murudeshwar'],
    templeVisits: [
      'Chennakeshava Temple, Belur (Exquisite Hoysala soapstone architecture)',
      'Sri Annapoorneshwari Temple, Horanadu (Serene valley sanctum)',
      'Sri Sharadamba Temple & Vidyashankara Temple, Sringeri',
      'Sri Krishna Matha, Udupi (Madhvacharya\\'s sacred seat)',
      'Murudeshwar Temple & Giant Shiva Statue on the Arabian Sea'
    ],
    highlights: [
      'Scenic hairpin bends of Charmadi Ghat and Agumbe sunset point',
      'VIP guided darshans at Sringeri and Horanadu temples',
      'Ride support vehicle with mechanical assistance and luggage transit',
      'Authentic Malnad and coastal sattvic temple prasada banquets'
    ],
    itinerary: [
      { day: 1, title: 'Bengaluru to Belur & Chikmagalur', desc: 'Early morning flag-off from Bengaluru. Highway cruise to Belur for an in-depth architectural temple walk, night stay in Chikmagalur coffee estates.' },
      { day: 2, title: 'Chikmagalur to Horanadu & Sringeri', desc: 'Ride the winding forest curves through Kottigehara and Kalasa to Horanadu. Afternoon ride to Sringeri for evening temple rituals.' },
      { day: 3, title: 'Sringeri Sacred Exploration to Agumbe', desc: 'Morning darshan of Jagadguru and Vidyashankara temple. Ride through dense canopy to Agumbe rainforest and sunset viewpoint.' },
      { day: 4, title: 'Agumbe down to Udupi & Murudeshwar', desc: 'Descent through 14 thrilling hairpin bends of Someshwara wildlife sanctuary. Darshan at Udupi Sri Krishna Matha and coastal ride to Murudeshwar.' },
      { day: 5, title: 'Murudeshwar to Bengaluru via Shimoga', desc: 'Sunrise darshan at Murudeshwar temple overlooking the sea. Return scenic cruise via Honnavar, Sagara, and Shimoga back to Bengaluru.' }
    ],
    priceStandard: '₹24,500 per rider',
    priceDeluxe: '₹32,000 per rider',
    accommodationDetails: 'Heritage estate homestays in Chikmagalur and premium hotels in Sringeri and Murudeshwar.',
    meals: 'Traditional Malnad vegetarian feasts, temple mahaprasadam, and freshly brewed Chikmagalur filter coffee.',
    included: [
      'Ride logistics, pilot marshal, and backup support vehicle',
      '4 nights accommodation on twin sharing basis',
      'Breakfasts and traditional dinners',
      'Guided temple entries and cultural facilitation'
    ],
    excluded: [
      'Fuel for own motorcycle (or motorcycle rental if requested)',
      'Personal riding gear and toll charges'
    ],
    safetyRequirements: 'Riders must wear proper riding jacket, helmet, riding pants/knee guards, and sturdy riding boots.'
  },
  {
    id: 'bike-ladakh-monasteries-circuit',
    name: 'Ladakh High Altitude Monasteries & Sacred Pass Ride',
    category: 'bike',
    destination: 'Ladakh (Leh, Hemis, Thiksey, Nubra Valley, Pangong Tso, Khardung La)',
    duration: '8 Days / 7 Nights',
    travelMode: 'Adventure Touring 450cc Dual-Sport Motorcycles with Oxygen & Mechanic Backup',
    startingLocation: 'Leh Kushok Bakula Rimpochee Airport',
    shortDescription: 'Navigate the highest motorable passes on earth while exploring ancient gompas, meditation caves, and sacred high-altitude alpine lakes.',
    image: 'assets/temples/kailash.jpg',
    featured: false,
    overview: 'An epic spiritual journey through high-altitude desert plateaus, prayer-flagged passes, and timeless Buddhist and Vedic meditation sanctuaries. Riders ascend Khardung La and Chang La, explore Hemis and Thiksey monasteries, and camp under starlit Himalayan skies beside Pangong Tso.',
    historyBackground: 'Ladakh (Maryul - the ancient red land) sits at the crossroads of Tibetan Buddhist tantric traditions and ancient Indic Silk Route caravans. Monasteries founded in the 10th and 11th centuries by Guru Rinpoche and Naropa safeguard irreplaceable ancient frescoes, copper-gilt Buddhas, and thousands of sacred Buddhist manuscripts.',
    placesCovered: ['Leh', 'Shey', 'Thiksey', 'Hemis', 'Khardung La', 'Nubra Valley', 'Diskit', 'Pangong Tso', 'Chang La'],
    templeVisits: [
      'Thiksey Monastery (Mini-Potala Palace of Ladakh)',
      'Hemis Gompa (Drukpa lineage spiritual capital)',
      'Diskit Monastery & Giant Maitreya Buddha, Nubra',
      'Shanti Stupa & Leh Palace',
      'Sacred Pangong Tso meditation shores'
    ],
    highlights: [
      'Conquer Khardung La (17,982 ft) and Chang La (17,688 ft)',
      'Adventure motorcycles with specialized high-altitude carburetor tuning',
      'Full mechanical crew, backup pickup truck, and medical oxygen cylinders',
      'Deluxe Swiss tent glamping beside Pangong Tso with heating'
    ],
    itinerary: [
      { day: 1, title: 'Arrival in Leh & Complete Rest', desc: 'Mandatory acclimatization day to adjust to 11,500 ft elevation. Evening walk to Shanti Stupa.' },
      { day: 2, title: 'Leh Local Gompas & Bike Orientation', desc: 'Visit Shey Palace, Thiksey Monastery, and Hemis. Afternoon short test ride around Leh valley.' },
      { day: 3, title: 'Leh to Nubra Valley via Khardung La', desc: 'Epic ascent to Khardung La pass at nearly 18,000 feet. Descend into the dramatic dunes of Nubra Valley.' },
      { day: 4, title: 'Diskit to Turtuk Border Village', desc: 'Ride along the Shyok river to Turtuk, exploring ancient Balti heritage and organic apricot orchards.' },
      { day: 5, title: 'Nubra to Pangong Tso via Shyok Route', desc: 'Thrilling off-road and water crossings along the rugged Shyok river gorge leading to the azure waters of Pangong Tso.' },
      { day: 6, title: 'Pangong Tso to Leh via Chang La', desc: 'Sunrise meditation by the lake, followed by conquering Chang La pass (17,688 ft) and returning to Leh.' },
      { day: 7, title: 'Leh Sangam & Magnetic Hill Ride', desc: 'Ride along the Indus to the sacred Indus-Zanskar confluence (Nimmu) and Gurudwara Pathar Sahib.' },
      { day: 8, title: 'Departure from Leh', desc: 'Airport transfer with blessed Tibetan prayer flags and memories of the sacred high Himalayas.' }
    ],
    priceStandard: '₹48,000 per rider',
    priceDeluxe: '₹62,000 per rider',
    accommodationDetails: 'Premium boutique hotels in Leh and luxury heated Swiss tents at Nubra and Pangong.',
    meals: 'Wholesome nutritious vegetarian meals with high-altitude hydration drinks and soups.',
    included: [
      'Royal Enfield Himalayan motorcycle with fuel',
      'All Inner Line Permits and wildlife environmental fees',
      'Support vehicle with mechanic, spare parts, and oxygen backup',
      '7 nights accommodation with breakfast and dinner'
    ],
    excluded: [
      'Flights to/from Leh',
      'Personal riding gear and monument camera fees'
    ],
    safetyRequirements: 'Strict physical fitness required for high altitude. Pre-acclimatization and comprehensive riding gear mandatory.'
  }
'''

# Find the end of INITIAL_PACKAGES
target_end = 'safetyRequirements: \'Evenings can be chilly in February; warm shawls and jackets necessary for the open-air festival venue.\'\n  }\n];'
replacement_end = 'safetyRequirements: \'Evenings can be chilly in February; warm shawls and jackets necessary for the open-air festival venue.\'\n  },' + bike_packages_code + '\n];'

if target_end in data_content:
    data_content = data_content.replace(target_end, replacement_end)
    print("Added Bike Rides packages to INITIAL_PACKAGES in data.js")
else:
    print("Could not find target_end in data.js")

# Also update getPackages() in PrashantiDatabase to merge any missing packages into localStorage automatically:
old_get_pkg = '''  static getPackages() {
    const data = localStorage.getItem(STORAGE_KEYS.PACKAGES);
    if (!data) {
      localStorage.setItem(STORAGE_KEYS.PACKAGES, JSON.stringify(INITIAL_PACKAGES));
      return INITIAL_PACKAGES;
    }
    try {
      return JSON.parse(data);
    } catch (e) {
      console.error('Error parsing packages from localStorage', e);
      return INITIAL_PACKAGES;
    }
  }'''

new_get_pkg = '''  static getPackages() {
    const data = localStorage.getItem(STORAGE_KEYS.PACKAGES);
    if (!data) {
      localStorage.setItem(STORAGE_KEYS.PACKAGES, JSON.stringify(INITIAL_PACKAGES));
      return INITIAL_PACKAGES;
    }
    try {
      const stored = JSON.parse(data);
      const storedIds = new Set(stored.map(p => p.id));
      let updated = false;
      INITIAL_PACKAGES.forEach(pkg => {
        if (!storedIds.has(pkg.id)) {
          stored.push(pkg);
          updated = true;
        }
      });
      if (updated) {
        localStorage.setItem(STORAGE_KEYS.PACKAGES, JSON.stringify(stored));
      }
      return stored;
    } catch (e) {
      console.error('Error parsing packages from localStorage', e);
      return INITIAL_PACKAGES;
    }
  }'''

data_content = data_content.replace(old_get_pkg, new_get_pkg)

with open(DATA_JS_PATH, 'w', encoding='utf-8') as f:
    f.write(data_content)
print("Updated js/data.js successfully!")
