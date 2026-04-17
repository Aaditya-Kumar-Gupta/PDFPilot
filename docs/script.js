// ==================== NAV SCROLL ====================
const nav = document.getElementById('nav');
window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 20);
});

// ==================== HAMBURGER ====================
const hamburger = document.getElementById('hamburger');
const navMobile = document.getElementById('navMobile');
hamburger.addEventListener('click', () => {
  navMobile.classList.toggle('open');
});
navMobile.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => navMobile.classList.remove('open'));
});

// ==================== HERO SCREENSHOT ====================
window.addEventListener('load', () => {
  const heroImg = document.getElementById('heroScreenshot');
  if (heroImg) {
    if (typeof HERO_SCREENSHOT !== 'undefined') {
      heroImg.src = HERO_SCREENSHOT;
    } else if (typeof SCREENSHOTS !== 'undefined' && SCREENSHOTS.length > 0) {
      heroImg.src = SCREENSHOTS[0].src;
    }
  }
});

// ==================== GALLERY ====================
function buildGallery() {
  if (typeof SCREENSHOTS === 'undefined') return;
  const gallery = document.getElementById('gallery');
  if (!gallery) return;

  SCREENSHOTS.forEach((item, i) => {
    const card = document.createElement('div');
    card.className = 'gallery-card reveal';
    card.innerHTML = `
      <img class="gallery-card-img" src="${item.src}" alt="${item.title}" loading="lazy" />
      <div class="gallery-card-overlay">
        <span class="material-icons-round">zoom_in</span>
      </div>
      <div class="gallery-card-info">
        <div class="gallery-card-title">${item.title}</div>
        <div class="gallery-card-desc">${item.desc}</div>
      </div>
    `;
    card.addEventListener('click', () => openLightbox(i));
    gallery.appendChild(card);
  });
}

// ==================== LIGHTBOX ====================
let currentLightboxIndex = 0;

function openLightbox(index) {
  currentLightboxIndex = index;
  updateLightbox();
  document.getElementById('lightbox').classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  document.getElementById('lightbox').classList.remove('open');
  document.body.style.overflow = '';
}

function updateLightbox() {
  const item = SCREENSHOTS[currentLightboxIndex];
  document.getElementById('lightboxImg').src = item.src;
  document.getElementById('lightboxTitle').textContent = item.title;
  document.getElementById('lightboxDesc').textContent = item.desc;
}

document.getElementById('lightboxClose').addEventListener('click', closeLightbox);

document.getElementById('lightboxPrev').addEventListener('click', () => {
  currentLightboxIndex = (currentLightboxIndex - 1 + SCREENSHOTS.length) % SCREENSHOTS.length;
  updateLightbox();
});

document.getElementById('lightboxNext').addEventListener('click', () => {
  currentLightboxIndex = (currentLightboxIndex + 1) % SCREENSHOTS.length;
  updateLightbox();
});

document.getElementById('lightbox').addEventListener('click', (e) => {
  if (e.target === document.getElementById('lightbox')) closeLightbox();
});

document.addEventListener('keydown', (e) => {
  const lightbox = document.getElementById('lightbox');
  if (!lightbox.classList.contains('open')) return;
  if (e.key === 'Escape') closeLightbox();
  if (e.key === 'ArrowLeft') {
    currentLightboxIndex = (currentLightboxIndex - 1 + SCREENSHOTS.length) % SCREENSHOTS.length;
    updateLightbox();
  }
  if (e.key === 'ArrowRight') {
    currentLightboxIndex = (currentLightboxIndex + 1) % SCREENSHOTS.length;
    updateLightbox();
  }
});

// ==================== SCROLL REVEAL ====================
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

function observeReveal() {
  document.querySelectorAll('.reveal').forEach((el, i) => {
    el.style.transitionDelay = `${(i % 6) * 0.07}s`;
    observer.observe(el);
  });
}

// ==================== INIT ====================
document.addEventListener('DOMContentLoaded', () => {
  buildGallery();
  // Give DOM a moment then observe
  setTimeout(observeReveal, 100);

  // Add reveal to feature cards
  document.querySelectorAll('.feature-cat, .privacy-item, .feature-card-mini').forEach(el => {
    el.classList.add('reveal');
  });
  setTimeout(observeReveal, 150);
});
// ==================== TYPEWRITER ROTATE ====================
const words = ["Offline.", "Safe.", "Private."];
let wordIndex = 0;
let charIndex = 0;
let isDeleting = false;
const speed = 70;

function typeEffect() {
  const el = document.getElementById("typewriter");
  if (!el) return;

  const currentWord = words[wordIndex];

  if (!isDeleting) {
    el.textContent = currentWord.substring(0, charIndex + 1);
    charIndex++;

    if (charIndex === currentWord.length) {
      isDeleting = true;
      setTimeout(typeEffect, 1200);
      return;
    }

  } else {
    el.textContent = currentWord.substring(0, charIndex - 1);
    charIndex--;

    if (charIndex === 0) {
      isDeleting = false;
      wordIndex = (wordIndex + 1) % words.length;
    }
  }

  setTimeout(typeEffect, isDeleting ? 40 : speed);
}

document.addEventListener("DOMContentLoaded", typeEffect);