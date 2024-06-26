import svgwrite

def generate_svg_with_text(text, filename, width=1000, height=2000, font_size="12px", font_family="Arial"):
  """
  Creates an SVG file with the given text.

  Args:
      text: The text to be displayed in the SVG.
      filename: The filename to save the SVG file.
      width: The desired width of the SVG (default: 200 pixels).
      height: The desired height of the SVG (default: 100 pixels).
      font_size: The font size of the text (default: "12px").
      font_family: The font family of the text (default: "Arial").
  """

  # Create a new SVG drawing with a viewBox
  dwg = svgwrite.Drawing(filename, profile='tiny', viewBox=f"0 0 {width} {height}")

  # Define a text element
  text_element = dwg.text(text, insert=(10, 20), font_size=font_size, font_family=font_family)

  # Add text element to the drawing
  dwg.add(text_element)

  # Save the SVG file
  dwg.save()

# Example usage
text = "This is some sample text"
filename = "my_svg.svg"
generate_svg_with_text(text, filename)
