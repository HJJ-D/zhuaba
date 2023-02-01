def import_all_databases():
    import os
    prefix = f'app{os.sep}model{os.sep}'
    for dir_name, dir_list, filename_list in os.walk(prefix):
        dir_name = dir_name[len(prefix):]
        for filename in filename_list:
            name, ext = os.path.splitext(filename)
            if ext != '.py' or name == '__init__':
                continue
            lib_name = f'app.model.{dir_name}.{name}' if dir_name != '' else f'app.model.{name}'
            __import__(lib_name)
