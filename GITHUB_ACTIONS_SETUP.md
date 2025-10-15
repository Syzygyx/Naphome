# 🚀 GitHub Actions + Netlify Setup Guide

This guide will help you set up automatic deployment of your Naphome documentation to Netlify using GitHub Actions.

## 📋 Prerequisites

1. **GitHub Repository** - Your code is already in GitHub ✅
2. **Netlify Account** - Sign up at [netlify.com](https://netlify.com) if you haven't already
3. **Admin access** to your GitHub repository

## 🔧 Step 1: Create Netlify Site

### Option A: Connect via GitHub (Recommended)

1. Go to [app.netlify.com](https://app.netlify.com)
2. Click **"New site from Git"**
3. Choose **"GitHub"** as your Git provider
4. Select your **Naphome** repository
5. Configure build settings:
   - **Build command:** `source venv/bin/activate && python convert_md_to_html.py`
   - **Publish directory:** `html`
   - **Branch to deploy:** `main`
6. Click **"Deploy site"**

### Option B: Manual Site Creation

1. Go to [app.netlify.com](https://app.netlify.com)
2. Click **"New site"** → **"Deploy manually"**
3. Drag and drop your `html` folder (after running the conversion script)
4. Note down your **Site ID** from the site settings

## 🔑 Step 2: Get Netlify Credentials

### Get Site ID
1. In Netlify dashboard, go to **Site settings**
2. Under **"General"**, find **"Site details"**
3. Copy the **Site ID** (looks like: `abc123def-4567-8901-2345-678901234567`)

### Get Auth Token
1. Go to [app.netlify.com/user/applications#personal-access-tokens](https://app.netlify.com/user/applications#personal-access-tokens)
2. Click **"New access token"**
3. Give it a name like "Naphome GitHub Actions"
4. Click **"Generate token"**
5. **Copy the token immediately** (you won't see it again!)

## 🔐 Step 3: Configure GitHub Secrets

1. Go to your GitHub repository: `https://github.com/Syzygyx/Naphome`
2. Click **"Settings"** tab
3. In the left sidebar, click **"Secrets and variables"** → **"Actions"**
4. Click **"New repository secret"**
5. Add these two secrets:

### Secret 1: NETLIFY_AUTH_TOKEN
- **Name:** `NETLIFY_AUTH_TOKEN`
- **Value:** The personal access token you generated in Step 2

### Secret 2: NETLIFY_SITE_ID
- **Name:** `NETLIFY_SITE_ID`
- **Value:** The Site ID you copied in Step 2

## 🎯 Step 4: Test the Setup

1. **Commit and push** the GitHub Actions workflow:
   ```bash
   git add .github/
   git commit -m "Add GitHub Actions workflow for Netlify deployment"
   git push origin main
   ```

2. **Check the Actions tab** in your GitHub repository:
   - Go to `https://github.com/Syzygyx/Naphome/actions`
   - You should see the workflow running
   - Wait for it to complete (usually 2-3 minutes)

3. **Verify deployment** in Netlify:
   - Go to your Netlify dashboard
   - Check the **"Deploys"** tab
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
5. **Deploys** to Netlify (production or preview)
6. **Comments** on PRs with preview links

## 🎨 Features

- ✅ **Automatic deployment** on every push to main
- ✅ **Preview deployments** for pull requests
- ✅ **Build caching** for faster deployments
- ✅ **Artifact storage** for debugging
- ✅ **Deployment comments** on PRs
- ✅ **Error handling** and rollback support

## 🐛 Troubleshooting

### Common Issues:

**❌ "NETLIFY_AUTH_TOKEN not found"**
- Make sure you added the secret correctly in GitHub
- Check the secret name is exactly `NETLIFY_AUTH_TOKEN`

**❌ "NETLIFY_SITE_ID not found"**
- Make sure you added the secret correctly in GitHub
- Check the secret name is exactly `NETLIFY_SITE_ID`

**❌ "Build failed"**
- Check the Actions tab for detailed error logs
- Make sure your markdown files are valid
- Verify the Python conversion script works locally

**❌ "Deployment failed"**
- Check your Netlify site settings
- Verify the Site ID is correct
- Make sure your Netlify account is active

### Getting Help:

1. **Check GitHub Actions logs:**
   - Go to your repository → Actions tab
   - Click on the failed workflow
   - Expand the failed step to see detailed logs

2. **Check Netlify logs:**
   - Go to your Netlify dashboard
   - Click on the failed deployment
   - Check the build logs

3. **Test locally:**
   ```bash
   # Test the conversion script
   source venv/bin/activate
   python convert_md_to_html.py
   
   # Test the HTML files
   cd html
   python3 -m http.server 8000
   ```

## 🎉 Success!

Once everything is set up, your documentation will automatically deploy to Netlify every time you:

- Push changes to the main branch
- Merge a pull request
- Update any markdown file

Your site will be available at: `https://[your-site-name].netlify.app`

---

**Need help?** Check the GitHub Actions logs or Netlify deployment logs for detailed error information.
