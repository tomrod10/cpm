# CPM - Color Palette Maker

## Summary
CPM is an image based color palette generator CLI tool that can return color schemes in Hex and RGB. It will use various algorithms to generate different color schemes (monochromatic, analogous, complementary, split complementary, triadic, square, and rectangle (or tetradic).

## Main Features
- Image upload and processing
- Color palette generation in Hex, RGB and HLS
- Color palette generation in different color schemes
- Copy and paste generated color in Hex, RGB and HLS
- Let user select between 4 main color schemes before generating (monochromatic, analogous, complementary, split complementary)

## Extra Features (Non-essential)

- In CLI show generated color palette in small squares
- Build CPM website using same color palette generating logic and algorithms as the CLI tool
- Generate the color scheme config for popular vim and nvim plugin managers
    - Lazy, packer, etc
- Generate color scheme config for different shells and shell config managers
- Have an ‘Explore’ page of popular color palettes
- Have a ranking or up vote / down vote system
- Share color palette feature via (link)

## Tech

**Language:** Python

**Framework/Tools:** Pillow, colorsys

**Deployment:** Docker
