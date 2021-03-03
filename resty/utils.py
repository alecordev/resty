import datetime


def generate_filename_path(location_path, config):
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")
    path = location_path.joinpath(config["save_dir"])
    path.mkdir(exist_ok=True)
    filename = f"{config['save_prefix']}_{config['name'].lower().replace(' ', '_')}_{timestamp}.{config['save_extension'].lower()}"
    return path.joinpath(filename)
