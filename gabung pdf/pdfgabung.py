import PyPDF2

def gabungkan_pdf(file_list, output_filename):
    merger = PyPDF2.PdfMerger()
    
    for pdf in file_list:
        merger.append(pdf)
    
    merger.write(output_filename)
    merger.close()
    print(f"PDF berhasil digabungkan menjadi {output_filename}")

# Contoh penggunaan
file_pdf = ["Proposal Legalitas IEEE 2024 (1).pdf", "AD ART IEEE ITK FIX 2024_2025 (2).pdf"]
gabungkan_pdf(file_pdf, "hasil_gabungan.pdf")
