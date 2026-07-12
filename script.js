document.documentElement.classList.add("js");

const header = document.querySelector(".site-header");
const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.querySelectorAll(".site-nav a");
const faqItems = document.querySelectorAll(".faq-list details");
const yearNode = document.getElementById("year");

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

if (yearNode) {
  yearNode.textContent = new Date().getFullYear().toString();
}

// Motion budget: one scroll-triggered reveal on the bento cells,
// staggered, fires once. Nothing else animates.
const bentoCells = document.querySelectorAll(".bento-cell");

if (bentoCells.length && "IntersectionObserver" in window) {
  bentoCells.forEach((cell, index) => {
    cell.style.setProperty("--stagger", `${index * 80}ms`);
  });

  const bentoObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          bentoObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  bentoCells.forEach((cell) => bentoObserver.observe(cell));
} else {
  bentoCells.forEach((cell) => cell.classList.add("visible"));
}
