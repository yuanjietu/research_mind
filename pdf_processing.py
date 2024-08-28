from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    return extract_text(pdf_path)

def extract_section(text, section_name):
    """Extracts a specific section from the text based on the section name."""
    start = text.find(section_name)
    if start == -1:
        return ""
    end = text.find("\n", start) + 1
    return text[start:end]

def extract_text_by_section(pdf_path):
    """Extract text from a PDF and split it into sections."""
    text = extract_text_from_pdf(pdf_path)
    sections = {
        "abstract": extract_section(text, "Abstract"),
        "introduction": extract_section(text, "Introduction"),
        "methods": extract_section(text, "Methods"),
        "results": extract_section(text, "Results"),
        "discussion": extract_section(text, "Discussion"),
        "references": extract_section(text, "References")
    }
    return sections
