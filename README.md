# 🌙 Naphome Smart Sleep Device

A next-generation smart sleep companion that unites light, sound, and environmental sensing to create a restorative bedroom ecosystem.

> **🔒 Private Repository** - This project and documentation are confidential and restricted to authorized team members only.

## 📚 Documentation

This repository contains comprehensive documentation for the Naphome project, including:

- **P0 Specifications** - Current prototype achievements and specifications
- **Prototype I & II Proposal** - Complete development roadmap from COTS validation to mass production
- **Audio System Design** - Smart bedside audio and synchronized lighting system
- **Core Specifications** - Essential hardware and software requirements

## 🌐 Live Documentation

The documentation is automatically converted to HTML and deployed to Netlify using GitHub Actions:

🔗 **[View Live Documentation](https://naphome-docs.netlify.app)** *(Password Protected)*

### 🚀 Automatic Deployment

- **Push to main** → Automatic production deployment
- **Pull requests** → Preview deployments with live links
- **No manual steps** required after initial setup
- **Access Control** → Site is password protected for security

## 🛠️ Local Development

### Prerequisites

- Python 3.11+
- Git

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Syzygyx/Naphome.git
   cd Naphome
   ```

2. **Set up virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install markdown
   ```

3. **Convert markdown to HTML:**
   ```bash
   python convert_md_to_html.py
   ```

4. **Preview locally:**
   ```bash
   cd html
   python3 -m http.server 8000
   ```
   Open http://localhost:8000 in your browser.

### Deployment

#### Automatic Deployment (Recommended)
The site automatically deploys when you push to GitHub thanks to GitHub Actions. No manual steps required!

#### Manual Deployment
To deploy updates manually:

```bash
./deploy.sh
```

This script will:
- Convert all markdown files to HTML
- Commit changes to git
- Push to GitHub
- Trigger Netlify deployment

#### Setting up GitHub Actions
For automatic deployment, follow the detailed setup guide:

📖 **[GitHub Actions Setup Guide](GITHUB_ACTIONS_SETUP.md)**

## 📁 Project Structure

```
Naphome/
├── .github/workflows/             # GitHub Actions workflows
│   ├── deploy.yml                 # Simple deployment workflow
│   └── netlify-deploy.yml         # Advanced deployment workflow
├── html/                          # Generated HTML files
│   ├── index.html                 # Main documentation page
│   ├── P0.html                    # P0 specifications
│   ├── Naphome_Prototype_I_II.html # Development roadmap
│   ├── Naphome_Audio.html         # Audio system design
│   └── SPECS.html                 # Core specifications
├── *.md                           # Source markdown files
├── convert_md_to_html.py          # HTML conversion script
├── deploy.sh                      # Manual deployment script
├── netlify.toml                   # Netlify configuration
├── GITHUB_ACTIONS_SETUP.md        # GitHub Actions setup guide
└── README.md                      # This file
```

## 🎨 Features

- **Responsive Design** - Works on desktop, tablet, and mobile
- **Modern Styling** - Clean, professional appearance with smooth animations
- **Navigation** - Easy navigation between documentation sections
- **Syntax Highlighting** - Code blocks with proper syntax highlighting
- **Tables** - Well-formatted tables for specifications and BOMs
- **Mobile Optimized** - Touch-friendly interface for mobile devices

## 🔧 Technical Details

- **HTML Generation**: Python script using the `markdown` library
- **Styling**: Custom CSS with modern design principles
- **Deployment**: Netlify with automatic GitHub integration
- **Performance**: Optimized for fast loading and SEO

## 📝 Contributing

1. Edit the markdown files in the root directory
2. Run `python convert_md_to_html.py` to generate HTML
3. Test locally with `python3 -m http.server 8000`
4. Commit and push changes
5. Netlify will automatically deploy the updates

## 📄 License

© 2025 Syzygy Labs - Naphome Smart Sleep Device

---

*For technical questions or support, please contact the development team.*
