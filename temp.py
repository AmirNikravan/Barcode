import cairosvg

# تعیین کردن رزولوشن بالا
cairosvg.svg2pdf(url="qt_api_test.svg", write_to="output.pdf", output_width=800, output_height=600)
