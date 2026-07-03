def split_text(text: str, chunk_size: int = 3000, max_chunks: int = 3):
    if not text:
        return []

    chunks = []
    start = 0

    while start < len(text) and len(chunks) < max_chunks:
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end

    return chunks