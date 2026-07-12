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
// staggered, fires once. Everything else below is pointer feedback
// (tilt, magnetism, border glow, click ripple), not load motion.
const bentoCells = document.querySelectorAll(".bento-cell");
const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
const finePointer = window.matchMedia("(hover: hover) and (pointer: fine)");

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
          setTimeout(() => enablePointerFeedback(entry.target), 700);
        }
      });
    },
    { threshold: 0.15 }
  );

  bentoCells.forEach((cell) => bentoObserver.observe(cell));
} else {
  bentoCells.forEach((cell) => {
    cell.classList.add("visible");
    enablePointerFeedback(cell);
  });
}

function enablePointerFeedback(cell) {
  if (reducedMotion.matches || !finePointer.matches || window.innerWidth <= 768) {
    return;
  }

  cell.style.transition = "transform 160ms ease-out";

  cell.addEventListener("mousemove", (event) => {
    const rect = cell.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;

    const rotateX = ((y - centerY) / centerY) * -4;
    const rotateY = ((x - centerX) / centerX) * 4;
    const magnetX = (x - centerX) * 0.04;
    const magnetY = (y - centerY) * 0.04;

    cell.style.transform =
      `perspective(1000px) translate(${magnetX.toFixed(1)}px, ${magnetY.toFixed(1)}px) ` +
      `rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg)`;

    cell.style.setProperty("--glow-x", `${((x / rect.width) * 100).toFixed(1)}%`);
    cell.style.setProperty("--glow-y", `${((y / rect.height) * 100).toFixed(1)}%`);
    cell.style.setProperty("--glow-i", "1");
  });

  cell.addEventListener("mouseleave", () => {
    cell.style.transform = "";
    cell.style.setProperty("--glow-i", "0");
  });

  cell.addEventListener("click", (event) => {
    const rect = cell.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    const maxDistance = Math.max(
      Math.hypot(x, y),
      Math.hypot(x - rect.width, y),
      Math.hypot(x, y - rect.height),
      Math.hypot(x - rect.width, y - rect.height)
    );

    const ripple = document.createElement("span");
    ripple.className = "cell-ripple";
    ripple.style.width = `${maxDistance * 2}px`;
    ripple.style.height = `${maxDistance * 2}px`;
    ripple.style.left = `${x - maxDistance}px`;
    ripple.style.top = `${y - maxDistance}px`;
    cell.appendChild(ripple);

    ripple.animate(
      [
        { transform: "scale(0)", opacity: 1 },
        { transform: "scale(1)", opacity: 0 }
      ],
      { duration: 700, easing: "ease-out" }
    ).onfinish = () => ripple.remove();
  });
}
