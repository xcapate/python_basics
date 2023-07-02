import mammoth

with open("test_xxx.docx", "rb") as docx_file:
	result = mammoth.convert_to_html(docx_file)
	html = result.value
	f=open("out.html","a")
	f.write(html)
	f.close()


