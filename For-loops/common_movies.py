############## Problem  1 #################### 
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the movie"
#Continue until they is atleast 3 movies they both like

#init variables
movies = input("What movies you like ? ")
#convert movies into a List
movies.split(',')
#FillinMissingCode
common_movies=[]
commonMovieCount = 0
while (True) :
    #ask the second friend for one movie at a time
    movie = input ( "What movie you like?")#FillinMissingCode)
    #Check if this movie is in the movie list
    if movie in movies:
    #if present, 
        commonMovieCount +=1
        common_movies.append(movie)
        print(f"You both like {movie}")
        #check if we reached the max
        if(commonMovieCount >= 3):
            break
        else:
            print ("Try again")
    else:
        print("Try again")

for movie in common_movies:
       print (f"{movie}\n") #FillinMissingCode - list all the common movies
