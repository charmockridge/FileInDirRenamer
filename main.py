import os


class FileInDirRenamer():
    Dir = ""
    Files = []
    Additional = ""

    def __init__(self, givenDir, givenAdd):
        self.Dir = givenDir
        self.Files = os.listdir(self.Dir)
        self.Additional = givenAdd

    def rename(self):
        for filename in self.Files:
            fName = os.path.splitext(filename)[0]
            ext = os.path.splitext(filename)[1]
            newName = fName + self.Additional + ext
            os.rename(
                os.path.join(
                    self.Dir, filename
                ),
                os.path.join(
                    self.Dir, newName
                )
            )

        self.reset()

    def reset(self):
        self.Dir = ""
        self.Files = []
        self.Additional = ""


if __name__ == "__main__":
    Directory = FileInDirRenamer(
        "PATH/TO/YOUR/DIRECTORY/HERE",
        "STRING THAT WILL BE AT THE END OF YOUR FILE NAMES"
    )

    Directory.rename()
