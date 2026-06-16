from rag import (
    extract_text_from_pdf,
    split_text,
    create_vector_store,
    get_answer
)

text = extract_text_from_pdf(
    "uploads/divyanshi_negi_internship_resume.pdf"
)

chunks = split_text(text)

vectorstore = create_vector_store(chunks)

question = input("Ask a question: ")

answer = get_answer(
    vectorstore,
    question
)

print("\nANSWER:\n")
print(answer)