---
name: Aetheric Intelligence
colors:
  surface: '#111319'
  surface-dim: '#111319'
  surface-bright: '#373940'
  surface-container-lowest: '#0c0e14'
  surface-container-low: '#191b22'
  surface-container: '#1e1f26'
  surface-container-high: '#282a30'
  surface-container-highest: '#33343b'
  on-surface: '#e2e2eb'
  on-surface-variant: '#c3c6d7'
  inverse-surface: '#e2e2eb'
  inverse-on-surface: '#2e3037'
  outline: '#8d90a0'
  outline-variant: '#434655'
  surface-tint: '#b4c5ff'
  primary: '#b4c5ff'
  on-primary: '#002a78'
  primary-container: '#2563eb'
  on-primary-container: '#eeefff'
  inverse-primary: '#0053db'
  secondary: '#c0c1ff'
  on-secondary: '#1000a9'
  secondary-container: '#3131c0'
  on-secondary-container: '#b0b2ff'
  tertiary: '#b9c8de'
  on-tertiary: '#233143'
  tertiary-container: '#5f6e82'
  on-tertiary-container: '#e8f1ff'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b4c5ff'
  on-primary-fixed: '#00174b'
  on-primary-fixed-variant: '#003ea8'
  secondary-fixed: '#e1e0ff'
  secondary-fixed-dim: '#c0c1ff'
  on-secondary-fixed: '#07006c'
  on-secondary-fixed-variant: '#2f2ebe'
  tertiary-fixed: '#d4e4fa'
  tertiary-fixed-dim: '#b9c8de'
  on-tertiary-fixed: '#0d1c2d'
  on-tertiary-fixed-variant: '#39485a'
  background: '#111319'
  on-background: '#e2e2eb'
  surface-variant: '#33343b'
typography:
  display-lg:
    fontFamily: Outfit
    fontSize: 48px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Outfit
    fontSize: 32px
    fontWeight: '300'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Outfit
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Outfit
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Outfit
    fontSize: 18px
    fontWeight: '300'
    lineHeight: '1.6'
  body-md:
    fontFamily: Outfit
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Outfit
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  mono-label:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  container-max: 1440px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style
The design system establishes a high-fidelity environment for enterprise-grade AI orchestration. It moves away from the common "cyberpunk" aesthetic toward an editorial, high-end professional identity. The brand personality is authoritative yet calm—acting as a silent, intelligent partner rather than a flashy tool.

The visual style is **Sophisticated Glassmorphism**. It utilizes matte surfaces, refined translucency, and precise, thin-stroke architecture to create a sense of depth and intelligence. The aesthetic is "quiet luxury" for software: spacious, high-contrast, and meticulously structured.

## Colors
This design system utilizes a palette of "Intellectual Tones." The foundation is a matte charcoal-blue background that avoids the visual fatigue of pure black.

- **Primary (Indigo-Slate):** Used for core actions and active states. It should feel grounded and stable.
- **Agent Accents:** These are used for semantic identification of AI personas. They avoid neon saturations in favor of rich, muted, and sophisticated pigments (Deep Royal Purple, Rich Terracotta, Muted Arctic, and Champagne).
- **Surface Palette:** Surfaces are constructed using varying opacities of the primary and neutral colors to create a layered "glass" effect without compromising legibility.

## Typography
The typography relies on **Outfit** to provide a modern, geometric base, but is styled with an editorial lens. 

- **Weight Contrast:** Use Light (300) for large display text and semi-bold (600) for labels to create a clear hierarchy. 
- **Character:** Headings should use tighter letter-spacing and lighter weights to evoke a premium, "tech-forward" feel.
- **Secondary Type:** For technical metadata or AI processing strings, Geist (monospaced) is used in a supporting role to contrast the warmth of the primary font.

## Layout & Spacing
The layout follows a **Fixed-Fluid hybrid grid**. On desktop, content is constrained to a 1440px max-width container with generous 48px external margins to ensure the "editorial" whitespace is preserved.

- **Grid:** A 12-column system for dashboard layouts, transitioning to a single-column stack on mobile.
- **Rhythm:** An 8px base grid is used for component internal spacing, while a 4px "fine-tune" unit is reserved for micro-adjustments like icon-to-text alignment.
- **Vertical Air:** Use expansive padding in agent interaction threads to prevent the "cluttered chatbot" look.

## Elevation & Depth
This design system rejects traditional drop shadows in favor of **Tonal Layering and Glassmorphism**.

- **Surfaces:** Layers are defined by `rgba(255, 255, 255, 0.03)` fills with a `blur(12px)` backdrop filter. 
- **Borders:** Every surface must have a "hairline" border of `1px`. The border uses a linear gradient (top-left to bottom-right) from `rgba(255, 255, 255, 0.1)` to `transparent`.
- **Depth Hierarchy:** 
  - Level 0: Background (#0a0c12)
  - Level 1: Glass Cards (low opacity)
  - Level 2: Modals / Popovers (higher opacity, more pronounced border)

## Shapes
The shape language is "Soft Geometric." It uses medium-radius rounding to feel approachable but maintains crisp lines to keep the "Professional" promise.

- **Primary Radius:** 8px for standard components like buttons and inputs.
- **Large Radius:** 16px to 24px for container cards and agent-response bubbles.
- **Interactive Elements:** Buttons should never be fully pill-shaped (unless they are small utility chips) to avoid a "toy-like" appearance.

## Components

- **Buttons:** Primary buttons use a solid #2563eb fill with no shadow. Secondary buttons use the glass style (low-opacity fill with hairline border).
- **Agent Cards:** These are the centerpiece. Each card should feature a subtle 2px left-accent border using the specific Agent Color (e.g., Terracotta for Sales) to denote ownership.
- **Inputs:** Darker than the surface level, with a 1px border that glows subtly when focused. Typography within inputs should remain at `body-md`.
- **Chips:** Used for "Agent Skills" or "Tags." These should be monochrome (white text on a 10% white background) to avoid competing with the Agent Accent colors.
- **Status Indicators:** Use small, non-glowing solid circles. Avoid "pulsing" animations; use subtle opacity transitions (80% to 100%) for active states.
- **Dividers:** Use a 1px solid line with `0.05` opacity; never use pure black or high-contrast white lines.