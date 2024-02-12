import sys

def main():
    styled_content_path = sys.argv[1]
    template_path = sys.argv[2]

    # Read the styled RSS content
    with open(styled_content_path, 'r') as f:
        styled_content = f.read()

    # Read the template content
    with open(template_path, 'r') as f:
        template_content = f.read()

    # Replace the placeholder with the styled content
    updated_content = template_content.replace('[[ARTICLES]]', styled_content)

    # Write the updated content to README.md
    with open('README.md', 'w') as f:
        f.write(updated_content)

if __name__ == "__main__":
    main()
