const header = document.querySelector(".site-header");
const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.querySelectorAll(".site-nav a");
const counters = document.querySelectorAll(".metric-number");
const faqItems = document.querySelectorAll(".faq-list details");

if (navToggle && header) {
  navToggle.addEventListener("click", () => {
    const expanded = navToggle.getAttribute("aria-expanded") === "true";
    navToggle.setAttribute("aria-expanded", String(!expanded));
    header.classList.toggle("menu-open", !expanded);
  });

  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      navToggle.setAttribute("aria-expanded", "false");
      header.classList.remove("menu-open");
    });
  });
}

const counterObserver = new IntersectionObserver(
  (entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) {
        return;
      }

      const node = entry.target;
      const target = Number(node.getAttribute("data-target"));
      const duration = 1200;
      const start = performance.now();

      const tick = (time) => {
        const progress = Math.min((time - start) / duration, 1);
        node.textContent = Math.floor(progress * target).toString();
        if (progress < 1) {
          requestAnimationFrame(tick);
          return;
        }
        node.textContent = target.toString();
      };

      requestAnimationFrame(tick);
      observer.unobserve(node);
    });
  },
  { threshold: 0.45 }
);

counters.forEach((counter) => counterObserver.observe(counter));

faqItems.forEach((item) => {
  item.addEventListener("toggle", () => {
    if (!item.open) {
      return;
    }

    faqItems.forEach((other) => {
      if (other !== item) {
        other.open = false;
      }
    });
  });
});

// ===== Dynamic Eyebrow: Auto-updating Date =====
const eyebrowDate = document.querySelector(".eyebrow-date");
if (eyebrowDate) {
  const updateDate = () => {
    const now = new Date();
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    eyebrowDate.textContent = now.toLocaleDateString('en-US', options);
  };
  updateDate();
  // Update date at midnight
  const msUntilMidnight = new Date().setHours(24, 0, 0, 0) - Date.now();
  setTimeout(() => {
    updateDate();
    setInterval(updateDate, 86400000); // Update daily
  }, msUntilMidnight);
}

// ===== Scroll-triggered Animations =====
const revealElements = document.querySelectorAll(
  '.section-heading, .testimonial-card, .blog-card, .plan-card, ' +
  '.proof-card, .security-list article, .integration-cloud span, ' +
  '.metrics-panel, .faq-list details'
);

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  },
  { threshold: 0.1, rootMargin: '0px 0px -50px 0px' }
);

revealElements.forEach((el) => revealObserver.observe(el));
