import os, tarfile

def make_targz(output_filename, source_dir):
    try:
        with tarfile.open(output_filename, "w:gz") as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))

        return True
    except Exception as e:
        print(e)
        return False

path_sufix = '_format'
emoji_path = 'emoji'
hotword_path = 'hotword'
tv_path = 'tv'
girl_path = '2233'

make_targz(f'{emoji_path}.tar.gz', emoji_path + path_sufix)
make_targz(f'{hotword_path}.tar.gz', hotword_path + path_sufix)
make_targz(f'{tv_path}.tar.gz', tv_path + path_sufix)
make_targz(f'{girl_path}.tar.gz', girl_path + path_sufix)