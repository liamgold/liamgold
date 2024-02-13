import filecmp
import sys
import xml.etree.ElementTree as ET

def generate_markdown(rss_content):
    # Parse the RSS content
    root = ET.fromstring(rss_content)
    items = root.findall("./channel/item")

    # Generate Markdown content
    markdown_content = ""
    for index, item in enumerate(items):
        title = item.find("title").text
        link = item.find("link").text
        description = item.find("description").text

        markdown_content += f"**[{title}]({link})**  \n{description}\n\n"

        # Add separator line if not the last item
        if index < len(items) - 1:
            markdown_content += "\n"

    return markdown_content

def main():
    # Read RSS content from command line argument
    rss_content = sys.argv[1]

    # Generate Markdown content from RSS
    markdown_content = generate_markdown(rss_content)

    # Check if the content of styled_rss_content.html is different from README.md
    if not filecmp.cmp('styled_rss_content.html', 'README.md'):
        # Write Markdown content to styled_rss_content.html
        with open('styled_rss_content.html', 'w') as f:
            f.write(markdown_content)

if __name__ == "__main__":
    main()
