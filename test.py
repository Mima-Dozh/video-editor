import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory(dir = 'D:\\py\\py.Task\\video-editor\\') as tmpdirname:
    path_dir = Path(tmpdirname)
    a_file = path_dir / 'a_txt'
    a_file.write_text("AAAAAAAA")
    b_file = path_dir / 'd_txt'
    b_file.write_text("AAAAAAAA")
    c_file = path_dir / 'c_txt'
    c_file.write_text("AAAAAAAA")
    d_file = path_dir / 'd_txt'
    d_file.write_text("AAAAAAAA")
    e_file = path_dir / 'e_txt'
    e_file.write_text("AAAAAAAA")
    print(*list(path_dir.glob('*')), sep = '\n')
