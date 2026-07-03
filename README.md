
# DocPilot AI - Telegram AI Document Assistant

<img width="1536" height="1024" alt="5965DA80-8738-41DF-9316-0DB2A02F13E9" src="https://github.com/user-attachments/assets/28e02dbb-7f2a-476f-8a11-81dfa928aedd" />

A Telegram bot that receives PDF files, extracts text using PDF parsing or OCR, cleans the extracted text, summarizes it with a local AI model using Ollama, and sends the result back to the user.

## Tech Stack

- Python
- Telegram Bot API
- Ollama
- Qwen2.5
- SQLite
- pdfplumber
- Tesseract OCR
- pdf2image
- Poppler

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
- Automatic OCR detection
- Local-first AI processing
- Smart PDF/OCR fallback

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
```

## Screenshots

### Start
<img width="1170" height="2532" alt="start" src="https://github.com/user-attachments/assets/73863a68-426c-40f3-89dd-7c42ab60e622" />

### OCR Processing
<img width="1170" height="2532" alt="ocr" src="https://github.com/user-attachments/assets/32bacbfb-4fda-4101-8004-752e53f7b333" />

### Summary Result
<img width="1170" height="2532" alt="suumary" src="https://github.com/user-attachments/assets/c7546e95-fe3e-479b-8088-c30927f0e071" />

## Future Improvements

- FastAPI Web API
- PostgreSQL
- User Authentication
- Web Dashboard
- Background Workers
- Multi-language Support

## License

MIT License
