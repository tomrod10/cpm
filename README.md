# CPM - Color Palette Maker

## Summary
CPM is an image based color palette generator CLI tool that can return color schemes in Hex and RGB. It will use various algorithms to generate different color schemes (monochromatic, analogous, complementary, split complementary, triadic, square, and rectangle (or tetradic).

## Main Features
- Image upload and processing
- Color palette generation in Hex, RGB and HLS
- Color palette generation in different color schemes
- Copy and paste generated color in Hex, RGB and HLS
- Let user select between 4 main color schemes (monochromatic, analogous, complementary, split complementary)

## Extra Features (Non-essential)

- In CLI show generated color palette in small squares
- Build CPM website using same color palette generating logic and algorithms as the CLI tool
- Generate the color scheme config for popular vim and nvim plugin managers
    - Lazy, packer, etc
- Generate color scheme config for different shells and shell config managers
- Have an ‘Explore’ page of popular color palettes
- Have a ranking or up vote / down vote system
- Share color palette feature via (link)


## Milestones
### M1 - Monochromatic Color Scheme Available
Users can now select `mono` as their color scheme when generating color palettes

Color Palettes:
![Screenshot from 2024-12-20 14-14-26](https://github.com/user-attachments/assets/3b2b0eb4-6230-4bd3-bbe0-3172b6ce9026)

### M2 - Analogous Color Scheme Available
Users can now select `alog` as their color scheme when generating color palettes

Color Palettes:
![Screenshot from 2025-02-12 20-18-28](https://github.com/user-attachments/assets/2d9c6840-480f-481a-9d5f-b2f24e237d47)

Image Used:
![dawgs](https://github.com/user-attachments/assets/fd59fad1-ae76-4e27-bb4c-a8507e203a2f)

## Tech

**Language:** Python

**Framework/Tools:** Pillow, colorsys

**Containerization:** Docker
