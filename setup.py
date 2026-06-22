import json, zipfile, tarfile, shutil
from urllib.request import urlopen, urlretrieve
from pathlib import Path


#idk what im doing

def fetch_maretf(dest='scr/PyVTFLib/bin'):
    tmp = Path('tmp')
    tmp.mkdir(exist_ok=True)
    
    releases = {
        'MareTF-Linux-x86_64.tar.zst':(
            'linux64',
            'maretf',
            tarfile.open,
            {'filter':'data'}
        ),
        'MareTF-Windows-x86_64.zip':(
            'win64',
            'maretf.exe',
            zipfile.ZipFile,
            {}
        )
    }
    
    for asset in json.loads(urlopen("https://api.github.com/repos/craftablescience/MareTF/releases/latest").read())["assets"]:
        if asset['name'] in releases:
            print(f"Downloading {asset['name']}...")
            urlretrieve(asset["browser_download_url"], tmp / asset['name'])
    
    for fname, (subdir, exe, opener, kwargs) in releases.items():
        extract_dir = tmp / subdir
        extract_dir.mkdir(exist_ok=True)
        
        with opener(tmp / fname, "r") as archive:
            archive.extractall(path=extract_dir, **kwargs)
        
        target = Path(dest) / subdir / exe
        target.parent.mkdir(parents=True, exist_ok=True)
        target.unlink(missing_ok=True)
        shutil.move(next(extract_dir.rglob(exe)), target)
        shutil.rmtree(extract_dir)
    
    shutil.rmtree(tmp)

if __name__ == "__main__":
    fetch_maretf()