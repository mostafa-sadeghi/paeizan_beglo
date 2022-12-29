
# Files and pathlib
# f = open("f.txt", 'w')
# f.close()

# with open("f.txt", 'w') as f:
#     pass

import time
from pathlib import Path

# create a path:
# Path("c:\\Program Files\\Microsoft")
# Path(r"c:\Program Files\Microsoft")
# print(Path(r"c:\Program Files\Microsoft"))
# print(Path()/Path('ecommerce')/Path("shop"))

# print(Path().home())
# path = Path()/Path('ecommerce')/Path("shop/myapp.py")
# print(path.exists())
# print(path.is_file())
# print(path.is_dir())
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)

# path = path.with_name("file.txt")
# print(path)

# path = Path()/Path('woocommerce')
# path.mkdir()
# # path.rmdir()
# path.rename("target")
path = Path()/Path('ecommerce')
# print(path.iterdir())

# path_list = path.iterdir()
# paths = [p for p in path_list]
# print(paths)
# for p in path_list:
#     print(p)
# paths = [p for p in path.iterdir() if p.is_dir()]
# print(paths)
# paths = [p for p in path.rglob("*.py") if p.is_file()]
# print(paths)
# path = Path("ecommerce//temp.txt")
# path.write_text("")
# # path.unlink()
# print(time.ctime(path.stat().st_ctime))


# copy file

source = Path('ecommerce//temp.txt')
des = Path('ecommerce//temp2.txt')
des.write_text(source.read_text())
