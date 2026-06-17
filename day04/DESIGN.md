---
name: Academic Hub
colors:
  surface: '#fcf8ff'
  surface-dim: '#dcd8e5'
  surface-bright: '#fcf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f2ff'
  surface-container: '#f0ecf9'
  surface-container-high: '#eae6f4'
  surface-container-highest: '#e4e1ee'
  on-surface: '#1b1b24'
  on-surface-variant: '#464555'
  inverse-surface: '#302f39'
  inverse-on-surface: '#f3effc'
  outline: '#777587'
  outline-variant: '#c7c4d8'
  surface-tint: '#4d44e3'
  primary: '#3525cd'
  on-primary: '#ffffff'
  primary-container: '#4f46e5'
  on-primary-container: '#dad7ff'
  inverse-primary: '#c3c0ff'
  secondary: '#006a61'
  on-secondary: '#ffffff'
  secondary-container: '#86f2e4'
  on-secondary-container: '#006f66'
  tertiary: '#703a00'
  on-tertiary: '#ffffff'
  tertiary-container: '#934e00'
  on-tertiary-container: '#ffd2b1'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2dfff'
  primary-fixed-dim: '#c3c0ff'
  on-primary-fixed: '#0f0069'
  on-primary-fixed-variant: '#3323cc'
  secondary-fixed: '#89f5e7'
  secondary-fixed-dim: '#6bd8cb'
  on-secondary-fixed: '#00201d'
  on-secondary-fixed-variant: '#005049'
  tertiary-fixed: '#ffdcc3'
  tertiary-fixed-dim: '#ffb77d'
  on-tertiary-fixed: '#2f1500'
  on-tertiary-fixed-variant: '#6e3900'
  background: '#fcf8ff'
  on-background: '#1b1b24'
  surface-variant: '#e4e1ee'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  sidebar-width: 260px
  header-height: 72px
  container-max: 1440px
  gutter: 24px
  margin-mobile: 16px
  stack-gap: 12px
---

## Brand & Style
The design system is centered on clarity, organization, and academic progress. It targets Computer Engineering students who require a high-density information environment that remains approachable and stress-free. 

The aesthetic is **Modern Corporate** with a focus on **Soft Minimalism**. It prioritizes a human-centric experience by using generous white space to reduce cognitive load during intense study sessions. The emotional response should be one of "controlled productivity"—feeling organized, empowered, and encouraged. We avoid the clinical, hollow feel of generic dashboards by introducing subtle tactile cues, like soft shadows and intentional color accents that represent different technical disciplines.

## Colors
The palette uses a crisp white foundation with layered grays to define hierarchy. 
- **Primary (Indigo):** Used for core navigation, primary actions, and HTML-related content.
- **Secondary (Teal):** Dedicated to CSS modules and success-state indicators.
- **Tertiary (Amber):** Focused on JavaScript modules and cautionary status updates.
- **Quaternary (Blue):** Reserved for Python modules and technical documentation links.
- **Neutral:** A range of Slate grays (from `#F8FAFC` to `#1E293B`) provides the structural scaffolding, ensuring the interface feels grounded and professional.

## Typography
This design system utilizes **Inter** exclusively to maintain a systematic, utilitarian, yet modern feel. 
- **Scale:** High contrast between headlines and body text helps students scan course names versus content quickly.
- **Weights:** Semi-bold (600) and Bold (700) are reserved for navigational anchors and card titles. Regular (400) is used for all instructional text to maximize legibility.
- **Hierarchy:** Use `label-caps` for overlines or category tags (e.g., "COURSE MODULE") to provide structure without adding visual bulk.

## Layout & Spacing
The layout follows a **Fixed Sidebar / Fluid Content** model.
- **Sidebar:** A persistent 260px left-hand column. Active states are indicated by a 4px vertical primary-color pill on the left edge and a subtle 10% opacity background tint.
- **Header:** A 72px tall fixed top-bar containing a centered search bar and right-aligned profile utility.
- **Grid:** A 12-column grid system is used for the main content area. Dashboard widgets (Cards) should typically span 3, 4, or 6 columns.
- **Responsive:** On tablet, the sidebar collapses into a hamburger menu. On mobile, margins reduce to 16px and all grid items stack vertically (12 columns).

## Elevation & Depth
Depth is achieved through **Ambient Shadows** and tonal layering rather than heavy borders.
- **Surface Level (Level 0):** Background uses `#F8FAFC`.
- **Card Level (Level 1):** White background (`#FFFFFF`) with a soft, diffused shadow: `0px 4px 20px rgba(0, 0, 0, 0.05)`.
- **Active/Hover Level (Level 2):** Increased shadow depth for interactive elements: `0px 10px 30px rgba(0, 0, 0, 0.08)`.
- **Sidebar:** Uses a subtle right-hand border (`1px solid #E2E8F0`) instead of a shadow to maintain a clean vertical axis.

## Shapes
The design system adopts a **Rounded** philosophy to soften the technical nature of the content.
- **Standard Cards:** 12px (`rounded-lg`) corner radius.
- **Buttons & Inputs:** 8px (`rounded-md`) corner radius.
- **Avatar & Progress Tracks:** Circular/Pill-shaped for organic contrast against the geometric grid.

## Components
- **Buttons:** Primary buttons use a solid Indigo fill with white text. Secondary buttons use a transparent background with a 1px border.
- **Course Chips:** Small badges with a light-tinted background (10% opacity) and high-contrast text color corresponding to the subject (e.g., Amber background with Dark Amber text for JS).
- **Progress Bars:** Thin, 8px tall rounded tracks. The background track is always `#F1F5F9` with the "filled" portion using the module's specific accent color.
- **Cards:** White containers with 24px internal padding. Title and metadata are separated by a 1px divider or generous whitespace.
- **Input Fields:** Search and form inputs use a light gray stroke (`#E2E8F0`) that thickens and changes to Indigo on focus.
- **Sidebar Nav:** Icons should be 20px, stroke-based, with a 2px weight to match the Inter font's visual density.