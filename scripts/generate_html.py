import filecmp
import sys
import xml.etree.ElementTree as ET

def generate_html(rss_content):
    # Parse the RSS content
    root = ET.fromstring(rss_content)
    items = root.findall("./channel/item")

    # Generate HTML content
    html_content = "<ol>"
    for item in items:
        title = item.find("title").text
        link = item.find("link").text
        description = item.find("description").text

        html_content += f"""
            <li>
                <a href="{link}">{title}</a>
                <p>{description}</p>
            </li>"""
    html_content += "</ol>"
    return html_content

def main():
    # Read RSS content from command line argument
    rss_content = sys.argv[1]

    # Generate HTML content from RSS
    html_content = generate_html(rss_content)

    # Check if the content of styled_rss_content.html is different from README.md
    if not filecmp.cmp('styled_rss_content.html', 'README.md'):
        # Write HTML content to styled_rss_content.html
        with open('styled_rss_content.html', 'w') as f:
            f.write(html_content)
        
        print("Content updated successfully.")
    else:
        # Content has not changed, no need to commit and push
        print("No changes detected, skipping commit and push.")

if __name__ == "__main__":
    main()
