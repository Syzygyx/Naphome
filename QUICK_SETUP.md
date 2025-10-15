# ⚡ Quick Setup Guide

## 🚀 GitHub Actions + Netlify (5 minutes)

### 1. Create Netlify Site
- Go to [app.netlify.com](https://app.netlify.com)
- Click "New site from Git" → GitHub → Select Naphome repo
- Build settings: `source venv/bin/activate && python convert_md_to_html.py`
- Publish directory: `html`

### 2. Get Credentials
- **Site ID**: Netlify Dashboard → Site Settings → General → Site details
- **Auth Token**: [Personal Access Tokens](https://app.netlify.com/user/applications#personal-access-tokens) → New token

### 3. Add GitHub Secrets
- Go to: `https://github.com/Syzygyx/Naphome/settings/secrets/actions`
- Add secrets:
  - `NETLIFY_AUTH_TOKEN` = Your personal access token
  - `NETLIFY_SITE_ID` = Your site ID

### 4. Test
- Push any change to main branch
- Check: `https://github.com/Syzygyx/Naphome/actions`
- Your site will auto-deploy! 🎉

---

**That's it!** Your documentation will now automatically deploy every time you push to GitHub.

📖 **Full guide**: [GITHUB_ACTIONS_SETUP.md](GITHUB_ACTIONS_SETUP.md)
