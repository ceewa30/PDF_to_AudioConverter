# 📄🔊 PDF to Audio Converter

An efficient, lightweight **Python pipeline** that extracts textual content from multi-page PDF documents and synthesizes it directly into playable, high-quality **MP3 spoken audio files**. 

Perfect for turning textbooks, academic papers, or documents into personalized, on-demand audiobooks.

---

## ✨ Features

* **Multi-Page Processing:** Seamlessly reads through multi-page PDFs to capture continuous text structures.
* **Layout Cleaning:** Automatically strips out double whitespaces and line break artifacts left over by PDF structural encoding.
* **Natural Voice Engine:** Powered by the Google Text-to-Speech (`gTTS`) API for smooth, clear pronunciation.
* **Localization Ready:** Supports multi-language and regional accent switches directly via code parameters.

---

## 🛠️ Prerequisites & Installation

This project requires Python 3.7+ and an active internet connection (to reach the cloud text-to-speech API).

1. Clone this repository to your local system:
   ```bash
   git clone https://github.com
   cd YOUR_REPOSITORY_NAME
   ```

2. Install the required dependencies using `pip`:
   ```bash
   pip install pypdf gtts
   ```

---

## 🚀 Quick Start Guide

1. Place your target `.pdf` file in the project folder.
2. Open the script file and update the `input_pdf` path variable.
3. Execute the script:
   ```bash
   python converter.py
   ```


## 💡 Troubleshooting & Edge Cases

* **Empty Output / Scanned PDFs:** The `pypdf` module reads native text layers. If your PDF contains scanned images or book photos, the text extraction will yield empty pages. To fix this, you must introduce an optical character recognition tool like `pytesseract` or `pdfplumber` before passing text blocks to `gTTS`.
* **Internet Connection Required:** Because `gTTS` sends translation synthesis requests to Google's translation servers, the conversion process will throw an connection exception if your device goes offline.

---
