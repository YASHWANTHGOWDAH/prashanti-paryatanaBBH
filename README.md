# Prashanti Paryatana (प्रशान्ति पर्यटन)

> **Spiritual, Heritage, Pilgrimage and Cultural Travel Organization**  
> *Dedicated to Sanatana Dharma and the Preservation of Indian Cultural Heritage*

---

## 🚩 Overview

**Prashanti Paryatana** is a specialized spiritual and cultural pilgrimage web platform designed to prioritize simplicity, clarity, and unhurried spiritual devotion. It is built strictly using clean, modern **HTML5, CSS3, and Vanilla JavaScript**, requiring **zero build steps or dependencies**, making it 100% ready for instant deployment to **GitHub Pages**.

---

## 🌟 Key Travel Categories

Visitors discover spiritual journeys based on their preferred mode of travel or cultural interest:
1. **Bus Tours (`bus-tours.html`)**: Deluxe AC executive coach pilgrimages traversing regional temple clusters (Hoysala, Chola, Jyotirlingas, Western Ghats).
2. **Train Tours (`train-tours.html`)**: Sacred rail circuits aboard Vande Bharat and reserved express trains (Divya Kashi, Ayodhya, Jagannath Puri, Dakshin Divya Desam).
3. **Flight Packages (`flight-packages.html`)**: Char Dham aerial pilgrimages, VIP helicopter shuttles, Om Parvat & Adi Kailash aerial circuits, and Nepal Muktinath.
4. **Trekking Expeditions (`trekking-expeditions.html`)**: Guided high-altitude alpine trails to Gaumukh-Tapovan, Tungnath-Chandrashila (highest Shiva temple), and Kinnaur Kailash with certified mountaineering support.
5. **Cultural Travel (`cultural.html`)**: Dedicated portal for attending classical concerts (Carnatic, Hindustani, Bharatanatyam, Natyanjali) and a Classical Artist Temple Program Registration engine.
6. **Bike Rides (`bike-rides.html`)**: Sacred motorcycle expeditions across high-altitude mountain passes, spiritual ghat circuits, and remote Himalayan shrines.

---

## 🏛️ Knowledge Hub & Supporting Pages

- **Home (`index.html`)**: 10-section structured journey adhering strictly to traditional pilgrimage requirements.
- **About Us (`about.html`)**: Our sacred vows, dedication to Sanatana Dharma, and why we reject commercialized tourism.
- **Our Heritage (`heritage.html`)**: Architectural taxonomy (Dravida, Nagara, Vesara, Hoysala, Kalinga) and the Vedic science of *Tirtha Yatra*.
- **The Three Great Acharyas (`acharyas.html`)**: Biographies, sacred routes, and lineages of *Adi Shankaracharya*, *Sri Ramanujacharya*, and *Sri Madhvacharya*.
- **All Packages (`packages.html`)**: Complete filterable catalog across all travel modes.
- **Package Details (`package-detail.html?id=...`)**: Dynamic detail pages with Day-by-Day Itineraries, Sthala Purana, and direct enquiry modal.
- **Contact & Helpdesk (`contact.html`)**: Direct helpdesk, elder care requests, and FAQs.
- **Admin Dashboard (`admin.html`)**: Protected management portal (Default: User: `admin` | PIN: `sanskrit108`).

---

## 🚀 How to Deploy on GitHub (in 3 Simple Steps)

### Step 1: Initialize Git and Commit
Open a terminal in this project folder:
```bash
git init
git add .
git commit -m "Deploy Prashanti Paryatana website"
```

### Step 2: Push to Your GitHub Repository
Create a new public repository on [GitHub](https://github.com/new), then run:
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages
1. Go to your repository on GitHub.
2. Click **Settings** ➔ **Pages** (in the left sidebar).
3. Under **Build and deployment** ➔ **Source**:
   - **Option A (Automated GitHub Actions - Recommended)**: Select **GitHub Actions**. The included `.github/workflows/deploy.yml` will automatically build and publish your site!
   - **Option B (Classic Branch Deploy)**: Select **Deploy from a branch**, choose `main`, and folder `/ (root)`. Click **Save**.
4. In under 1 minute, your website will be live at:
   `https://YOUR_USERNAME.github.io/YOUR_REPOSITORY/`

---

## 💻 Local Preview

Run Python's built-in HTTP server:
```bash
python -m http.server 8080
```
Then open [http://localhost:8080](http://localhost:8080) in your browser.
