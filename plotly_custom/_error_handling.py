def check_str(string, name='variabel') -> None:
    if type(string) is not str:
        raise ValueError(f'{name} is expected to be str!')
        
def check_bool(boolean, name='variabel') -> bool:
    if type(boolean) is not bool:
        raise ValueError(f'{name} is expected to be boolean!')

def check_mode(mode) -> None:
    if mode not in {'lines', 'markers', 'lines+markers'}:
        raise ValueError('mode is expected to be either "lines", "markers" or "lines+markers"!')