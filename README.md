# FacultyWell: Teacher Mutual Aid & Wellbeing Network

> A modern, responsive mutual aid and wellbeing platform for educators. Grounded in Dr. Angela Adair's educational leadership research on mentoring, mindfulness, and resilience.

---

## 🌐 Live Online Website

Once GitHub Pages is activated on this repository, the site is live at:
### 👉 **[https://adairgarrett.github.io/teacher.wellbeing/](https://adairgarrett.github.io/teacher.wellbeing/)**

---

## 🚀 How to Enable GitHub Pages (Takes 30 seconds)

If the site isn't live yet at the URL above, enable GitHub Pages in your repository settings:

1. Go to your repository settings: **[Repository Settings > Pages](https://github.com/adairgarrett/teacher.wellbeing/settings/pages)**
2. Under **Build and deployment > Source**, choose either:
   - **GitHub Actions** (recommended — the included `.github/workflows/deploy.yml` workflow will automatically deploy on every push)
   *OR*
   - **Deploy from a branch**: Select `main` branch and `/ (root)` folder, then click **Save**.
3. Within 1–2 minutes, your website will be live at:
   `https://adairgarrett.github.io/teacher.wellbeing/`

---

## ⚡ Alternative Free 1-Click Hosting Options

Because this is a clean, self-contained single-page application (`index.html`), it can also be hosted for free with zero configuration on:

- **Netlify**: Drag and drop the project folder onto [app.netlify.com/drop](https://app.netlify.com/drop) for instant deployment.
- **Vercel**: Import the `adairgarrett/teaching_wellbeing_website` repository directly at [vercel.com/new](https://vercel.com/new).
- **Cloudflare Pages**: Connect the GitHub repository and select `/` as the root directory.

---

## 💻 Local Preview

To preview the website locally on your computer:

```bash
# Using Python
py -m http.server 8000
```

Then open `http://localhost:8000` in your web browser.

---

## ✨ Features Included

1. **"What do you need today?" Request Hub**:
   - Multi-select needs (5-min classroom watch, urgent de-escalation, medical emergency, nurse escort, print/supplies run, mindful debrief).
   - Real-time campus board with status claiming ("I Can Step In!") and resolution tracking.
2. **"I Can Help" Availability Board**:
   - Teachers publish when they are available (periods, prep blocks, lunch, after school) and what assistance they can provide.
   - Live directory of standby colleagues.
3. **Interactive Wellbeing & Mindfulness**:
   - Interactive Box Breathing (4-4-4-4), Calm (4-7-8), and Transition (3-3) pacing visualizer with synthesized chimes.
   - Real-time audio soundscape generator (Soft Rain, Ocean Tide, Singing Bowl, Alpha Waves) using Web Audio API.
   - 60-Second Desk Somatics guided stretches.
   - Staff Gratitude & Kudos Wall.
4. **Interactive Educator SMART Goals**:
   - Five-dimension SMART goal wizard with educator templates (Departure boundaries, batch grading, morning quiet reset, mentoring).
   - Milestone progress tracking (+25% increments) and Print/PDF export.
5. **About Dr. Angela Adair**:
   - Bio highlighting her Doctorate in Educational Leadership from Auburn University and Program Evaluation Certification.
   - Research pillars: Mentoring, Mindfulness & Wellbeing, Resilience, Principal Preparation.
   - Institutional scaling roadmap from single-school pilot to multi-district network.
   - Contact email: `angelacadair@gmail.com`.
