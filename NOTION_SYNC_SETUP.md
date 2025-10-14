# 📝 Notion Sync Setup Guide

This repository automatically syncs Markdown files to Notion using GitHub Actions and [NotionIt](https://pypi.org/project/notionit/).

## 🚀 Quick Setup

### 1. Create a Notion Integration

1. Go to [Notion Integrations](https://www.notion.so/my-integrations)
2. Click **"+ New integration"**
3. Give it a name (e.g., "Naphome GitHub Sync")
4. Select your workspace
5. Copy the **Internal Integration Token** (starts with `secret_`)

### 2. Create Notion Pages for Each Document

Create three pages in your Notion workspace:
- One for `Naphome_Prototype_I_II.md`
- One for `P0.md`
- One for `SPECS.md`

For each page:
1. Share the page with your integration:
   - Click **"Share"** in the top right
   - Search for your integration name
   - Click **"Invite"**
2. Copy the **Page ID** from the URL:
   - URL format: `https://www.notion.so/Your-Page-Title-{PAGE_ID}?pvs=4`
   - The PAGE_ID is the 32-character string (with dashes)

### 3. Add GitHub Secrets

Go to your GitHub repository settings:

1. Navigate to **Settings** → **Secrets and variables** → **Actions**
2. Click **"New repository secret"**
3. Add the following secrets:

| Secret Name | Value |
|-------------|-------|
| `NOTION_TOKEN` | Your Notion integration token (e.g., `secret_abc123...`) |
| `NOTION_PAGE_ID_PROTOTYPE` | Page ID for Naphome_Prototype_I_II.md |
| `NOTION_PAGE_ID_P0` | Page ID for P0.md |
| `NOTION_PAGE_ID_SPECS` | Page ID for SPECS.md |

### 4. Test the Workflow

The workflow will automatically run when:
- You push changes to any `.md` file on the `main` branch
- You manually trigger it from the **Actions** tab

To manually trigger:
1. Go to **Actions** tab in your GitHub repository
2. Click on **"Sync Markdown to Notion"**
3. Click **"Run workflow"**

## 📋 How It Works

The GitHub Action (`.github/workflows/notion-sync.yml`):
1. Triggers on pushes to `.md` files on the `main` branch
2. Installs Python and NotionIt
3. Uploads each markdown file to its corresponding Notion page
4. Preserves formatting, code blocks, tables, and headings

## 🔧 Supported Markdown Features

NotionIt supports:
- ✅ Headers (H1-H6)
- ✅ Bold, italic, strikethrough
- ✅ Code blocks with syntax highlighting
- ✅ Tables
- ✅ Lists (ordered and unordered)
- ✅ Links
- ✅ Images (if publicly accessible)
- ✅ Block quotes
- ✅ Horizontal rules

## 🛠️ Local Testing

To test NotionIt locally before pushing:

```bash
# Install NotionIt
pip install notionit

# Upload a file to Notion
notionit upload \
  --token "secret_YOUR_TOKEN" \
  --page-id "YOUR_PAGE_ID" \
  Naphome_Prototype_I_II.md
```

## 📚 Additional Resources

- [NotionIt Documentation](https://pypi.org/project/notionit/)
- [Notion API Documentation](https://developers.notion.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## 🔒 Security Notes

- **Never commit your Notion token** to the repository
- Always use GitHub Secrets for sensitive credentials
- The integration token only has access to pages you explicitly share with it
- You can revoke integration access at any time from Notion settings

## 📝 Updating the Workflow

To add more markdown files to sync:

1. Edit `.github/workflows/notion-sync.yml`
2. Add a new step following the existing pattern
3. Create a new GitHub secret for the page ID
4. Push the changes to trigger the workflow

Example:
```yaml
- name: Sync NEW_FILE.md to Notion
  env:
    NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}
  run: |
    notionit upload \
      --token "$NOTION_TOKEN" \
      --page-id "${{ secrets.NOTION_PAGE_ID_NEWFILE }}" \
      NEW_FILE.md
```

## 🐛 Troubleshooting

**Error: "Could not find page"**
- Verify the page ID is correct
- Ensure the page is shared with your integration

**Error: "Unauthorized"**
- Check that `NOTION_TOKEN` secret is set correctly
- Verify the token hasn't been revoked

**Workflow not triggering**
- Ensure you're pushing to the `main` branch
- Check that you modified a `.md` file
- View workflow logs in the Actions tab

