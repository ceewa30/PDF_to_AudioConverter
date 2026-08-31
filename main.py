import os
from pypdf import PdfReader
from gtts import gTTS


def pdf_to_mp3(pdf_path, mp3_output_path, lang="en"):
    """
    Extract text from a multi-page PDF and synthesizes it into an MP3 file.
    Args:
        pdf_path (str): Path to the input PDF file.
        mp3_output_path (str): Path to the output MP3 file.
        lang (str): Language code for the text-to-speech synthesis (default is "en" for English).
    """
    print(f"Opening pdf file: {pdf_path} ....")

    try:
        reader = PdfReader(pdf_path)
    except Exception as e:
        print(f"Error opening PDF: {e}")
        return

    full_text = []
    total_pages = len(reader.pages)
    print(f"Processing {total_pages} pages...")

    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text:
            clean_text = " ".join(text.split())
            full_text.append(clean_text)
            print(f"Extracted text from page {page_num}")
        else:
            print(f"Warning: page {page_num} is empty or scanned (no selected text found).")

    combined_text = " ".join(full_text).strip()

    if not combined_text:
        print("Error: No textual content could be extracted from the PDF.")
        return

    print("Text extraction complete. Synthesizing audio...")
    tts = gTTS(text=combined_text, lang=lang, slow=False)

    try:
        tts.save(mp3_output_path)
        print(f"Success! Audio saved directly to: {mp3_output_path}")
    except Exception as e:
        print(f"Error saving audio file: {e}")


if __name__ == "__main__":
    input_pdf = "input.pdf"
    output_mp3 = "output.mp3"
    pdf_to_mp3(input_pdf, output_mp3, lang='en')