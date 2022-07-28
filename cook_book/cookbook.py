# import csv functionality
import csv


html = "<body>\n"

# opening in a way that will close the file when we are done
#with open("recipes.csv", "rb") as csvfile:

# reading file

file_name = 'recipes.csv'
delimiter = ','
quote_character = '"'

csv_recipes = open(file_name, 'rU')
csv_reader = csv.DictReader(csv_recipes, fieldnames=[], restkey='undefined-fieldnames', delimiter=delimiter, quotechar=quote_character)

current_row = 0

for row in csv_reader:
	current_row += 1

	# Use heading row as field names for all other rows
	if current_row == 1:
		csv_reader.fieldnames = row['undefined-fieldnames']
		continue
	if current_row > 1:
		html = html + "<section>\n <ul>\n"

		for data in row.values():
			html = html + "<li>" + str(data) + "</li>\n" #how do I describe value in key value pairs?
			#possibly list out every row['Title'] as an option and then if None, etc. should be able to loop through all of them generically though.

		html = html + "</ul>\n" + "</section\n"

print(html)

	#print(row['Title'] + '/' + row['Directions'])


		#for data in row:
		#	html = html + "<td>" + data + "</td>"



html = html + "</body>"