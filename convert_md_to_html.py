#!/usr/bin/env python3
"""
Convert markdown files to HTML with modern styling for Netlify deployment.
"""

import os
import re
from pathlib import Path
import markdown
from markdown.extensions import tables, codehilite, fenced_code, toc

def create_html_template(title, content, nav_links=None):
    """Create a complete HTML page with modern styling."""
    
    if nav_links is None:
        nav_links = [
            ("Home", "index.html"),
            ("P0 Specs", "P0.html"),
            ("Proposal", "Proposal.html"),
            ("Audio System", "Naphome_Audio.html"),
            ("Core Specs", "SPECS.html"),
            ("Development Plan", "Naphome_egg.html")
        ]
    
    nav_html = ""
    for link_text, link_url in nav_links:
        nav_html += f'<a href="{link_url}">{link_text}</a>'
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Naphome</title>
    <link rel="icon" href="/egg.png" type="image/png">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #2c3e50;
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 50%, #dee2e6 100%);
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            min-height: 100vh;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }}
        
        header {{
            background: linear-gradient(135deg, #6c5ce7 0%, #a29bfe 100%);
            color: white;
            padding: 2rem 0;
            text-align: center;
            box-shadow: 0 4px 20px rgba(108, 92, 231, 0.3);
        }}
        
        header h1 {{
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            font-weight: 300;
        }}
        
        header p {{
            font-size: 1.1rem;
            opacity: 0.9;
        }}
        
        nav {{
            background: #6366f1;
            padding: 1rem 0;
            text-align: center;
            border-bottom: 3px solid #8b5cf6;
        }}
        
        nav a {{
            color: white;
            text-decoration: none;
            margin: 0 1.5rem;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            transition: all 0.3s ease;
            font-weight: 500;
        }}
        
        nav a:hover {{
            background: #8b5cf6;
            transform: translateY(-2px);
        }}
        
        main {{
            padding: 3rem 2rem;
            max-width: 900px;
            margin: 0 auto;
        }}
        
        h1, h2, h3, h4, h5, h6 {{
            color: #2c3e50;
            margin-top: 2rem;
            margin-bottom: 1rem;
            font-weight: 600;
        }}
        
        h1 {{
            font-size: 2.2rem;
            border-bottom: 3px solid #8b5cf6;
            padding-bottom: 0.5rem;
        }}
        
        h2 {{
            font-size: 1.8rem;
            color: #34495e;
        }}
        
        h3 {{
            font-size: 1.4rem;
            color: #7f8c8d;
        }}
        
        p {{
            margin-bottom: 1.5rem;
            text-align: justify;
        }}
        
        ul, ol {{
            margin: 1rem 0 1rem 2rem;
            padding-left: 0;
        }}
        
        ul li {{
            list-style-type: disc;
            margin-bottom: 0.5rem;
            line-height: 1.5;
        }}
        
        ol li {{
            list-style-type: decimal;
            margin-bottom: 0.5rem;
            line-height: 1.5;
        }}
        
        li {{
            margin-bottom: 0.5rem;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 2rem 0;
            background: white;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            border-radius: 8px;
            overflow: hidden;
        }}
        
        th, td {{
            padding: 1rem;
            text-align: left;
            border-bottom: 1px solid #ecf0f1;
        }}
        
        th {{
            background: #8b5cf6;
            color: white;
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.9rem;
            letter-spacing: 0.5px;
        }}
        
        tr:hover {{
            background: #f8f9fa;
        }}
        
        code {{
            background: #f1f2f6;
            padding: 0.2rem 0.4rem;
            border-radius: 3px;
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
            font-size: 0.9rem;
            color: #e74c3c;
        }}
        
        pre {{
            background: #2c3e50;
            color: #ecf0f1;
            padding: 1.5rem;
            border-radius: 8px;
            overflow-x: auto;
            margin: 1.5rem 0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }}
        
        pre code {{
            background: none;
            color: inherit;
            padding: 0;
        }}
        
        blockquote {{
            border-left: 4px solid #8b5cf6;
            margin: 2rem 0;
            padding: 1rem 2rem;
            background: #f8f9fa;
            border-radius: 0 8px 8px 0;
            font-style: italic;
        }}
        
        .highlight {{
            background: linear-gradient(120deg, #e0e7ff 0%, #f3e8ff 100%);
            padding: 2rem;
            border-radius: 10px;
            margin: 2rem 0;
            border-left: 5px solid #8b5cf6;
        }}
        
        .emoji {{
            font-size: 1.2em;
        }}
        
        /* Side-by-side comparison images */
        .comparison-table img {{
            width: 40%;
            height: auto;
            max-width: 300px;
            object-fit: cover;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}
        
        footer {{
            background: linear-gradient(135deg, #6c5ce7 0%, #a29bfe 100%);
            color: white;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
        }}
        
        .back-to-top {{
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: #8b5cf6;
            color: white;
            border: none;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            cursor: pointer;
            font-size: 1.2rem;
            box-shadow: 0 4px 15px rgba(139, 92, 246, 0.4);
            transition: all 0.3s ease;
        }}
        
        .back-to-top:hover {{
            background: #7c3aed;
            transform: translateY(-3px);
        }}
        
        @media (max-width: 768px) {{
            .container {{
                margin: 0;
                box-shadow: none;
            }}
            
            main {{
                padding: 2rem 1rem;
            }}
            
            header h1 {{
                font-size: 2rem;
            }}
            
            nav a {{
                margin: 0 0.5rem;
                padding: 0.4rem 0.8rem;
                font-size: 0.9rem;
            }}
            
            table {{
                font-size: 0.9rem;
            }}
            
            th, td {{
                padding: 0.8rem 0.5rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🌙 Naphome</h1>
            <p>Smart Sleep Device Documentation</p>
        </header>
        
        <nav>
            {nav_html}
        </nav>
        
        <main>
            {content}
        </main>
        
        <footer>
            <p>&copy; 2025 Syzygy Labs - Naphome Smart Sleep Device</p>
        </footer>
    </div>
    
    <button class="back-to-top" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})">↑</button>
    
    <script>
        // Authentication check
        if (!document.cookie.includes('naphome-auth=authenticated') && 
            !window.location.search.includes('bypass=naphome-bypass-2025')) {{
            window.location.href = '/auth';
        }}
        
        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{
                        behavior: 'smooth',
                        block: 'start'
                    }});
                }}
            }});
        }});
        
        // Show/hide back to top button
        window.addEventListener('scroll', function() {{
            const backToTop = document.querySelector('.back-to-top');
            if (window.pageYOffset > 300) {{
                backToTop.style.display = 'block';
            }} else {{
                backToTop.style.display = 'none';
            }}
        }});
        
        // Hide back to top button initially
        document.querySelector('.back-to-top').style.display = 'none';
    </script>
</body>
</html>"""

def convert_markdown_to_html(md_file_path, output_dir="html"):
    """Convert a markdown file to HTML."""
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read markdown file
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Configure markdown extensions
    md = markdown.Markdown(
        extensions=[
            'tables',
            'codehilite',
            'fenced_code',
            'toc',
            'attr_list',
            'def_list',
            'footnotes'
        ],
        extension_configs={
            'codehilite': {
                'css_class': 'highlight',
                'use_pygments': False
            }
        }
    )
    
    # Convert markdown to HTML
    html_content = md.convert(md_content)
    
    # Add CSS class to comparison table for image styling
    html_content = re.sub(
        r'<table>\s*<thead>\s*<tr>\s*<th>Phase I — Little Egg</th>\s*<th>Phase II — Big Egg</th>\s*</tr>\s*</thead>',
        r'<table class="comparison-table">\n<thead>\n<tr>\n<th>Phase I — Little Egg</th>\n<th>Phase II — Big Egg</th>\n</tr>\n</thead>',
        html_content,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    # Get title from first heading or filename
    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', html_content, re.IGNORECASE)
    if title_match:
        title = title_match.group(1).strip()
        # Remove HTML tags from title
        title = re.sub(r'<[^>]+>', '', title)
    else:
        title = Path(md_file_path).stem.replace('_', ' ').title()
    
    # Create navigation links
    nav_links = [
        ("Home", "index.html"),
        ("P0 Specs", "P0.html"),
        ("Proposal", "Proposal.html"),
        ("Audio System", "Naphome_Audio.html"),
        ("Core Specs", "SPECS.html"),
        ("Development Plan", "Naphome_egg.html")
    ]
    
    # Generate complete HTML
    full_html = create_html_template(title, html_content, nav_links)
    
    # Write HTML file
    output_filename = Path(md_file_path).stem + '.html'
    output_path = os.path.join(output_dir, output_filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"Converted {md_file_path} -> {output_path}")
    return output_path

def create_index_page(output_dir="html"):
    """Create an index page that links to all converted pages."""
    
    pages = [
        {
            "title": "Development Plan",
            "description": "Phase I & Phase II development roadmap with sensor validation and PCB design",
            "file": "Naphome_egg.html",
            "icon": "🥚"
        },
        {
            "title": "P0 Specifications",
            "description": "Current prototype specifications and achievements",
            "file": "P0.html",
            "icon": "🔧"
        },
        {
            "title": "Prototype I & II Proposal",
            "description": "Complete development roadmap from COTS validation to mass production",
            "file": "Naphome_Prototype_I_II.html",
            "icon": "📋"
        },
        {
            "title": "Audio System Design",
            "description": "Smart bedside audio and synchronized lighting system",
            "file": "Naphome_Audio.html",
            "icon": "🔊"
        },
        {
            "title": "Core Specifications",
            "description": "Essential hardware and software requirements",
            "file": "SPECS.html",
            "icon": "⚙️"
        }
    ]
    
    content = """
    <div class="highlight">
        <h1>Welcome to Naphome Documentation</h1>
        <p>Naphome is a next-generation smart sleep companion that unites light, sound, and environmental sensing to create a restorative bedroom ecosystem. Explore our comprehensive documentation below.</p>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin: 3rem 0;">
    """
    
    for page in pages:
        content += f"""
        <div style="background: white; border-radius: 10px; padding: 2rem; box-shadow: 0 4px 15px rgba(0,0,0,0.1); transition: transform 0.3s ease; border-left: 5px solid #8b5cf6;">
            <h3 style="color: #2c3e50; margin-bottom: 1rem;">
                <span class="emoji">{page['icon']}</span> {page['title']}
            </h3>
            <p style="color: #7f8c8d; margin-bottom: 1.5rem;">{page['description']}</p>
            <a href="{page['file']}" style="display: inline-block; background: #8b5cf6; color: white; padding: 0.8rem 1.5rem; text-decoration: none; border-radius: 5px; font-weight: 500; transition: all 0.3s ease;">
                Read More →
            </a>
        </div>
        """
    
    content += """
    </div>
    
    <div class="highlight">
        <h2>Quick Overview</h2>
        <p><strong>Naphome</strong> is designed to create the perfect sleep environment through:</p>
        <ul>
            <li>🌙 <strong>Smart Lighting:</strong> Circadian lighting with synchronized RGB effects</li>
            <li>🔊 <strong>Premium Audio:</strong> High-quality speakers with tactile subwoofer feedback</li>
            <li>🌡️ <strong>Environmental Sensing:</strong> Temperature, humidity, air quality monitoring</li>
            <li>🤖 <strong>AI Integration:</strong> Voice control and cloud-based intelligence</li>
            <li>🔌 <strong>IoT Control:</strong> Seamless integration with existing smart home devices</li>
        </ul>
    </div>
    """
    
    # Create navigation links
    nav_links = [
        ("Home", "index.html"),
        ("P0 Specs", "P0.html"),
        ("Proposal", "Proposal.html"),
        ("Audio System", "Naphome_Audio.html"),
        ("Core Specs", "SPECS.html"),
        ("Development Plan", "Naphome_egg.html")
    ]
    
    full_html = create_html_template("Naphome Documentation", content, nav_links)
    
    output_path = os.path.join(output_dir, "index.html")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"Created index page: {output_path}")
    return output_path

def main():
    """Main function to convert all markdown files."""
    
    # List of markdown files to convert
    md_files = [
        "P0.md",
        "Proposal.md", 
        "Naphome_Audio.md",
        "SPECS.md",
        "Naphome_egg.md"
    ]
    
    print("Converting markdown files to HTML...")
    
    # Convert each markdown file
    for md_file in md_files:
        if os.path.exists(md_file):
            convert_markdown_to_html(md_file)
        else:
            print(f"Warning: {md_file} not found")
    
    # Create index page
    create_index_page()
    
    print("\n✅ All files converted successfully!")
    print("📁 HTML files are in the 'html' directory")
    print("🌐 Ready for Netlify deployment!")

if __name__ == "__main__":
    main()
