from rag import (
    extract_text_from_pdf,
    split_text
)

text = extract_text_from_pdf(
    "uploads/divyanshi_negi_internship_resume.pdf"
)

chunks = split_text(text)

print("Total Chunks:", len(chunks))

print("\nFIRST CHUNK:\n")
print(chunks[0])