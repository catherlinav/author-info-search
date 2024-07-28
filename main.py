#define function
def compute_stats(list_dict, name):
    #makes name all lowercase and strips it
    name = name.lower().strip()
    #variables for avg rating and total pages
    avg_rating = 0.0
    total_pages = 0
    #create a list of all the authors
    author_list = []
    for book in list_dict:
        if book['author'] not in author_list:
            author_list.append(book['author'])
    
    #checks if given name is an author in list_dict
    if name not in author_list:
        return (None, None)
    else:
        for book in bookshelf:
            if book['author'] == name:
                #put ratings into list
                total_rating = []
                total_rating.append(book['rating'])
                #add up total pages
                total_pages += book['number_of_pages']
        #calc avg_rating
        avg_rating = sum(total_rating) / len(total_rating)
        
        #return tuple of avg_rating and total_pages
        return (avg_rating, total_pages)



#global scope
bookshelf = [
    { 'title' : 'The Colour of Magic',
      'author': 'terry pratchett',
      'rating': 9,
      'number_of_pages': 268 },
    { 'title' : 'Dragonriders of Pern',
      'author': 'anne mccaffrey',
      'rating':8,
      'number_of_pages': 256 },
    { 'title' : 'The Hogfather',
      'author': 'terry pratchett',
      'rating': 10,
      'number_of_pages': 404 },
    {'title' : 'All the Weyrs of Pern',
      'author': 'anne mccaffrey',
      'rating': 7,
      'number_of_pages': 312 },
    { 'title' : 'Going Postal',
      'author': 'terry pratchett',
      'rating': 8,
      'number_of_pages': 372 }
    ]


books = bookshelf
author_name = input('Enter an author\'s first and last name: ')
avg_rate, total_pages = compute_stats(books, author_name)

    # returns a tuple containing: 
    # the average rating (as a float) for all the books by that author
    # the total number of pages (as an int) for all the books by that author
    
print(f'Average rating of {author_name}: {avg_rate}')
print(f'Total # of books pages of {author_name}: {total_pages}')
