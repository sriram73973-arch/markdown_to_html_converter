import argparse
import sys
from core_converter import convert_markdown_to_html


def main():
    parser = argparse.ArgumentParser(
        description="Convert Markdown text or file to HTML."
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "-f",
        "--file",
        help="Path to the Markdown file to convert"
    )

    group.add_argument(
        "-t",
        "--text",
        help="Markdown text to convert"
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Path to save the converted HTML file"
    )

    args = parser.parse_args()

    markdown_content = ""
    input_source = ""

    # Direct text input
    if args.text:
        markdown_content = args.text
        input_source = "direct text"

    # File input
    elif args.file:
        input_source = args.file

        try:
            with open(args.file, "r", encoding="utf-8") as f:
                markdown_content = f.read()

        except FileNotFoundError:
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            sys.exit(1)

    # No input provided
    else:
        print(
            "Error: Please provide either a file path or text to convert.",
            file=sys.stderr
        )
        sys.exit(1)

    # Convert markdown to HTML
    html_output = convert_markdown_to_html(markdown_content)

    # Save output to file
    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(html_output)

            print(f"Successfully converted {input_source} to HTML: {args.output}")

        except Exception as e:
            print(
                f"Error: Failed to write output file: {args.output}",
                file=sys.stderr
            )
            print(e, file=sys.stderr)
            sys.exit(1)

    # Print HTML to terminal
    else:
        print(html_output)


if __name__ == "__main__":
    main()
    