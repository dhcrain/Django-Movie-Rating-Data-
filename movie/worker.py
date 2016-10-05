import csv
from datetime import datetime


def import_all_data(apps, schema_editor):
    Rater = apps.get_model("movie", "Rater")
    with open("data/u.user") as infile:
        rater = csv.reader(infile, delimiter="|")
        for row in rater:
            Rater.objects.create(id=row[0], age=row[1], gender=row[2], occupation=row[3], zip_code=row[4])

    Movie = apps.get_model("movie", "Movie")
    with open("data/u.item", encoding='latin1') as infile:
        movie = csv.reader(infile, delimiter="|")
        for row in movie:
            Movie.objects.create(id=row[0], movie_title=row[1], release_date=row[2], video_release_date=row[3],
                                 imdb_url=row[4], unknown=row[5], action=row[6], adventure=row[7], animation=row[8],
                                 childrens=row[9], comedy=row[10], crime=row[11], documentry=row[12], drama=row[13],
                                 fantasy=row[14], film_noir=row[15], horror=row[16], musical=row[17], mystery=row[18],
                                 romance=row[19], sci_fi=row[20], thriller=row[21], war=row[22], western=row[23])

    Rating = apps.get_model("movie", "Rating")
    with open("data/u.data") as infile:
        rating = csv.reader(infile, delimiter="\t")
        for row in rating:
            rater_user_id = Rater.objects.get(id=row[0])
            movie_movie_id = Movie.objects.get(id=row[1])
            time = datetime.fromtimestamp(float(row[3]))
            Rating.objects.create(user_id=rater_user_id, item_id=movie_movie_id, rating=row[2], timestamp=time)

    # raise Exception("1 yay")      # This is a great test
