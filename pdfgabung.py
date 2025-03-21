import PyPDF2

def gabungkan_pdf(file_list, output_filename):
    merger = PyPDF2.PdfMerger()
    
    for pdf in file_list:
        try:
            merger.append(pdf)
        except FileNotFoundError:
            print(f"File '{pdf}' tidak ditemukan. Pastikan nama file benar.")
            return
    
    merger.write(output_filename)
    merger.close()
    print(f"PDF berhasil digabungkan menjadi {output_filename}")

if __name__ == "__main__":
    print("Masukkan nama file PDF yang ingin digabungkan (ketik 'selesai' untuk mengakhiri):")
    file_pdf = []
    
    while True:
        file_name = input("Masukkan nama file: ").strip()
        if file_name.lower() == "selesai":
            break
        file_pdf.append(file_name)
    
    if not file_pdf:
        print("Tidak ada file yang dimasukkan. Program berhenti.")
    else:
        output_file = input("Masukkan nama output file (contoh: hasil_gabungan.pdf): ").strip()
        gabungkan_pdf(file_pdf, output_file)
