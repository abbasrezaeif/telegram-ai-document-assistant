# DocPilot AI - Telegram AI Document Assistant

A Telegram bot that receives PDF files, extracts text using PDF parsing or OCR, cleans the extracted text, summarizes it with a local AI model using Ollama, and sends the result back to the user.

## Features

- Telegram Bot integration
- PDF upload support
- PDF text extraction with pdfplumber
- OCR support with Tesseract
- Persian + English OCR
- Text cleaning
- Chunk-based summarization
- Local AI summarization with Ollama
- SQLite database tracking
- Document status tracking
- Saves extracted text and summaries

## Workflow

```text
Telegram User
    ↓
Send PDF
    ↓
Download File
    ↓
Save Document in SQLite
    ↓
Extract Text with pdfplumber
    ↓
Fallback to OCR if needed
    ↓
Clean Text
    ↓
Split into Chunks
    ↓
Summarize with Ollama
    ↓
Save Summary
    ↓
Send Summary to Telegram