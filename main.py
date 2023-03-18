import os

def get_sources(name,version,source):
    suffix = {
        'ubuntu':[[
            ' main restricted universe multiverse',
            '-updates main restricted universe multiverse',
            '-backports main restricted universe multiverse',
            '-security main restricted universe multiverse',
        ],'-security main restricted universe multiverse'],
        'debian':[[
            ' main contrib non-free',
            '-updates main contrib non-free',
            '-backports main contrib non-free',
        ],'-security main contrib non-free']
    }
    sources = [f'deb {source}{name}/ {version}{i}' for i in suffix[name][0]]
    sources.append(f'deb {source}{name}-security {version}{suffix[name][1]}')
    return sources

if __name__ == '__main__':
    info = {
        'name':'',
        'version':'',
    }
    
    names = ['debian','ubuntu','arch*','manjaro']
    [print(f'{i}) {name}') for i,name in enumerate(names)]
    print('Please select your system')
    info['name'] = names[int(input(f'input 0-{len(names)-1}: '))]
    with open('/etc/os-release','r') as f:
        info['version'] = [i[i.index('=')+1:-1] for i in f.readlines() if 'VERSION_CODENAME=' in i][0]
    
    if input('change sources\n(y/n): ') == 'y':
        if info['name'] in ['ubuntu','debian']:
            os.system('cp /etc/apt/sources.list /etc/apt/sources.list.bak')
            sources_list = [
                ('THU ','https://mirrors.tuna.tsinghua.edu.cn/'),
                ('USTC','https://mirrors.ustc.edu.cn/')
            ]
            [print(f'{i}) {sources_name[0]}') for i,sources_name in enumerate(sources_list)]
            sources = get_sources(info['name'],info['version'],sources_list[int(input(f'input 0-{len(names)-1}: '))][1])
            with open('/etc/apt/sources.list','w') as f:
                [f.writelines(f'{i}\n') for i in sources]
            os.system('apt update && apt install git wget -y')