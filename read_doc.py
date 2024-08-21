from docx import Document


def read_docx_file(file_path):
    # 打开.docx文档
    doc = Document(file_path)

    # 读取文档中的所有段落文本
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)

    return '\n'.join(full_text)


file_path = "证明.doc"
content = read_docx_file(file_path)
print(content)
