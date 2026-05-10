import markdown

def convert_markdown_to_html(markdown_text):
    """Convert a string of Markdown text to HTML."""
    try:
        html = markdown.markdown(markdown_text)
        return html
    except Exception as e:
        return f"Error converting Markdown to HTML: {e}"


if __name__ == "__main__":
    sample_markdown = """
# Hello World!
This is a "simple" example
- Item 1
- Item 2
```python
print("Hello from Python!")
```
"""
    html_output = convert_markdown_to_html(sample_markdown)
    print("--- sample Markdown ---")
    print(sample_markdown)
    print("\n--- converted HTML ---")
    print(html_output)