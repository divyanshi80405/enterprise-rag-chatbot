from rag import (
    extract_text_from_pdf,
    split_text,
    create_vector_store
)

text = extract_text_from_pdf(
    "uploads/divyanshi_negi_internship_resume.pdf"
)

chunks = split_text(text)

vectorstore = create_vector_store(chunks)

query = input("Ask a question: ")

docs = vectorstore.similarity_search(
    query,
    k=3
)

print("\nTOP MATCHES:\n")

for doc in docs:
    print(doc.page_content)
    print("-" * 50)