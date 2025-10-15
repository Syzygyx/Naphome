# ⚡ Quick Vercel Setup Guide

## 🚀 Vercel Deployment (5 minutes)

### 1. Create Vercel Project
- Go to [vercel.com](https://vercel.com)
- Click "New Project" → Import Git Repository → Select Naphome repo
- Build settings: `pip install -r requirements.txt && python convert_md_to_html.py`
- Output directory: `html`

### 2. Get Credentials
- **Project ID**: Vercel Dashboard → Settings → General → Project ID
- **Team ID**: Vercel Dashboard → Settings → General → Team ID  
- **Auth Token**: [vercel.com/account/tokens](https://vercel.com/account/tokens) → Create token

### 3. Add GitHub Secrets
- Go to: `https://github.com/Syzygyx/Naphome/settings/secrets/actions`
- Add secrets:
  - `VERCEL_TOKEN` = Your auth token
  - `VERCEL_ORG_ID` = Your team ID
  - `VERCEL_PROJECT_ID` = Your project ID

### 4. Test
- Push any change to main branch
- Check: `https://github.com/Syzygyx/Naphome/actions`
- Your site will auto-deploy! 🎉

---

**That's it!** Your documentation will now automatically deploy to Vercel every time you push to GitHub.

📖 **Full guide**: [VERCEL_SETUP.md](VERCEL_SETUP.md)
