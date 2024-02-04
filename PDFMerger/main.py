import PyPDF2
import os

def list_pdf_files(directory):
    pdf_files = []
    for file in os.listdir(directory):
        if file.endswith(".pdf"):
            pdf_files.append(file)
    return pdf_files

def get_user_selection(pdf_files):
    selected_files = []
    print("Available PDF files in the directory:")
    for i, file in enumerate(pdf_files, 1):
        print(f"{i}. {file}")
    while True:
        selection = input("Enter the number of the PDF file you want to merge (or type 'done' to finish): ")
        if selection.lower() == 'done':
            break
        try:
            index = int(selection) - 1
            if 0 <= index < len(pdf_files):
                selected_files.append(pdf_files[index])
            else:
                print("Error: Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Error: Invalid input. Please enter a number or 'done'.")
    return selected_files

def merge_pdfs(pdf_files, output_path):
    merger = PyPDF2.PdfMerger()
    for file in pdf_files:
        file_path = os.path.join("PDFMerger/pdfStore", file)
        merger.append(file_path)
    with open(output_path, "wb") as output_file:
        merger.write(output_file)

if __name__ == "__main__":
    pdf_files = list_pdf_files("PDFMerger/pdfStore")
    if pdf_files:
        selected_files = get_user_selection(pdf_files)
        if selected_files:
            # Generate the output filename based on the original filenames
            output_filename = "_".join(os.path.splitext(os.path.basename(file))[0] for file in selected_files) + "_merge.pdf"
            output_path = os.path.join("PDFMerger/pdfStore", output_filename)
            merge_pdfs(selected_files, output_path)
            print("PDF files merged successfully.")
            if os.path.exists(output_path):
                print(f"Merged PDF file saved at '{output_path}'.")
                os.startfile(output_path)
            else:
                print(f"Error: Merged PDF file '{output_path}' not found.")
        else:
            print("No PDF files selected for merging.")
    else:
        print("No PDF files found in the directory.")
