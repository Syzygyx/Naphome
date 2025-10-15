# 🚀 Deploy Naphome to Vercel - Step by Step

## The 404 Error Fix

If you're getting a 404 error at `https://naphome.vercel.app`, it means the Vercel project hasn't been set up yet. Follow these steps:

## Step 1: Create Vercel Project

1. **Go to [vercel.com](https://vercel.com)** and sign in (or create account)
2. **Click "New Project"**
3. **Import Git Repository:**
   - Click "Import Git Repository"
   - Select your **Naphome** repository
   - Click "Import"

## Step 2: Configure Project Settings

In the project setup page:

1. **Project Name:** `naphome` (or your preferred name)
2. **Framework Preset:** Select "Other" or "Static Site"
3. **Root Directory:** Leave as `./` (default)
4. **Build Command:** `pip install -r requirements.txt && python convert_md_to_html.py`
5. **Output Directory:** `html`
6. **Install Command:** `pip install -r requirements.txt`

## Step 3: Deploy

1. **Click "Deploy"**
2. **Wait for deployment** (usually 2-3 minutes)
3. **Your site will be live** at `https://naphome.vercel.app` (or your chosen name)

## Step 4: Test Authentication

1. **Visit your site** - you should see the beautiful authentication page
2. **Enter password:** `Naphome2025!Secure`
3. **Access granted** - you'll see your documentation

## Step 5: Set Up GitHub Actions (Optional)

For automatic deployments:

1. **Get Vercel credentials:**
   - Go to your Vercel project → Settings → General
   - Copy **Project ID** and **Team ID**
   - Go to [vercel.com/account/tokens](https://vercel.com/account/tokens)
   - Create a new token

2. **Add GitHub secrets:**
   - Go to `https://github.com/Syzygyx/Naphome/settings/secrets/actions`
   - Add: `VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID`

## Troubleshooting

### Still getting 404?
- Check that the project name in Vercel matches the URL
- Verify the build completed successfully in Vercel dashboard
- Check the deployment logs for errors

### Build failing?
- Make sure Python 3.11 is selected in Vercel settings
- Check that `requirements.txt` exists
- Verify the build command is correct

### Authentication not working?
- Check browser console for JavaScript errors
- Verify the auth.html file was generated
- Try the bypass link: `https://naphome.vercel.app/?bypass=naphome-bypass-2025`

## Security Features

Your site now includes:
- ✅ **Password protection** with beautiful UI
- ✅ **Secure cookies** (7-day expiration)
- ✅ **Bypass token** for development
- ✅ **Security headers** (CSP, HSTS, etc.)
- ✅ **Client-side authentication** checks

## Quick Test

1. Visit: `https://naphome.vercel.app`
2. You should see the authentication page
3. Enter password: `Naphome2025!Secure`
4. Access your documentation!

---

**Need help?** Check the Vercel deployment logs or GitHub Actions logs for detailed error information.
