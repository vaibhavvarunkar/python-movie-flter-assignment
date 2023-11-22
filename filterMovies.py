import csv
from reportlab.pdfgen import canvas


class generatePdf:

    def createPdf(data, heading):
        width, height = 650, 800
        line_height = 15

        pdf = canvas.Canvas(
            f"{heading}.pdf", pagesize=(width, height))

        y_position = height - 50

        for line in data:
            pdf.drawString(50, y_position, line)
            y_position -= line_height

            if y_position < 50:
                pdf.showPage()
                y_position = height - 50

        pdf.save()
        print("PDF Generation Successfull!")


class filterOptions:
    def __init__(self, filename):
        self.filename = filename

    def filterByLanguage(self, language):
        filtered_movies = []
        with open(self.filename, newline='') as file:
            csvFile = csv.DictReader(file)
            for row in csvFile:
                if row['language'].lower() == language.lower():
                    filtered_movies.append(row['title'])
        return filtered_movies

    def filterByCountry(self, country):
        filtered_movies = []
        with open(self.filename, newline='') as file:
            csvFile = csv.DictReader(file)
            for row in csvFile:
                if row['country'].lower() == country.lower():
                    filtered_movies.append(row['title'])
        return filtered_movies

    def RatingGreaterThan7(self):
        filtered_movies = []
        with open(self.filename, newline='') as file:
            csvFile = csv.DictReader(file)
            for row in csvFile:
                imdb_rating = row.get("imdbRating")
                if imdb_rating and float(imdb_rating) > 7.0:
                    filtered_movies.append(row['title'])
        return filtered_movies

    def RatingGreaterThan1000(self):
        filtered_movies = []
        with open(self.filename, newline='') as file:
            csvFile = csv.DictReader(file)
            for row in csvFile:
                rating = row.get("rating")
                if rating and (type(rating) == int or (type(rating) == float and int(rating) > 1000)):
                    filtered_movies.append(row['title'])
        return filtered_movies

    def BasedOnYear(self, year):
        filtered_movies = []
        with open(self.filename, newline='') as file:
            csvFile = csv.DictReader(file)
            for row in csvFile:
                if row['year'] == year:
                    filtered_movies.append(row['title'])
        return filtered_movies

def main():
    print("\t\t\tIMDB DATA SET")
    while True:
        print("\n\t\t   FILTER MOVIES BASED ON\n")
        print("1. Language")
        print("2. Country")
        print("3. Movies with IMDB rating more greater than 7 ")
        print("4. Movies with ratings greater than 1000")
        print("5. Year")
        print("6. Exit\n")
        choice = int(input("What you want: "))
        filter = filterOptions("movies_initial.csv")
        match choice:
            case 1:
                language = str(input("Enter the language to be filtered: "))
                filtered_movies = filter.filterByLanguage(language)
                generatePdf.createPdf(
                    filtered_movies, f"Filtered by {language}")
            case 2:
                country = str(input("Enter the language to be filtered: "))
                filtered_movies = filter.filterByCountry(country)
                generatePdf.createPdf(
                    filtered_movies, f"Filtered by {country}")
            case 3:
                filtered_movies = filter.RatingGreaterThan7()
                generatePdf.createPdf(
                    filtered_movies, "Movies having IMDB rating more greater than 7")
            case 4:
                filtered_movies = filter.RatingGreaterThan1000()
                if filtered_movies:
                    generatePdf.createPdf(
                        filtered_movies, "Movies having  rating more greater than 1000 ")
                else:
                    generatePdf.createPdf(
                        filtered_movies, "No Movies")
            case 5:
                year = str(input("Enter the year:"))
                filtered_movies = filter.BasedOnYear(year)
                if filtered_movies:
                    generatePdf.createPdf(
                        filtered_movies, f"Movies in the year {year}")
                else:
                    generatePdf.createPdf(
                        filtered_movies, "No Movies")
            case 6:
                break
            case default:
                print("Incorrect Choice")
        print("\n\n")


if __name__ == "__main__":
    main()