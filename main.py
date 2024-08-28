from pdf_processing import extract_text_by_section
from indexing import create_sectional_index, retrieve_information
from ai_interface import generate_response_with_context

def main():
    # Path to the research paper PDF
    pdf_path = "//Users/tuyuanjie/Documents/human_ai_teaming/original/data/research_paper.pdf"
    
    # Step 1: Extract text by section
    sections = extract_text_by_section(pdf_path)
    
    # Step 2: Create an index of the extracted sections
    index_dir = "indexdir"
    create_sectional_index(index_dir, sections)
    
    # Step 3: Interactive exploration
    print("Welcome to the research paper exploration tool.")
    while True:
        query = input("Ask a question about the paper or type 'exit' to quit: ")
        if query.lower() == "exit":
            break
        
        # Step 4: Retrieve relevant information
        retrieved_docs = retrieve_information(query, index_dir)
        print(retrieved_docs)
        context = "\n".join(retrieved_docs)  # Combine retrieved docs as context
        print(context)
        
        # Step 5: Generate response using the context
        response = generate_response_with_context(query, context)
        print(f"AI: {response}")
        
        feedback = input("Do you need further explanation? (yes/no): ")
        if feedback.lower() == "yes":
            follow_up = input("Please specify your follow-up question: ")
            response = generate_response_with_context(follow_up, context)
            print(f"AI: {response}")

if __name__ == "__main__":
    main()
