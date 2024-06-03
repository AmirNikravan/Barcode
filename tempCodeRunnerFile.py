import barcode
from barcode.writer import ImageWriter
ITF = barcode.get_barcode_class('itf')
itf = ITF('30573190692203003169482900832115201911297', writer=ImageWriter())
fullname = itf.save('itf_barcode', options={"write_text": False})