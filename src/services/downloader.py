from pathlib import Path

DOWNLOAD_DIR = Path("data/downloads")
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)


async def save_pdf(document):
    file_name = document.file_name or "document.pdf"

    telegram_file = await document.get_file()

    save_path = DOWNLOAD_DIR / file_name

    await telegram_file.download_to_drive(
        custom_path=str(save_path)
    )

    return save_path