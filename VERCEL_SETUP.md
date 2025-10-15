# 🚀 Vercel Deployment Setup Guide

This guide will help you set up automatic deployment of your Naphome documentation to Vercel using GitHub Actions.

## 📋 Prerequisites

1. **GitHub Repository** - Your code is already in GitHub ✅
2. **Vercel Account** - Sign up at [vercel.com](https://vercel.com) if you haven't already
3. **Admin access** to your GitHub repository

## 🔧 Step 1: Create Vercel Project

### Option A: Connect via GitHub (Recommended)

1. Go to [vercel.com](https://vercel.com) and sign in
2. Click **"New Project"**
3. Choose **"Import Git Repository"**
4. Select your **Naphome** repository
5. Configure project settings:
   - **Framework Preset:** Other
   - **Root Directory:** `./` (leave as default)
   - **Build Command:** `pip install -r requirements.txt && python convert_md_to_html.py`
   - **Output Directory:** `html`
   - **Install Command:** `pip install -r requirements.txt`
6. Click **"Deploy"**

### Option B: Manual Project Creation

1. Go to [vercel.com](https://vercel.com)
2. Click **"New Project"**
3. Choose **"Browse All Templates"**
4. Select **"Empty"** template
5. Connect your GitHub repository
6. Configure the same settings as above

## 🔑 Step 2: Get Vercel Credentials

### Get Project ID and Org ID
1. In Vercel dashboard, go to your **Naphome** project
2. Go to **Settings** → **General**
3. Copy the **Project ID** (looks like: `prj_abc123def456`)
4. Copy the **Team ID** (looks like: `team_xyz789`)

### Get Auth Token
1. Go to [vercel.com/account/tokens](https://vercel.com/account/tokens)
2. Click **"Create Token"**
3. Give it a name like "Naphome GitHub Actions"
4. Set scope to **"Full Account"**
5. Click **"Create"**
6. **Copy the token immediately** (you won't see it again!)

## 🔐 Step 3: Configure GitHub Secrets

1. Go to your GitHub repository: `https://github.com/Syzygyx/Naphome`
2. Click **"Settings"** tab
3. In the left sidebar, click **"Secrets and variables"** → **"Actions"**
4. Click **"New repository secret"**
5. Add these three secrets:

### Secret 1: VERCEL_TOKEN
- **Name:** `VERCEL_TOKEN`
- **Value:** The auth token you generated in Step 2

### Secret 2: VERCEL_ORG_ID
- **Name:** `VERCEL_ORG_ID`
- **Value:** The Team ID you copied in Step 2

### Secret 3: VERCEL_PROJECT_ID
- **Name:** `VERCEL_PROJECT_ID`
- **Value:** The Project ID you copied in Step 2

## 🎯 Step 4: Test the Setup

1. **Commit and push** the Vercel configuration:
   ```bash
   git add vercel.json .github/workflows/
   git commit -m "Switch from Netlify to Vercel deployment"
   git push origin main
   ```

2. **Check the Actions tab** in your GitHub repository:
   - Go to `https://github.com/Syzygyx/Naphome/actions`
   - You should see the workflow running
   - Wait for it to complete (usually 2-3 minutes)

3. **Verify deployment** in Vercel:
   - Go to your Vercel dashboard
   - Check the **"Deployments"** tab
   - You should see a new deployment from GitHub Actions

## 🔄 How It Works

### Automatic Deployment Flow:
1. **Push to main branch** → Triggers production deployment
2. **Create Pull Request** → Creates preview deployment
3. **Merge PR** → Triggers production deployment

### What the GitHub Action Does:
1. **Checks out** your repository
2. **Sets up Python** environment
3. **Installs dependencies** (markdown library)
4. **Converts** all `.md` files to HTML
5. **Deploys** to Vercel (production or preview)
6. **Comments** on PRs with preview links

## 🎨 Features

- ✅ **Automatic deployment** on every push to main
- ✅ **Preview deployments** for pull requests
- ✅ **Build caching** for faster deployments
- ✅ **Artifact storage** for debugging
- ✅ **Deployment comments** on PRs
- ✅ **Error handling** and rollback support
- ✅ **Free hosting** with excellent performance

## 🔒 Security Setup (Important!)

Since this is a private repository, you should also secure your Vercel site:

1. **Go to Vercel Dashboard** → Your project → **Settings**
2. **Security** → **Password Protection**
3. **Enable password protection** and set a strong password
4. **Save changes**

This ensures your documentation is protected even if someone discovers the Vercel URL.

## 🐛 Troubleshooting

### Common Issues:

**❌ "VERCEL_TOKEN not found"**
- Make sure you added the secret correctly in GitHub
- Check the secret name is exactly `VERCEL_TOKEN`

**❌ "VERCEL_ORG_ID not found"**
- Make sure you added the secret correctly in GitHub
- Check the secret name is exactly `VERCEL_ORG_ID`

**❌ "VERCEL_PROJECT_ID not found"**
- Make sure you added the secret correctly in GitHub
- Check the secret name is exactly `VERCEL_PROJECT_ID`

**❌ "Build failed"**
- Check the Actions tab for detailed error logs
- Make sure your markdown files are valid
- Verify the Python conversion script works locally

**❌ "Deployment failed"**
- Check your Vercel project settings
- Verify the Project ID and Org ID are correct
- Make sure your Vercel account is active

### Getting Help:

1. **Check GitHub Actions logs:**
   - Go to your repository → Actions tab
   - Click on the failed workflow
   - Expand the failed step to see detailed logs

2. **Check Vercel logs:**
   - Go to your Vercel dashboard
   - Click on the failed deployment
   - Check the build logs

3. **Test locally:**
   ```bash
   # Test the conversion script
   pip install -r requirements.txt
   python convert_md_to_html.py
   
   # Test the HTML files
   cd html
   python3 -m http.server 8000
   ```

## 🎉 Success!

Once everything is set up, your documentation will automatically deploy to Vercel every time you:

- Push changes to the main branch
- Merge a pull request
- Update any markdown file

Your site will be available at: `https://[your-project-name].vercel.app` *(Password Protected)*

---

**Need help?** Check the GitHub Actions logs or Vercel deployment logs for detailed error information.
