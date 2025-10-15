#!/bin/bash

# Naphome HTML Deployment Script
echo "🚀 Deploying Naphome documentation to Netlify..."

# Install dependencies and convert markdown to HTML
echo "📝 Converting markdown files to HTML..."
source venv/bin/activate
pip install -r requirements.txt
python convert_md_to_html.py

# Add and commit changes
echo "📦 Committing changes..."
git add html/
git add netlify.toml
git add convert_md_to_html.py
git add deploy.sh

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "✅ No changes to commit"
else
    git commit -m "Update HTML documentation for Netlify deployment
    
    - Converted all markdown files to styled HTML
    - Added Netlify configuration
    - Created deployment script
    - Ready for production deployment"
    echo "✅ Changes committed"
fi

# Push to remote
echo "🌐 Pushing to GitHub..."
git push origin main

echo "🎉 Deployment complete!"
echo "📋 Next steps:"
echo "   1. Go to https://app.netlify.com"
echo "   2. Connect your GitHub repository"
echo "   3. Set build directory to 'html'"
echo "   4. Deploy!"
echo ""
echo "🔗 Your site will be available at: https://[your-site-name].netlify.app"
