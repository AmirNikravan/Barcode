import svgwrite

def create_svg(text, filename):
    # Create an SVG drawing
    dwg = svgwrite.Drawing(filename, profile='tiny', size=("400px", "100px"))

    # Add text to the drawing
    dwg.add(dwg.text(text, insert=(10, 50), fill='black', font_size='20px'))

    # Save the SVG file
    dwg.save()

if __name__ == "__main__":
    text = input("Enter the text for the SVG: ")
    filename = "output.svg"
    create_svg(text, filename)
    print(f"SVG file '{filename}' created with the text: {text}")
