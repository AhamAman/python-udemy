import os
from weasyprint import HTML

INPUT_HTML = "document.html"
OUTPUT_PDF = "compiled_output.pdf"

def compile_html_to_pdf(html_path, pdf_path):
    """
    Reads a local HTML file with embedded styling, processes it through
    the WeasyPrint Paged Media layout engine, and generates a print-ready PDF.
    """
    print("🚀 Starting PDF Compilation Engine...")

    # Guard Gate 1: Check if input file exists
    if not os.path.exists(html_path):
        print(f"❌ Error: Source file '{html_path}' could not be located.")
        return

    try:
        print(f"📖 Reading layout from '{html_path}'...")
        
        # Guard Gate 2: Verify the file contains actual content
        if os.path.getsize(html_path) == 0:
            print("❌ Error: Source file is empty.")
            return

        print("🖨  Processing CSS rules and formatting pages...")
        
        # The Core Transformation Step:
        # WeasyPrint parses the HTML tree structure, attaches the CSS rules,
        # calculates document dimensions, cuts pages, and outputs a binary PDF vector stream.
        HTML(filename=html_path).write_pdf(pdf_path)

        print(f"✅ Success! Document compiled flawlessly into '{pdf_path}'.")

    except Exception as e:
        print(f"💥 Compilation Failed. Engine reported the following error:\n{str(e)}")

def main():
    compile_html_to_pdf(INPUT_HTML, OUTPUT_PDF)

if __name__ == "__main__":
    main()