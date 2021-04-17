import sys
from cx_Freeze import setup, Executable

executables  = [
    Executable("gui.py",
    base = "Win32GUI"),
]

setup(name='DDoS Attack and Prevention',
    version='1',
    description="Applicaton to predict DDoS attack",
    executables=executables,
    options = {
    'build_exe': {
        "excludes": ["scipy.spatial.transform._rotation_groups"],
        'packages':["pandas", "pandas", "numpy", "sklearn", "sklearn.tree"],
    },

}
)