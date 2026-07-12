I have loaded tasteskill v2 (experimental) as my only source of design rules.

Brief:
- Site: Ansai Technologies marketing site (the live repo, vanilla HTML/CSS/JS)
- Mode: overhaul on the visual layer, preserve on copy and IA. Do not touch URL structure, nav labels, or the locked terms "digital infrastructure" and "organizations"
- Product: Ansai, the structural digital infrastructure layer for African organizations. First live product is EduManage, a multi-tenant school management platform
- Audience: decision-makers at Kenyan and African organizations (schools, institutions, SMEs) evaluating trust-first B2B infrastructure, not a consumer or agency audience
- Vibe words: confident, structural, restrained, trust-first B2B, not agency-playful, not consumer-flashy
- References: none external, the brand mark itself is the primary reference, see logo section below
- Avoid: orange or any color outside the locked palette below as a base or accent, three-equal-card feature rows, rainbow or multi-hue icon sets, decorative status dots, autoplaying carousels, em-dashes anywhere in copy, centered hero, section-numbering eyebrows

Locked decisions, do not re-litigate these, implement them:

Design tokens
- --navy: #111C27 (page background)
- --blue: #1C5CF5 (sole accent, used identically everywhere: CTAs, icons, featured tiles, links)
- --teal: #2DE8E8 (reserved for the logo mark only, must not appear anywhere else on the page)
- --white: #ffffff (primary text on dark)
- --muted: #8B98A8 (secondary text on dark)
- --muted-dim: #5A6C82 / #7A8595 (tertiary text, labels)
- Corner radius: 8px on buttons, 20px on cards, one scale per element type, no exceptions
- Nav: single line, max 80px height, default 64px

Hero
- Pattern: Asymmetric Split Hero. Headline and CTA left-aligned, not centered
- Right side: solid blue (--blue) panel that bleeds past its own column edge in a deliberate overlap, not a boxed-in image slot
- Headline max 2 lines desktop, subtext max 20 words and 4 lines, primary CTA visible without scroll
- No tagline, trust strip, or pricing teaser inside the hero itself, those live in sections below it

Feature grid
- Pattern: Bento Grid, exact cell count for the content, no empty filler tiles
- Every cell is its own rounded card (20px radius) with real gaps between tiles, never flush edges
- Cells differ in material, not just color: at most one cell uses the fully saturated --blue fill, the rest use a soft blue-tinted surface (rgba(28,92,245,0.09)) or the page's neutral surface
- No three-equal-card default, vary tile size (one larger tile, smaller tiles around it)

Icon row
- Use the GlassIcons component provided (GlassIcons.jsx, GlassIcons.css), already re-skinned to a single hue with tint-only depth variation, no per-item color prop, do not reintroduce multi-hue icons

Motion budget, homepage only
- One scroll-triggered fade/rise reveal on the bento grid cells, via IntersectionObserver, fires once, staggered by roughly 0.08s per cell
- Nothing else animates on load or on a loop
- Do not add CardSwap or Stepper to the homepage, both are reserved for future pages (case studies, onboarding) with actual sequential content to justify them

Step 1. Declare your design read in one sentence and the three dial values with one-line reasoning each. Given the brief above, expect variance around 7 to 8 for the asymmetric hero and bento, motion around 3 to 4 given the single-reveal budget, density around 3 to 4. Stop and wait for confirmation before writing code.

Step 2 (after confirmation). Implement the hero, bento feature grid, and icon row exactly as specified above. Reuse existing page sections and copy untouched except where the locked tokens require a color or radius change. Do not invent new sections, new copy, or new components beyond what's listed.

Step 3. Run in writing, every box marked pass or fail with a one-line justification:
- Em-dash audit: zero em-dashes anywhere in output, headlines, labels, body, alt text
- Color Consistency Lock: --blue is the only accent, used identically in every section, --teal appears nowhere outside the logo
- Shape Consistency Lock: 8px buttons and 20px cards applied everywhere, no exceptions
- Bento Cell Count: cell count matches content count exactly, no empty tiles
- Motion Motivated: the single reveal animation is justified in one sentence, no other motion shipped
- No Duplicate CTA Intent: one label per intent across nav, hero, and footer
- Button Contrast Check: every CTA text passes WCAG AA against its background


## Integrate the <MagicBento /> component from React Bits

You are helping integrate an open-source React component into an existing application.

### Component: MagicBento
### Variant: JavaScript + CSS
### Dependencies: gsap

---

### Usage Example
```jsx
import MagicBento from './MagicBento'

<MagicBento 
  textAutoHide={true}
  enableStars={false}
  enableSpotlight={false}
  enableBorderGlow={true}
  enableTilt
  enableMagnetism
  clickEffect={true}
  spotlightRadius={300}
  particleCount={12}
  glowColor="132, 0, 255"
/>
```

### Props
| Prop | Type | Default | Description |
|------|------|---------|-------------|
| textAutoHide | boolean | true | Whether text content should auto-hide on hover |
| enableStars | boolean | true | Enable particle star animation effect |
| enableSpotlight | boolean | true | Enable spotlight cursor following effect |
| enableBorderGlow | boolean | true | Enable border glow effect that follows cursor |
| disableAnimations | boolean | false | Disable all animations (automatically enabled on mobile) |
| spotlightRadius | number | 300 | Radius of the spotlight effect in pixels |
| particleCount | number | 12 | Number of particles in the star animation |
| enableTilt | boolean | false | Enable 3D tilt effect on card hover |
| glowColor | string | "132, 0, 255" | RGB color values for glow effects (without rgba wrapper) |
| clickEffect | boolean | true | Enable ripple effect on card click |
| enableMagnetism | boolean | true | Enable subtle card attraction to cursor |

### Full Component Source
```jsx
import { useRef, useEffect, useCallback, useState } from 'react';
import { gsap } from 'gsap';
import './MagicBento.css';

const DEFAULT_PARTICLE_COUNT = 12;
const DEFAULT_SPOTLIGHT_RADIUS = 300;
const DEFAULT_GLOW_COLOR = '132, 0, 255';
const MOBILE_BREAKPOINT = 768;

const cardData = [
  {
    color: '#120F17',
    title: 'Analytics',
    description: 'Track user behavior',
    label: 'Insights'
  },
  {
    color: '#120F17',
    title: 'Dashboard',
    description: 'Centralized data view',
    label: 'Overview'
  },
  {
    color: '#120F17',
    title: 'Collaboration',
    description: 'Work together seamlessly',
    label: 'Teamwork'
  },
  {
    color: '#120F17',
    title: 'Automation',
    description: 'Streamline workflows',
    label: 'Efficiency'
  },
  {
    color: '#120F17',
    title: 'Integration',
    description: 'Connect favorite tools',
    label: 'Connectivity'
  },
  {
    color: '#120F17',
    title: 'Security',
    description: 'Enterprise-grade protection',
    label: 'Protection'
  }
];

const createParticleElement = (x, y, color = DEFAULT_GLOW_COLOR) => {
  const el = document.createElement('div');
  el.className = 'particle';
  el.style.cssText = `
    position: absolute;
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background: rgba(${color}, 1);
    box-shadow: 0 0 6px rgba(${color}, 0.6);
    pointer-events: none;
    z-index: 100;
    left: ${x}px;
    top: ${y}px;
  `;
  return el;
};

const calculateSpotlightValues = radius => ({
  proximity: radius * 0.5,
  fadeDistance: radius * 0.75
});

const updateCardGlowProperties = (card, mouseX, mouseY, glow, radius) => {
  const rect = card.getBoundingClientRect();
  const relativeX = ((mouseX - rect.left) / rect.width) * 100;
  const relativeY = ((mouseY - rect.top) / rect.height) * 100;

  card.style.setProperty('--glow-x', `${relativeX}%`);
  card.style.setProperty('--glow-y', `${relativeY}%`);
  card.style.setProperty('--glow-intensity', glow.toString());
  card.style.setProperty('--glow-radius', `${radius}px`);
};

const ParticleCard = ({
  children,
  className = '',
  disableAnimations = false,
  style,
  particleCount = DEFAULT_PARTICLE_COUNT,
  glowColor = DEFAULT_GLOW_COLOR,
  enableTilt = true,
  clickEffect = false,
  enableMagnetism = false
}) => {
  const cardRef = useRef(null);
  const particlesRef = useRef([]);
  const timeoutsRef = useRef([]);
  const isHoveredRef = useRef(false);
  const memoizedParticles = useRef([]);
  const particlesInitialized = useRef(false);
  const magnetismAnimationRef = useRef(null);

  const initializeParticles = useCallback(() => {
    if (particlesInitialized.current || !cardRef.current) return;

    const { width, height } = cardRef.current.getBoundingClientRect();
    memoizedParticles.current = Array.from({ length: particleCount }, () =>
      createParticleElement(Math.random() * width, Math.random() * height, glowColor)
    );
    particlesInitialized.current = true;
  }, [particleCount, glowColor]);

  const clearAllParticles = useCallback(() => {
    timeoutsRef.current.forEach(clearTimeout);
    timeoutsRef.current = [];
    magnetismAnimationRef.current?.kill();

    particlesRef.current.forEach(particle => {
      gsap.to(particle, {
        scale: 0,
        opacity: 0,
        duration: 0.3,
        ease: 'back.in(1.7)',
        onComplete: () => {
          particle.parentNode?.removeChild(particle);
        }
      });
    });
    particlesRef.current = [];
  }, []);

  const animateParticles = useCallback(() => {
    if (!cardRef.current || !isHoveredRef.current) return;

    if (!particlesInitialized.current) {
      initializeParticles();
    }

    memoizedParticles.current.forEach((particle, index) => {
      const timeoutId = setTimeout(() => {
        if (!isHoveredRef.current || !cardRef.current) return;

        const clone = particle.cloneNode(true);
        cardRef.current.appendChild(clone);
        particlesRef.current.push(clone);

        gsap.fromTo(clone, { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.3, ease: 'back.out(1.7)' });

        gsap.to(clone, {
          x: (Math.random() - 0.5) * 100,
          y: (Math.random() - 0.5) * 100,
          rotation: Math.random() * 360,
          duration: 2 + Math.random() * 2,
          ease: 'none',
          repeat: -1,
          yoyo: true
        });

        gsap.to(clone, {
          opacity: 0.3,
          duration: 1.5,
          ease: 'power2.inOut',
          repeat: -1,
          yoyo: true
        });
      }, index * 100);

      timeoutsRef.current.push(timeoutId);
    });
  }, [initializeParticles]);

  useEffect(() => {
    if (disableAnimations || !cardRef.current) return;

    const element = cardRef.current;

    const handleMouseEnter = () => {
      isHoveredRef.current = true;
      animateParticles();

      if (enableTilt) {
        gsap.to(element, {
          rotateX: 5,
          rotateY: 5,
          duration: 0.3,
          ease: 'power2.out',
          transformPerspective: 1000
        });
      }
    };

    const handleMouseLeave = () => {
      isHoveredRef.current = false;
      clearAllParticles();

      if (enableTilt) {
        gsap.to(element, {
          rotateX: 0,
          rotateY: 0,
          duration: 0.3,
          ease: 'power2.out'
        });
      }

      if (enableMagnetism) {
        gsap.to(element, {
          x: 0,
          y: 0,
          duration: 0.3,
          ease: 'power2.out'
        });
      }
    };

    const handleMouseMove = e => {
      if (!enableTilt && !enableMagnetism) return;

      const rect = element.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      if (enableTilt) {
        const rotateX = ((y - centerY) / centerY) * -10;
        const rotateY = ((x - centerX) / centerX) * 10;

        gsap.to(element, {
          rotateX,
          rotateY,
          duration: 0.1,
          ease: 'power2.out',
          transformPerspective: 1000
        });
      }

      if (enableMagnetism) {
        const magnetX = (x - centerX) * 0.05;
        const magnetY = (y - centerY) * 0.05;

        magnetismAnimationRef.current = gsap.to(element, {
          x: magnetX,
          y: magnetY,
          duration: 0.3,
          ease: 'power2.out'
        });
      }
    };

    const handleClick = e => {
      if (!clickEffect) return;

      const rect = element.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      const maxDistance = Math.max(
        Math.hypot(x, y),
        Math.hypot(x - rect.width, y),
        Math.hypot(x, y - rect.height),
        Math.hypot(x - rect.width, y - rect.height)
      );

      const ripple = document.createElement('div');
      ripple.style.cssText = `
        position: absolute;
        width: ${maxDistance * 2}px;
        height: ${maxDistance * 2}px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(${glowColor}, 0.4) 0%, rgba(${glowColor}, 0.2) 30%, transparent 70%);
        left: ${x - maxDistance}px;
        top: ${y - maxDistance}px;
        pointer-events: none;
        z-index: 1000;
      `;

      element.appendChild(ripple);

      gsap.fromTo(
        ripple,
        {
          scale: 0,
          opacity: 1
        },
        {
          scale: 1,
          opacity: 0,
          duration: 0.8,
          ease: 'power2.out',
          onComplete: () => ripple.remove()
        }
      );
    };

    element.addEventListener('mouseenter', handleMouseEnter);
    element.addEventListener('mouseleave', handleMouseLeave);
    element.addEventListener('mousemove', handleMouseMove);
    element.addEventListener('click', handleClick);

    return () => {
      isHoveredRef.current = false;
      element.removeEventListener('mouseenter', handleMouseEnter);
      element.removeEventListener('mouseleave', handleMouseLeave);
      element.removeEventListener('mousemove', handleMouseMove);
      element.removeEventListener('click', handleClick);
      clearAllParticles();
    };
  }, [animateParticles, clearAllParticles, disableAnimations, enableTilt, enableMagnetism, clickEffect, glowColor]);

  return (
    <div
      ref={cardRef}
      className={`${className} particle-container`}
      style={{ ...style, position: 'relative', overflow: 'hidden' }}
    >
      {children}
    </div>
  );
};

const GlobalSpotlight = ({
  gridRef,
  disableAnimations = false,
  enabled = true,
  spotlightRadius = DEFAULT_SPOTLIGHT_RADIUS,
  glowColor = DEFAULT_GLOW_COLOR
}) => {
  const spotlightRef = useRef(null);
  const isInsideSection = useRef(false);

  useEffect(() => {
    if (disableAnimations || !gridRef?.current || !enabled) return;

    const spotlight = document.createElement('div');
    spotlight.className = 'global-spotlight';
    spotlight.style.cssText = `
      position: fixed;
      width: 800px;
      height: 800px;
      border-radius: 50%;
      pointer-events: none;
      background: radial-gradient(circle,
        rgba(${glowColor}, 0.15) 0%,
        rgba(${glowColor}, 0.08) 15%,
        rgba(${glowColor}, 0.04) 25%,
        rgba(${glowColor}, 0.02) 40%,
        rgba(${glowColor}, 0.01) 65%,
        transparent 70%
      );
      z-index: 200;
      opacity: 0;
      transform: translate(-50%, -50%);
      mix-blend-mode: screen;
    `;
    document.body.appendChild(spotlight);
    spotlightRef.current = spotlight;

    const handleMouseMove = e => {
      if (!spotlightRef.current || !gridRef.current) return;

      const section = gridRef.current.closest('.bento-section');
      const rect = section?.getBoundingClientRect();
      const mouseInside =
        rect && e.clientX >= rect.left && e.clientX <= rect.right && e.clientY >= rect.top && e.clientY <= rect.bottom;

      isInsideSection.current = mouseInside || false;
      const cards = gridRef.current.querySelectorAll('.magic-bento-card');

      if (!mouseInside) {
        gsap.to(spotlightRef.current, {
          opacity: 0,
          duration: 0.3,
          ease: 'power2.out'
        });
        cards.forEach(card => {
          card.style.setProperty('--glow-intensity', '0');
        });
        return;
      }

      const { proximity, fadeDistance } = calculateSpotlightValues(spotlightRadius);
      let minDistance = Infinity;

      cards.forEach(card => {
        const cardElement = card;
        const cardRect = cardElement.getBoundingClientRect();
        const centerX = cardRect.left + cardRect.width / 2;
        const centerY = cardRect.top + cardRect.height / 2;
        const distance =
          Math.hypot(e.clientX - centerX, e.clientY - centerY) - Math.max(cardRect.width, cardRect.height) / 2;
        const effectiveDistance = Math.max(0, distance);

        minDistance = Math.min(minDistance, effectiveDistance);

        let glowIntensity = 0;
        if (effectiveDistance <= proximity) {
          glowIntensity = 1;
        } else if (effectiveDistance <= fadeDistance) {
          glowIntensity = (fadeDistance - effectiveDistance) / (fadeDistance - proximity);
        }

        updateCardGlowProperties(cardElement, e.clientX, e.clientY, glowIntensity, spotlightRadius);
      });

      gsap.to(spotlightRef.current, {
        left: e.clientX,
        top: e.clientY,
        duration: 0.1,
        ease: 'power2.out'
      });

      const targetOpacity =
        minDistance <= proximity
          ? 0.8
          : minDistance <= fadeDistance
            ? ((fadeDistance - minDistance) / (fadeDistance - proximity)) * 0.8
            : 0;

      gsap.to(spotlightRef.current, {
        opacity: targetOpacity,
        duration: targetOpacity > 0 ? 0.2 : 0.5,
        ease: 'power2.out'
      });
    };

    const handleMouseLeave = () => {
      isInsideSection.current = false;
      gridRef.current?.querySelectorAll('.magic-bento-card').forEach(card => {
        card.style.setProperty('--glow-intensity', '0');
      });
      if (spotlightRef.current) {
        gsap.to(spotlightRef.current, {
          opacity: 0,
          duration: 0.3,
          ease: 'power2.out'
        });
      }
    };

    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('mouseleave', handleMouseLeave);

    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseleave', handleMouseLeave);
      spotlightRef.current?.parentNode?.removeChild(spotlightRef.current);
    };
  }, [gridRef, disableAnimations, enabled, spotlightRadius, glowColor]);

  return null;
};

const BentoCardGrid = ({ children, gridRef }) => (
  <div className="card-grid bento-section" ref={gridRef}>
    {children}
  </div>
);

const useMobileDetection = () => {
  const [isMobile, setIsMobile] = useState(false);

  useEffect(() => {
    const checkMobile = () => setIsMobile(window.innerWidth <= MOBILE_BREAKPOINT);

    checkMobile();
    window.addEventListener('resize', checkMobile);

    return () => window.removeEventListener('resize', checkMobile);
  }, []);

  return isMobile;
};

const MagicBento = ({
  textAutoHide = true,
  enableStars = true,
  enableSpotlight = true,
  enableBorderGlow = true,
  disableAnimations = false,
  spotlightRadius = DEFAULT_SPOTLIGHT_RADIUS,
  particleCount = DEFAULT_PARTICLE_COUNT,
  enableTilt = false,
  glowColor = DEFAULT_GLOW_COLOR,
  clickEffect = true,
  enableMagnetism = true
}) => {
  const gridRef = useRef(null);
  const isMobile = useMobileDetection();
  const shouldDisableAnimations = disableAnimations || isMobile;

  return (
    <>
      {enableSpotlight && (
        <GlobalSpotlight
          gridRef={gridRef}
          disableAnimations={shouldDisableAnimations}
          enabled={enableSpotlight}
          spotlightRadius={spotlightRadius}
          glowColor={glowColor}
        />
      )}

      <BentoCardGrid gridRef={gridRef}>
        {cardData.map((card, index) => {
          const baseClassName = `magic-bento-card ${textAutoHide ? 'magic-bento-card--text-autohide' : ''} ${enableBorderGlow ? 'magic-bento-card--border-glow' : ''}`;
          const cardProps = {
            className: baseClassName,
            style: {
              backgroundColor: card.color,
              '--glow-color': glowColor
            }
          };

          if (enableStars) {
            return (
              <ParticleCard
                key={index}
                {...cardProps}
                disableAnimations={shouldDisableAnimations}
                particleCount={particleCount}
                glowColor={glowColor}
                enableTilt={enableTilt}
                clickEffect={clickEffect}
                enableMagnetism={enableMagnetism}
              >
                <div className="magic-bento-card__header">
                  <div className="magic-bento-card__label">{card.label}</div>
                </div>
                <div className="magic-bento-card__content">
                  <h2 className="magic-bento-card__title">{card.title}</h2>
                  <p className="magic-bento-card__description">{card.description}</p>
                </div>
              </ParticleCard>
            );
          }

          return (
            <div
              key={index}
              {...cardProps}
              ref={el => {
                if (!el) return;

                const handleMouseMove = e => {
                  if (shouldDisableAnimations) return;

                  const rect = el.getBoundingClientRect();
                  const x = e.clientX - rect.left;
                  const y = e.clientY - rect.top;
                  const centerX = rect.width / 2;
                  const centerY = rect.height / 2;

                  if (enableTilt) {
                    const rotateX = ((y - centerY) / centerY) * -10;
                    const rotateY = ((x - centerX) / centerX) * 10;
                    gsap.to(el, {
                      rotateX,
                      rotateY,
                      duration: 0.1,
                      ease: 'power2.out',
                      transformPerspective: 1000
                    });
                  }

                  if (enableMagnetism) {
                    const magnetX = (x - centerX) * 0.05;
                    const magnetY = (y - centerY) * 0.05;
                    gsap.to(el, {
                      x: magnetX,
                      y: magnetY,
                      duration: 0.3,
                      ease: 'power2.out'
                    });
                  }
                };

                const handleMouseLeave = () => {
                  if (shouldDisableAnimations) return;

                  if (enableTilt) {
                    gsap.to(el, {
                      rotateX: 0,
                      rotateY: 0,
                      duration: 0.3,
                      ease: 'power2.out'
                    });
                  }

                  if (enableMagnetism) {
                    gsap.to(el, {
                      x: 0,
                      y: 0,
                      duration: 0.3,
                      ease: 'power2.out'
                    });
                  }
                };

                const handleClick = e => {
                  if (!clickEffect || shouldDisableAnimations) return;

                  const rect = el.getBoundingClientRect();
                  const x = e.clientX - rect.left;
                  const y = e.clientY - rect.top;

                  const maxDistance = Math.max(
                    Math.hypot(x, y),
                    Math.hypot(x - rect.width, y),
                    Math.hypot(x, y - rect.height),
                    Math.hypot(x - rect.width, y - rect.height)
                  );

                  const ripple = document.createElement('div');
                  ripple.style.cssText = `
                    position: absolute;
                    width: ${maxDistance * 2}px;
                    height: ${maxDistance * 2}px;
                    border-radius: 50%;
                    background: radial-gradient(circle, rgba(${glowColor}, 0.4) 0%, rgba(${glowColor}, 0.2) 30%, transparent 70%);
                    left: ${x - maxDistance}px;
                    top: ${y - maxDistance}px;
                    pointer-events: none;
                    z-index: 1000;
                  `;

                  el.appendChild(ripple);

                  gsap.fromTo(
                    ripple,
                    {
                      scale: 0,
                      opacity: 1
                    },
                    {
                      scale: 1,
                      opacity: 0,
                      duration: 0.8,
                      ease: 'power2.out',
                      onComplete: () => ripple.remove()
                    }
                  );
                };

                el.addEventListener('mousemove', handleMouseMove);
                el.addEventListener('mouseleave', handleMouseLeave);
                el.addEventListener('click', handleClick);
              }}
            >
              <div className="magic-bento-card__header">
                <div className="magic-bento-card__label">{card.label}</div>
              </div>
              <div className="magic-bento-card__content">
                <h2 className="magic-bento-card__title">{card.title}</h2>
                <p className="magic-bento-card__description">{card.description}</p>
              </div>
            </div>
          );
        })}
      </BentoCardGrid>
    </>
  );
};

export default MagicBento;

```

### Component CSS
```css
:root {
  --hue: 27;
  --sat: 69%;
  --white: hsl(0, 0%, 100%);
  --purple-primary: rgba(132, 0, 255, 1);
  --purple-glow: rgba(132, 0, 255, 0.2);
  --purple-border: rgba(132, 0, 255, 0.8);
  --border-color: #2F293A;
  --background-dark: #120F17;
  color-scheme: light dark;
}

.card-grid {
  display: grid;
  gap: 0.5em;
  padding: 0.75em;
  max-width: 54em;
  font-size: clamp(1rem, 0.9rem + 0.5vw, 1.5rem);
}

.magic-bento-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
  aspect-ratio: 4/3;
  min-height: 200px;
  width: 100%;
  max-width: 100%;
  padding: 1.25em;
  border-radius: 20px;
  border: 1px solid var(--border-color);
  background: var(--background-dark);
  font-weight: 300;
  overflow: hidden;
  transition: all 0.3s ease;

  --glow-x: 50%;
  --glow-y: 50%;
  --glow-intensity: 0;
  --glow-radius: 200px;
}

.magic-bento-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.magic-bento-card__header,
.magic-bento-card__content {
  display: flex;
  position: relative;
  color: var(--white);
}

.magic-bento-card__header {
  gap: 0.75em;
  justify-content: space-between;
}

.magic-bento-card__content {
  flex-direction: column;
}

.magic-bento-card__label {
  font-size: 16px;
}

.magic-bento-card__title,
.magic-bento-card__description {
  --clamp-title: 1;
  --clamp-desc: 2;
}

.magic-bento-card__title {
  font-weight: 400;
  font-size: 16px;
  margin: 0 0 0.25em;
}

.magic-bento-card__description {
  font-size: 12px;
  line-height: 1.2;
  opacity: 0.9;
}

.magic-bento-card--text-autohide .magic-bento-card__title,
.magic-bento-card--text-autohide .magic-bento-card__description {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

.magic-bento-card--text-autohide .magic-bento-card__title {
  -webkit-line-clamp: var(--clamp-title);
  line-clamp: var(--clamp-title);
}

.magic-bento-card--text-autohide .magic-bento-card__description {
  -webkit-line-clamp: var(--clamp-desc);
  line-clamp: var(--clamp-desc);
}

@media (max-width: 599px) {
  .card-grid {
    grid-template-columns: 1fr;
    width: 90%;
    margin: 0 auto;
    padding: 0.5em;
  }

  .magic-bento-card {
    width: 100%;
    min-height: 180px;
  }
}

@media (min-width: 600px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .card-grid {
    grid-template-columns: repeat(4, 1fr);
  }

  .magic-bento-card:nth-child(3) {
    grid-column: span 2;
    grid-row: span 2;
  }

  .magic-bento-card:nth-child(4) {
    grid-column: 1 / span 2;
    grid-row: 2 / span 2;
  }

  .magic-bento-card:nth-child(6) {
    grid-column: 4;
    grid-row: 3;
  }
}

/* Border glow effect */
.magic-bento-card--border-glow::after {
  content: '';
  position: absolute;
  inset: 0;
  padding: 6px;
  background: radial-gradient(
    var(--glow-radius) circle at var(--glow-x) var(--glow-y),
    rgba(132, 0, 255, calc(var(--glow-intensity) * 0.8)) 0%,
    rgba(132, 0, 255, calc(var(--glow-intensity) * 0.4)) 30%,
    transparent 60%
  );
  border-radius: inherit;
  -webkit-mask:
    linear-gradient(#fff 0 0) content-box,
    linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask:
    linear-gradient(#fff 0 0) content-box,
    linear-gradient(#fff 0 0);
  mask-composite: exclude;
  pointer-events: none;
  opacity: 1;
  transition: opacity 0.3s ease;
  z-index: 1;
}

.magic-bento-card--border-glow:hover::after {
  opacity: 1;
}

.magic-bento-card--border-glow:hover {
  box-shadow:
    0 4px 20px rgba(46, 24, 78, 0.4),
    0 0 30px var(--purple-glow);
}

.particle-container {
  position: relative;
  overflow: hidden;
}

.particle::before {
  content: '';
  position: absolute;
  top: -2px;
  left: -2px;
  right: -2px;
  bottom: -2px;
  background: rgba(132, 0, 255, 0.2);
  border-radius: 50%;
  z-index: -1;
}

.particle-container:hover {
  box-shadow:
    0 4px 20px rgba(46, 24, 78, 0.2),
    0 0 30px var(--purple-glow);
}

/* Global spotlight styles */
.global-spotlight {
  mix-blend-mode: screen;
  will-change: transform, opacity;
  z-index: 200 !important;
  pointer-events: none;
}

.bento-section {
  position: relative;
  user-select: none;
}

```

### Integration Instructions
1. Install any listed dependencies.
2. Copy the component source into the appropriate directory in the project.
3. Import the CSS file alongside the component.
4. Import and render the component using the usage example above as a starting point.
5. Adjust props as needed for the specific use case — refer to the props table for all available options.


## Integrate the <AnimatedContent /> component from React Bits

You are helping integrate an open-source React component into an existing application.

### Component: AnimatedContent
### Variant: JavaScript + CSS
### Dependencies: gsap

---

### Usage Example
```jsx
import AnimatedContent from './AnimatedContent'

<AnimatedContent
  distance={150}
  direction="horizontal"
  reverse={false}
  duration={1.2}
  ease="bounce.out"
  initialOpacity={0.2}
  animateOpacity
  scale={1.1}
  threshold={0.2}
  delay={0.3}
>
  <div>Content to Animate</div>
</AnimatedContent>
```

### Props
| Prop | Type | Default | Description |
|------|------|---------|-------------|
| children | ReactNode | — | The content to be animated. |
| container | string | HTMLElement | null | The scroll container to use for ScrollTrigger. Can be a selector string or an HTMLElement. Defaults to main container. Uses auto-detection (for snap-main-container id) if not provided. |
| distance | number | 100 | Distance (in pixels) the component moves during animation. |
| direction | string | "vertical" | Animation direction. Can be "vertical" or "horizontal". |
| reverse | boolean | false | Whether the animation moves in the reverse direction. |
| duration | number | 0.8 | Duration of the animation in seconds. |
| ease | string | "power3.out" | GSAP easing function for the animation. |
| initialOpacity | number | 0 | Initial opacity before animation begins. |
| animateOpacity | boolean | true | Whether to animate opacity during transition. |
| scale | number | 1 | Initial scale of the component. |
| threshold | number | 0.1 | Intersection threshold to trigger animation (0-1). |
| delay | number | 0 | Delay before animation starts (in seconds). |
| onComplete | function | undefined | Callback function called when animation completes. |
| dissappearAfter | number | 0 | Time in seconds after which the content will disappear. Disabled if set to 0. |
| disappearDuration | number | 0.5 | Duration of the disappearance animation in seconds. |
| disappearEase | string | "power3.in" | GSAP easing function for the disappearance animation. |
| onDisappearanceComplete | function | undefined | Callback function called when disappearance animation completes. |
| className | string | '' | Additional CSS classes to apply to the animated component. |

### Full Component Source
```jsx
import { useRef, useEffect } from 'react';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

const AnimatedContent = ({
  children,
  container,
  distance = 100,
  direction = 'vertical',
  reverse = false,
  duration = 0.8,
  ease = 'power3.out',
  initialOpacity = 0,
  animateOpacity = true,
  scale = 1,
  threshold = 0.1,
  delay = 0,
  disappearAfter = 0,
  disappearDuration = 0.5,
  disappearEase = 'power3.in',
  onComplete,
  onDisappearanceComplete,
  className = '',
  ...props
}) => {
  const ref = useRef(null);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;

    let scrollerTarget = container || document.getElementById('snap-main-container') || null;

    if (typeof scrollerTarget === 'string') {
      scrollerTarget = document.querySelector(scrollerTarget);
    }

    const axis = direction === 'horizontal' ? 'x' : 'y';
    const offset = reverse ? -distance : distance;
    const startPct = (1 - threshold) * 100;

    gsap.set(el, {
      [axis]: offset,
      scale,
      opacity: animateOpacity ? initialOpacity : 1,
      visibility: 'visible'
    });

    const tl = gsap.timeline({
      paused: true,
      delay,
      onComplete: () => {
        if (onComplete) onComplete();
        if (disappearAfter > 0) {
          gsap.to(el, {
            [axis]: reverse ? distance : -distance,
            scale: 0.8,
            opacity: animateOpacity ? initialOpacity : 0,
            delay: disappearAfter,
            duration: disappearDuration,
            ease: disappearEase,
            onComplete: () => onDisappearanceComplete?.()
          });
        }
      }
    });

    tl.to(el, {
      [axis]: 0,
      scale: 1,
      opacity: 1,
      duration,
      ease
    });

    const st = ScrollTrigger.create({
      trigger: el,
      scroller: scrollerTarget,
      start: `top ${startPct}%`,
      once: true,
      onEnter: () => tl.play()
    });

    return () => {
      st.kill();
      tl.kill();
    };
  }, [
    container,
    distance,
    direction,
    reverse,
    duration,
    ease,
    initialOpacity,
    animateOpacity,
    scale,
    threshold,
    delay,
    disappearAfter,
    disappearDuration,
    disappearEase,
    onComplete,
    onDisappearanceComplete
  ]);

  return (
    <div ref={ref} className={className} style={{ visibility: 'hidden' }} {...props}>
      {children}
    </div>
  );
};

export default AnimatedContent;

```

### Integration Instructions
1. Install any listed dependencies.
2. Copy the component source into the appropriate directory in the project.
3. Import and render the component using the usage example above as a starting point.
4. Adjust props as needed for the specific use case — refer to the props table for all available options.
