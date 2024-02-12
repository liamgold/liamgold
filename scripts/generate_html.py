import xml.etree.ElementTree as ET
import sys

def generate_html(rss_content):
    # Parse the XML RSS content
    root = ET.fromstring(rss_content)

    # Start building the HTML content
    html_content = '<ol>'
    
    # Iterate over the items in the RSS feed
    for item in root.findall('.//item'):
        # Extract relevant information from each item
        title = item.find('title').text
        link = item.find('link').text
        description = item.find('description').text

        # Construct HTML for each item and append to the overall HTML content
        html_content += f'''
        <li>
            <a href="{link}">{title}</a>
            <p>{description}</p>
        </li>'''

    # Close the ordered list tag
    html_content += f'''
    </ol>'''
    
    return html_content

if __name__ == '__main__':
    # Read the RSS content from command-line argument
    rss_content = sys.argv[1]

    # Generate HTML content from the RSS content
    html_content = generate_html(rss_content)

    # Print the HTML content to standard output
    print(html_content)
