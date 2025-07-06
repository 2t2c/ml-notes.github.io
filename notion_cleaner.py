import os
import argparse
import re
import shutil
import glob

def slugify(name):
    # convert to lowercase and replace spaces with hyphens
    return name.lower().replace(' ', '-')

def strip_guid(name):
    # remove trailing 32 hex char GUID after space
    return re.sub(r'\s[0-9a-f]{32}$', '', name)

def is_preface(folder_names, file_name):
    # return True if stripped file_name matches any stripped folder_name in the list
    file_base = strip_guid(file_name)
    return any(file_base == strip_guid(folder_name) for folder_name in folder_names)

def rename_files_and_build_structure(src_root, dst_root):
    mkdocs_structure = {}
    # get all the folders and sub-folders
    folder_paths = glob.glob(os.path.join(src_root, '**/'), recursive=True)
    folder_names = [os.path.basename(os.path.normpath(p)) for p in folder_paths]
    folder_names = list(set(folder_names)) 
    for root, dirs, files in os.walk(src_root):
        rel_path = os.path.relpath(root, src_root)
        rel_parts = [] if rel_path == '.' else rel_path.split(os.sep)
        clean_parts = [slugify(strip_guid(p)) for p in rel_parts]
        dst_dir = os.path.join(dst_root, *clean_parts)
        os.makedirs(dst_dir, exist_ok=True)

        subtree = mkdocs_structure
        for part in [strip_guid(p) for p in rel_parts]:
            if part not in subtree:
                subtree[part] = {}
            elif isinstance(subtree[part], str):
                subtree[part] = {"__file__": subtree[part]}
            subtree = subtree[part]
        
        for filename in files:
            name, ext = os.path.splitext(filename)
            # copy certain file types only
            if ext not in ['.md', '.csv']:
                continue
            file_path = os.path.join(root, filename)
            clean_name = strip_guid(name)
            slug_name = slugify(clean_name) + ext
            dst_file = os.path.join(dst_dir, slug_name)
            
            if ext == '.md' and is_preface(folder_names, name):
                pref_dir = os.path.join(dst_dir, slug_name.split(".")[0])
                dst_file = os.path.join(pref_dir, 'preface.md')
                rel_file = os.path.relpath(dst_file, dst_root).replace('\\', '/')
                os.makedirs(pref_dir, exist_ok=True)
                shutil.copy2(file_path, dst_file)
                subtree[clean_name] = {"__file__": rel_file}
                # print(f"Copied {file_path} -> {dst_file} [as preface]")
            else:
                shutil.copy2(file_path, dst_file)
                if ext == '.md':
                    rel_file = os.path.relpath(dst_file, dst_root).replace('\\', '/')
                    subtree[clean_name] = {"__file__": rel_file}
                    # print(f"Copied {file_path} -> {dst_file}")

    return mkdocs_structure

def format_mkdocs_yaml(structure, prefix='', indent=2):
    lines = []

    def recurse(d, level):
        indent_str = ' ' * (level * indent)
        for key, val in d.items():
            if isinstance(val, dict):
                if set(val.keys()) == {'__file__'}:
                    lines.append(f"{indent_str}- '{key}': '{prefix}{val['__file__']}'")
                else:
                    lines.append(f"{indent_str}- '{key}':")
                    if '__file__' in val:
                        lines.append(f"{indent_str}  - 'Preface': '{prefix}{val['__file__']}'")
                    for subkey, subval in val.items():
                        if subkey == '__file__':
                            continue
                        if isinstance(subval, dict) and set(subval.keys()) == {'__file__'}:
                            lines.append(f"{indent_str}  - '{subkey}': '{prefix}{subval['__file__']}'")
                        else:
                            recurse({subkey: subval}, level + 1)
            else:
                lines.append(f"{indent_str}- '{key}': '{prefix}{val}'")

    recurse(structure, 0)
    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser(description='Clean Notion export and generate mkdocs.yml section.')
    parser.add_argument('--dir', required=True, help='Path to exported Notion root directory')
    parser.add_argument('--prefix', default='', help='Prefix path to prepend to mkdocs.yml file paths (optional)')
    args = parser.parse_args()

    src_dir = args.dir
    base_name = os.path.basename(os.path.normpath(src_dir))
    dst_dir = os.path.join(os.path.dirname(src_dir), slugify(base_name))

    os.makedirs(dst_dir, exist_ok=True)
    structure = rename_files_and_build_structure(src_dir, dst_dir)

    print("\nMkdocs.yml Section\n")
    prefix = args.prefix
    if prefix and not prefix.endswith('/'):
        prefix += '/'
    print(format_mkdocs_yaml(structure, prefix=prefix))

if __name__ == '__main__':
    main()
