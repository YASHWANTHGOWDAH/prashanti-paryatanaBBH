import re
import glob

replacement = """  <!-- ================= WEBSITE LOADING PRELOADER (CINEMATIC BACKGROUND & MOVING LOGO) ================= -->
  <div id="sitePreloader" class="site-preloader" aria-label="Loading Prashanti Paryatana">
    <!-- Cinematic Background Image Crossfade Carousel -->
    <div class="preloader-bg-slideshow">
      <div class="preloader-bg-slide active" style="background-image: url('assets/loader/bg-1.jpg');"></div>
      <div class="preloader-bg-slide" style="background-image: url('assets/loader/bg-2.jpg');"></div>
      <div class="preloader-bg-slide" style="background-image: url('assets/loader/bg-3.jpg');"></div>
      <div class="preloader-bg-slide" style="background-image: url('assets/loader/bg-4.jpg');"></div>
      <div class="preloader-bg-slide" style="background-image: url('assets/loader/bg-5.jpg');"></div>
      <div class="preloader-overlay"></div>
    </div>

    <!-- Center Floating Animated Logo Badge & Content -->
    <div class="preloader-content">
      <div class="preloader-badge">
        <div class="preloader-aura-glow"></div>
        <div class="preloader-mandala-outer"></div>
        <div class="preloader-mandala-inner"></div>
        <div class="preloader-logo-wrap">
          <img src="assets/logo.png" alt="Prashanti Paryatana" class="preloader-logo" />
        </div>
      </div>

      <div class="preloader-text-group">
        <div class="preloader-sanskrit font-sanskrit-style">॥ सनातन संस्कृति यात्रा ॥</div>
        <h1 class="preloader-title">PRASHANTI PARYATANA</h1>
        <p class="preloader-tagline">Spiritual & Cultural Journeys Across Sacred Bharat</p>
      </div>

      <!-- Modern Progress Line & Counter -->
      <div class="preloader-status">
        <div class="preloader-progress-bar">
          <div id="preloaderProgressFill" class="preloader-progress-fill"></div>
        </div>
        <div class="preloader-status-text">
          <span id="preloaderPercent">0%</span>
          <span class="preloader-dot">•</span>
          <span id="preloaderPhase">Awakening Sacred Heritage...</span>
        </div>
      </div>

      <button type="button" class="preloader-skip-btn" id="preloaderSkipBtn" title="Enter Website">
        Enter Site <i class="fa-solid fa-arrow-right"></i>
      </button>
    </div>
  </div>"""

pattern = re.compile(r'<!--\s*=+\s*WEBSITE LOADING PRELOADER.*?</div>\s*</div>\s*</div>', re.DOTALL)

for fpath in glob.glob('C:/Users/yashw/Desktop/TASN  PP/TASN/*.html'):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    if 'preloader-bg-slideshow' in text:
        print(f'Already updated: {fpath}')
        continue
    new_text, n = pattern.subn(replacement, text)
    if n > 0:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f'Updated ({n}): {fpath}')
    else:
        print(f'No match: {fpath}')
