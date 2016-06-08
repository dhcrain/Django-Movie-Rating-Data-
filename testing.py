import csv


with open("data/u.item", encoding='latin1') as infile:
    rating = csv.reader(infile, delimiter="|")
    for row in rating:
        print(row[4])




def movie_import(apps, schema_editor):
    Movie = apps.get_model("movie", "Movie")
    with open("data/u.item", encoding='latin1') as infile:
        movie = csv.reader(infile, delimiter="|")
        for row in movie:
            Movie.objects.create(movie_id=row[0], movie_title=row[1], release_date=row[2], video_release_date=row[3],
                                 imdb_url=row[4], unknown=row[5], action=row[6], adventure=row[7], animation=row[8],
                                 childrens=row[9], comedy=row[10], crime=row[11], documentry=row[12], drama=row[13],
                                 fantasy=row[14], film_noir=row[15], horror=row[16], musical=row[17], mystery=row[18],
                                 romance=row[19], sci_fi=row[20], thriller=row[21], war=row[22], western=row[23])
    raise Exception("2 yay")


def rating_import(apps, schema_editor):
    Rating = apps.get_model("movie", "Rating")
    with open("data/u.data") as infile:
        rating = csv.reader(infile, delimiter="\t")
        for row in rating:
            # Foreign Key ????
            Rating.objects.create(user_id=Rater.user_id, item_id=Movie.movie_id, rating=row[2], timestamp=row[3])
    raise Exception("3 yay")