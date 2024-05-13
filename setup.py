from cx_Freeze import setup, Executable

setup(
    name="CardSplitter",
    version="1.0",
    description="CardSplitter",
    executables=[Executable("cardsplitter.py")]
)
