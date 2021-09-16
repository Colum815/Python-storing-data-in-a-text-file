bands_info = 'band_info.txt'


def create_file_if_empty():
    with open(bands_info, "w")as file:
        pass


def band_info(band, album, producer):
    with open(bands_info, "a")as file:
        file.write(f"{band},{album},{producer},no\n")


def list_band_info():
    with open(bands_info, "r")as file:
        lines = [line.strip().split(',') for line in file.readlines()]

        bands = [
            {'name': line[0], 'album': line[1], 'producer': line[2], 'listened to: ': line[3]}

            for line in lines

        ]

        return bands


def _save_all_info(bands):
    with open(bands_info, "w")as file:
        for band in bands:
            file.write(f"{band['name']},{band['album']},{band['producer']},{band['listened to: ']}\n")


def listened_to_album_info(user):
    bands = list_band_info()
    for band in bands:
        if user == band['album']:
            band['listened to: '] = "yes"
    _save_all_info(bands)


def delete_band_info(user):
    bands = list_band_info()
    bands = [band for band in bands if band['name'] != user]
    _save_all_info(bands)



