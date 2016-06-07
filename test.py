import csv


# def rater_import():
def rater_import(apps, schema_editor):
    Rater = apps.get_model("movie", "Rater")
    with open("data/u.user") as infile:
        movie = csv.reader(infile, delimiter="\t")
        for row in movie:
            Rater.objects.create(user_id=row[0], age=row[1], gender=row[2], occupation=row[3], zip_code=row[4])
    raise Exception("yay")

def movie_import(apps, schema_editor):
    Movie = apps.get_model("movie", "Movie")
    with open("data/u.item", encoding='latin1') as infile:
        rating = csv.reader(infile, delimiter="|")
        for row in rating:
            Movie.objects.create(movie_id=row[0], movie_title=row[1], release_date=row[2], video_release_date=row[3],
                                 imdb_url=row[4], unknown=row[5], action=row[6], adventure=row[7], animation=row[8],
                                 childrens=row[9], comedy=row[10], crime=row[11], documentry=row[12], drama=row[13],
                                 fantasy=row[14], film_noir=row[15], horror=row[16], musical=row[17], mystery=row[18],
                                 romance=row[19], sci_fi=row[20], thriller=row[21], war=row[22], western=row[23])


def rating_import(apps, schema_editor):
    Rating = apps.get_model("movie", "Rating")
    with open("data/u.data") as infile:
        rater = csv.reader(infile, delimiter="|")
        for row in rater:
            Rating.objects.create(user_id=row[0], item_id=row[1], rating=row[2], timestamp=row[3])
