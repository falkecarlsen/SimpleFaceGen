from pathlib import Path
import random

from PIL import Image


class FaceGen:
    def __init__(self, width: int = 227, height: int = 227):
        self.width = width
        self.height = height
        self.bases = []
        self.hairs = []
        self.eyes = []
        self.noses = []
        self.mouths = []
        self.ears = []

        parts_dir = Path(__file__).parent / 'parts'
        for f in parts_dir.iterdir():
            if not f.is_file() or f.suffix != '.png':
                continue
            if f.stem.startswith('eyes'):
                self.eyes.append(f)
            elif f.stem.startswith('nose'):
                self.noses.append(f)
            elif f.stem.startswith('mouth'):
                self.mouths.append(f)
            elif f.stem.startswith('ears'):
                self.ears.append(f)
            elif f.stem.startswith('hair'):
                self.hairs.append(f)
            elif f.stem.startswith('base'):
                self.bases.append(f)

    @property
    def size(self):
        return self.width, self.height

    def generate(self) -> Image:
        img = Image.new('RGBA', self.size, color='white')

        base = Image.open(random.choice(self.bases))
        mouth = Image.open(random.choice(self.mouths))
        eyes = Image.open(random.choice(self.eyes))
        ears = Image.open(random.choice(self.ears))
        hair = Image.open(random.choice(self.hairs))
        nose = Image.open(random.choice(self.noses))

        img.paste(base, (0, 0), base)
        img.paste(mouth, (0, 0), mouth)
        img.paste(eyes, (0, 0), eyes)
        img.paste(nose, (0, 0), nose)
        img.paste(hair, (0, 0), hair)
        img.paste(ears, (0, 0), ears)

        return img


if __name__ == '__main__':
    FaceGen().generate().show()
